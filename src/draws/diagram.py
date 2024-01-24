from __future__ import annotations

import importlib
import os
import textwrap
import uuid
from pathlib import Path
from typing import Any, Dict, List, Literal, Tuple, Union

from .colors import color_mapping
from .graph import Graph
from .icons import icon_mapping
from .renderer import DiagramRenderer
from .template import Template

DEFAULT_STROKE_COLOR = "#333"
STROKE_WIDTH = 2
ICON_SIZE = 64
TITLE_FONT_SIZE = 21
LABEL_FONT_SIZE = 13
DEFAULT_DIAGRAM_PADDING = ICON_SIZE // 3 * 2
TITLE_MARGIN = ICON_SIZE
LABEL_MARGIN = 4
ARROW_LENGTH = 15
ARROW_PADDING = ARROW_LENGTH * 1.2
DEFAULT_VERTICAL_SPACING: int = (ICON_SIZE + LABEL_MARGIN) * 3
DEFAULT_HORIZONTAL_SPACING = ICON_SIZE * 3.5
SVG_DEFS_PATH = "assets/svg_defs"
DEFAULT_ICON_FILE = "Arch_AWS-Cloud-Development-Kit_64.svg"
LabelSource = Literal["id", "type"]
current_diagram = None


def set_current_diagram(diagram) -> Diagram:
    global current_diagram
    current_diagram = diagram


def get_current_diagram() -> Diagram:
    return current_diagram


class Elem:
    _counter = 0

    def __init__(self, resource_type: str, label: str = None):
        self.resource_type = resource_type
        self.label = label or resource_type
        self.id = f"elem_{Elem._counter}_{uuid.uuid4().hex[:6]}"
        Elem._counter += 1
        self.x = 0
        self.y = 0
        self.connections = []
        self.icon = self._get_icon(resource_type)
        self.color = self._get_color(resource_type)
        self.diagram = get_current_diagram()
        if self.diagram is not None:
            self.diagram.add_elem(self)

    @property
    def position(self) -> Tuple(int, int):
        return (self.x, self.y)

    @property
    def label_width(self):
        """Calculate width of the label without wrapping."""
        return len(self.label) * self._get_estimated_char_width()

    @property
    def wrapped_label_lines(self) -> List[str]:
        return textwrap.wrap(self.label, self._calculate_max_label_width())

    @property
    def wrapped_label_width(self):
        """Calculate width of the label with wrapping."""
        max_line_width = (
            max(len(line) for line in self.wrapped_label_lines)
            if self.wrapped_label_lines
            else 0
        )
        return max_line_width * self._get_estimated_char_width()

    @property
    def wrapped_label(self):
        """Wrap the label text based on maximum width."""
        return "\n".join(self.wrapped_label_lines)

    @property
    def total_width(self) -> int:
        return self.diagram.icon_width + self.wrapped_label_width

    @property
    def total_height(self) -> int:
        return (
            self.diagram.icon_height
            + (len(self.wrapped_label_lines) * self.diagram.label_font_size)
            + self.diagram.label_margin
        )

    def connect(self, other: "Elem"):
        if isinstance(other, list):
            # TODO: support lists
            raise ValueError("Elem must connet to another Elem")
        else:
            if other not in self.connections:
                self.connections.append(other)
                if self.diagram is not None:
                    self.diagram.graph.add_edge(u=self.id, v=other.id)

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y

    def _get_icon(self, resource_type: str) -> str:
        resource_type = resource_type.split("::")
        icon_filename = icon_mapping.get("-".join(resource_type))
        if not icon_filename:
            icon_filename = icon_mapping.get("-".join(resource_type[:-1]))

        if not icon_filename:
            icon_filename = DEFAULT_ICON_FILE

        return icon_filename

    def _get_color(self, resource_type):
        resource_type_parts = resource_type.split("::")
        return color_mapping.get(
            "-".join(resource_type_parts[:2]), DEFAULT_STROKE_COLOR
        )

    def _get_estimated_char_width(self) -> int:
        return self.diagram.label_font_size * 0.6

    def _calculate_max_label_width(self):
        """Calculate the maximum width of a label."""
        max_label_width = self.diagram.icon_width + self.diagram.horizontal_spacing // 2
        return int(max_label_width // self._get_estimated_char_width())

    def __rshift__(self, other: Elem):
        self.connect(other)
        return other

    def __lshift__(self, other: Elem):
        other.connect(self)
        return other

    def __str__(self) -> str:
        """String representation of the Elem."""
        return f"Elem({self.id})"

    def __repr__(self):
        return self.__str__()


class Diagram:
    def __init__(
        self,
        title: str = "",
    ):
        self.title = title
        self.title_font_size: int = TITLE_FONT_SIZE
        self.title_margin: int = TITLE_MARGIN
        self.padding: int = DEFAULT_DIAGRAM_PADDING
        self.vertical_spacing: int = DEFAULT_VERTICAL_SPACING
        self.horizontal_spacing: int = DEFAULT_HORIZONTAL_SPACING
        self.arrow_length: int = ARROW_LENGTH
        self.arrow_padding: int = ARROW_PADDING
        self.icon_width: int = ICON_SIZE
        self.icon_height: int = ICON_SIZE
        self.label_margin: int = LABEL_MARGIN
        self.label_font_size: int = LABEL_FONT_SIZE
        self.label_margin: int = LABEL_MARGIN
        self.stroke_width: int = STROKE_WIDTH

        self.graph: Graph = Graph()
        self.elems: List[Elem] = []

        self.id = f"diagram_{uuid.uuid4().hex[:6]}"

    def __enter__(self):
        set_current_diagram(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        set_current_diagram(None)

    def to_svg(self, filename: Union[str, Path] = None):
        renderer = DiagramRenderer(self)
        renderer.render(filename=filename)
        print(f"Diagram saved to: {filename}")

    def add_elem(self, elem: Elem):
        self.elems.append(elem)
        self.graph.add_vertex(elem.id)
        connected_elem_ids = [conn.id for conn in elem.connections]

        for connected_elem_id in connected_elem_ids:
            self.graph.add_edge(elem.id, connected_elem_id)

    @classmethod
    def _auto_generate(
        cls, diagram: Diagram, template: Template, label_source: LabelSource
    ):
        with diagram:
            elems = {}
            # Add elements
            for resource_id, details in template.dependencies.items():
                resource_type = details["type"]
                label = resource_id if label_source == "id" else resource_type
                elem = Elem(resource_type, label)
                elems[resource_id] = elem
                diagram.add_elem(elem)

            # Add connections
            for resource_id, details in template.dependencies.items():
                for dep in details["dependencies"]:
                    if dep in elems and resource_id in elems:
                        elems[dep] >> elems[resource_id]

    @classmethod
    def from_template(
        cls,
        src: Union[Dict[str, Any], str, Path],
        title: str = "",
        label_source: LabelSource = "id",
    ) -> "Diagram":
        template = Template(template_source=src)
        diagram = cls(title=title)
        cls._auto_generate(
            diagram=diagram, template=template, label_source=label_source
        )

        return diagram


class Diagrams:
    @staticmethod
    def of(app, directory: str = ""):
        try:
            importlib.import_module("aws_cdk")
        except ImportError:
            try:
                importlib.import_module("aws_cdk.core")
            except ImportError:
                raise ImportError("AWS CDK is not installed.")

        if not hasattr(app, "synth") or not hasattr(app, "node"):
            raise AttributeError(
                "The provided app does not have the required methods ('synth', 'node')."
            )

        cloud_assembly = app.synth()
        for stack_artifact in cloud_assembly.stacks:
            template_dict = stack_artifact.template
            D = Diagram.from_template(src=template_dict)
            svg_filename = os.path.join(
                directory, f"{stack_artifact.stack_name}.diagram.svg"
            )
            D.to_svg(filename=svg_filename)
