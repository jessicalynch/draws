from __future__ import annotations

import base64
import math
import mimetypes
import os
from pathlib import Path
from typing import TYPE_CHECKING, List, Union

from .graph import VertexId
from .layout import Layout, SugiyamaStrategy

if TYPE_CHECKING:
    from .diagram import Diagram, Elem


class DiagramRenderer:
    def __init__(self, diagram: "Diagram"):
        self.diagram = diagram

        self._output_height = -1
        self._output_width = -1
        self._dummy_elems = {}

    def render(self, filename: Union[str, Path] = None):
        svg_content = self._get_svg_elements(D=self.diagram)
        if not filename:
            filename = f"{self.diagram.title or self.diagram.id}.diagram.svg"

        filename = Path(filename)
        filename.parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w") as file:
            file.write(svg_content)

    def _get_assets_path(self) -> Path:
        curr_dir = Path(os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(curr_dir.parent, "assets")

    def _get_svg_elements(self, D: "Diagram"):
        layout = Layout(graph=D.graph, strategy=SugiyamaStrategy())
        layers = layout.layers
        self._layout_elems(layers=layers, D=D)
        self._calculate_optimal_dimensions(D=D)
        min_x, min_y, width, height = self._calculate_bounds(D=D)
        viewBox = f"{min_x} {min_y} {width} {height}"

        svg_defs = "<defs>"
        for defs_filename in ["font.html", "style.html"]:
            defs_file_path = os.path.join(
                self._get_assets_path(), "svg_defs", defs_filename
            )
            defs_file = open(defs_file_path, "r")
            defs = defs_file.read()
            svg_defs += defs
            defs_file.close()

        image_defs = self._get_image_defs(D.elems)
        for img_path, encoded_img in image_defs.items():
            svg_defs += (
                f'<pattern id="{os.path.basename(img_path)}"'
                + ' patternUnits="objectBoundingBox" width="100%" height="100%">'
            )
            svg_defs += (
                f'<image href="{encoded_img}" x="0" y="0"'
                + f' width="{D.icon_width}" height="{D.icon_height}"/>'
            )
            svg_defs += "</pattern>"
        svg_defs += "</defs>"

        svg_elements = [
            '<svg xmlns="http://www.w3.org/2000/svg" width="100%"'
            + f' viewBox="{viewBox}">',
            svg_defs,
        ]

        for elem in D.elems:
            # Draw connections
            for connected_elem in elem.connections:
                path_coords = self._get_path_coords(
                    start_elem=elem, end_elem=connected_elem, layers=layers
                )
                if len(path_coords) < 2:
                    continue

                path_coords = self._add_arrow_padding(
                    path_coords,
                    start_padding=D.arrow_padding,
                    end_padding=D.arrow_padding,
                )
                x_end, y_end = path_coords[-1]
                x_prev, y_prev = path_coords[-2]
                svg_path = self._coords_to_svg_path(path_coords)

                arrowhead_svg = self._get_arrow_path(
                    x_end,
                    y_end,
                    x_prev,
                    y_prev,
                    color=elem.color,
                    length=D.arrow_length,
                )

                svg_elements.append(
                    f'<g class="route"><path d="{svg_path}" stroke="{elem.color}"'
                    + f' stroke-width="{D.stroke_width}" fill="none" />'
                    + f"{arrowhead_svg}</g>"
                )

            # Draw icons
            icon_id = os.path.basename(elem.icon)
            icon_x = elem.x - D.icon_width / 2
            icon_y = elem.y - D.icon_height / 2
            svg_elements.append(
                f'<rect x="{icon_x}" y="{icon_y}" width="{D.icon_width}"'
                + f' height="{D.icon_height}" fill="url(#{icon_id})" />'
            )

            wrapped_lines = elem.wrapped_label.split("\n")
            text_x = elem.x
            text_y = elem.y + D.icon_height / 2 + D.label_margin
            label_width = elem.wrapped_label_width
            label_height = D.label_font_size * len(wrapped_lines) + 2 * D.label_margin

            # Draw label background
            rect_x = text_x - label_width / 2
            rect_y = elem.y + D.icon_height / 2 + D.label_margin - D.label_margin

            svg_elements.append(
                f'<rect x="{rect_x}" y="{rect_y}" width="{label_width}"'
                + f' height="{label_height}" fill="rgba(255,255,255,.4)" rx="10"/>'
            )

            label_height = D.label_font_size * len(wrapped_lines) + 2 * D.label_margin

            # Draw label
            for line_index, line in enumerate(elem.wrapped_label.split("\n")):
                text_y = (
                    elem.y
                    + D.icon_height / 2
                    + D.label_margin
                    + line_index * D.label_font_size
                )
                svg_elements.append(
                    f'<text style="font-size: {D.label_font_size}px;"'
                    + f' x="{text_x}" y="{text_y}" text-anchor="middle"'
                    + f' dominant-baseline="hanging">{line}</text>'
                )

        # Draw title
        if D.title:
            title_x = (self.output_width // 2) - D.padding
            title_y = 0

            svg_elements.insert(
                1,
                f'<text style="font-size: {D.title_font_size}px; font-weight: 700;"'
                + f' x="{title_x}" y="{title_y}" text-anchor="middle"'
                + f' dominant-baseline="middle">{D.title}</text>',
            )

        svg_elements.append("</svg>")

        return "\n".join(svg_elements)

    def _layout_elems(self, layers: List[List[VertexId]], D: "Diagram"):
        for layer_index, layer in enumerate(layers):
            for vertex_index, vertex_id in enumerate(layer):
                elem = next((n for n in D.elems if n.id == vertex_id), None)
                x = vertex_index * D.horizontal_spacing + D.padding
                y = layer_index * D.vertical_spacing + D.padding
                if D.title:
                    y += D.title_margin
                if elem:
                    elem.set_position(x, y)
                else:
                    dummy_elem = {"id": vertex_id, "x": x, "y": y}
                    self._dummy_elems[vertex_id] = dummy_elem

    def _calculate_optimal_dimensions(self, D: "Diagram"):
        max_x = max((elem.x + elem.total_width / 2 for elem in D.elems), default=0)
        max_y = max(
            (elem.y + elem.total_height for elem in D.elems),
            default=0,
        )

        self.output_width = max_x + D.padding
        self.output_height = max_y + D.padding
        if D.title:
            self.output_height += D.title_font_size + D.title_margin

    def _calculate_bounds(self, D: "Diagram"):
        if not D.elems:
            return 0, 0, 0, 0

        min_x = min(elem.x for elem in D.elems) - D.icon_width - D.padding
        max_x = max(elem.x for elem in D.elems) + D.icon_width + D.padding
        min_y = min(elem.y for elem in D.elems) - D.icon_height - D.padding
        if D.title:
            min_y -= D.title_margin
        max_y = max(elem.y for elem in D.elems) + D.icon_height * 2 + D.padding

        width = max_x - min_x
        height = max_y - min_y
        return min_x, min_y, width, height

    def _get_image_defs(self, elems):
        unique_images = set(elem.icon for elem in elems)
        image_defs = {}
        for filename in unique_images:
            mime_type, _ = mimetypes.guess_type(filename)
            icon_path = os.path.join(self._get_assets_path(), "icons", filename)
            if not os.path.exists(icon_path):
                raise ValueError(f"Icon asset not found: {filename}")

            with open(icon_path, "rb") as icon_file:
                encoded_string = base64.b64encode(icon_file.read()).decode()
                image_defs[filename] = f"data:{mime_type};base64,{encoded_string}"
        return image_defs

    def _offset_coords(
        self, coords: List[List[int]], direction: str, offset_amount: int
    ):
        x, y = coords
        if direction == "left":
            return x - offset_amount, y
        elif direction == "right":
            return x + offset_amount, y
        elif direction == "top":
            return x, y - offset_amount
        elif direction == "bottom":
            return x, y + offset_amount

    def _get_path_direction(self, xy1: List[List[int]], xy2: List[List[int]]):
        x1, y1 = xy1
        x2, y2 = xy2

        if abs(x1 - x2) > abs(y1 - y2):
            return "left" if x1 > x2 else "right"
        else:
            return "top" if y1 > y2 else "bottom"

    def _get_path_coords(
        self, start_elem: "Elem", end_elem: "Elem", layers: List[List[str]]
    ) -> List[List[int]]:
        if not start_elem or not end_elem:
            return []

        path = [start_elem.position]
        start_layer_index = next(
            (i for i, layer in enumerate(layers) if start_elem.id in layer), None
        )
        end_layer_index = next(
            (i for i, layer in enumerate(layers) if end_elem.id in layer), None
        )

        range_to_check = (
            range(start_layer_index, end_layer_index)
            if start_layer_index <= end_layer_index
            else range(end_layer_index, start_layer_index)
        )

        for layer_index in range_to_check:
            curr_layer = layers[layer_index]
            next_layer = layers[layer_index + 1]

            if end_elem.id in curr_layer or end_elem.id in next_layer:
                path.append(end_elem.position)
                break
            else:
                layer_dummy_elems = [d for d in next_layer if "dummy" in d]

                if not len(layer_dummy_elems):
                    raise ValueError("No dummy elem in next layer")

                dummy_elem = self._dummy_elems[layer_dummy_elems[0]]
                if not dummy_elem.get("x") or not dummy_elem.get("y"):
                    raise ValueError("Dummy elem missing xy data")

                path.append([dummy_elem["x"], dummy_elem["y"]])

        if len(path) >= 2:
            direction1 = self._get_path_direction(path[0], path[1])
            direction2 = self._get_path_direction(path[-1], path[-2])

            offset_amount = self.diagram.icon_width / 2

            start_x, start_y = self._offset_coords(
                path[0], direction1, offset_amount=offset_amount
            )

            end_x, end_y = self._offset_coords(
                path[-1], direction2, offset_amount=offset_amount
            )

            path[0] = [start_x, start_y]
            path[-1] = [end_x, end_y]

        return path

    def _get_arrow_path(self, x, y, x_prev, y_prev, color: str, length: int):
        angle = math.atan2(y - y_prev, x - x_prev)

        # Convert to degrees
        angle_degrees = math.degrees(angle)

        # Shift the arrow slightly so path end isn't visible
        adjust_length = 2
        x_adjust = adjust_length * math.cos(angle)
        y_adjust = adjust_length * math.sin(angle)
        x += x_adjust
        y += y_adjust

        # Arrowhead path assuming the arrow points to the right (0 degrees)
        arrowhead_path = f"M {x} {y} l {-length} {-length / 2} l 0 {length} z"

        # Apply rotation
        transform = f"rotate({angle_degrees} {x} {y})"
        return f'<path d="{arrowhead_path}" transform="{transform}" fill="{color}" />'

    def _add_arrow_padding(self, path, start_padding, end_padding):
        if len(path) < 2:
            return path

        # Adjust the start of the path
        first_segment_vector = [path[1][0] - path[0][0], path[1][1] - path[0][1]]
        magnitude = (first_segment_vector[0] ** 2 + first_segment_vector[1] ** 2) ** 0.5
        if magnitude != 0:
            normalized_vector = [
                first_segment_vector[0] / magnitude,
                first_segment_vector[1] / magnitude,
            ]
            adjusted_startpoint = [
                path[0][0] + normalized_vector[0] * start_padding,
                path[0][1] + normalized_vector[1] * start_padding,
            ]
            path[0] = adjusted_startpoint

        # Adjust the end of the path
        last_segment_vector = [path[-1][0] - path[-2][0], path[-1][1] - path[-2][1]]
        magnitude = (last_segment_vector[0] ** 2 + last_segment_vector[1] ** 2) ** 0.5
        if magnitude != 0:
            normalized_vector = [
                last_segment_vector[0] / magnitude,
                last_segment_vector[1] / magnitude,
            ]
            adjusted_endpoint = [
                path[-1][0] - normalized_vector[0] * end_padding,
                path[-1][1] - normalized_vector[1] * end_padding,
            ]
            path[-1] = adjusted_endpoint

        return path

    def _coords_to_svg_path(self, coords):
        if not coords or len(coords) < 2:
            return ""

        # Start the path data string with the first coordinate
        path_data = f"M {coords[0][0]} {coords[0][1]}"

        # Add a curve to each subsequent coordinate
        for i in range(1, len(coords) - 1):
            mid_x = (coords[i][0] + coords[i + 1][0]) / 2
            mid_y = (coords[i][1] + coords[i + 1][1]) / 2
            path_data += f" Q {coords[i][0]} {coords[i][1]}, {mid_x} {mid_y}"

        # Line to the last coordinate
        path_data += f" L {coords[-1][0]} {coords[-1][1]}"

        return path_data
