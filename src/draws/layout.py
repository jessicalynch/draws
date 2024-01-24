import itertools
import math
from abc import ABC, abstractmethod
from typing import List, Tuple

from .graph import Graph, Vertex, VertexId


class LayoutStrategy(ABC):
    @abstractmethod
    def get_layers(self, graph):
        pass


class Layout:
    def __init__(self, graph: Graph, strategy: LayoutStrategy):
        self.graph = graph
        self.strategy = strategy
        self._layers = None

    @property
    def layers(self):
        if self._layers is None:
            self._layers = self.strategy.get_layers(self.graph)
        return self._layers


class SugiyamaStrategy(LayoutStrategy):
    def get_acyclic_sequence(self, graph: Graph) -> List:
        """Generates an ordering of vertices.

        Args:
            graph (Graph): The graph to analyze.

        Returns:
            List: Ordered vertices that facilitate acyclic representation.
        """

        g = graph.copy()
        source_order, sink_order = (
            [],
            [],
        )  # Track order of removed source and sink vertices

        while g.vertices:
            # Remove source vertices (vertices with no incoming edges)
            sources = [
                vertex for vertex in g.vertices if not g.vertices[vertex].in_vertex_ids
            ]
            if sources:
                source_order.extend(sources)
                for vertex in sources:
                    g.remove_vertex(vertex)

            # Remove sink vertices (vertices with no outgoing edges)
            sinks = [
                vertex for vertex in g.vertices if not g.vertices[vertex].out_vertex_ids
            ]
            if sinks:
                sink_order.extend(sinks)
                for vertex in sinks:
                    g.remove_vertex(vertex)

            # For remaining vertices, remove based on out-degree minus in-degree
            elif g.vertices:
                vertex_to_remove = max(
                    g.vertices,
                    key=lambda vertex: len(g.vertices[vertex].out_vertex_ids)
                    - len(g.vertices[vertex].in_vertex_ids),
                )
                source_order.append(vertex_to_remove)
                g.remove_vertex(vertex_to_remove)

        return source_order + sink_order

    def invert_cross_edges(self, graph: Graph, sequence: List[VertexId]) -> Graph:
        """Inverts the direction of cross edges in a graph.

        Args:
            graph (Graph): The graph on which to invert cross edges.
            sequence (List[VertexId]): The sequence used to determine cross edges.

        Returns:
            Graph: A new graph with the cross edges inverted.
        """
        g = graph.copy()
        cross_edges_to_invert = []

        for index, vertex in enumerate(sequence):
            for child_vertex in g.vertices[vertex].out_vertex_ids:
                if sequence.index(child_vertex) < index:
                    cross_edges_to_invert.append((vertex, child_vertex))

        g.invert_edges(cross_edges_to_invert)
        return g

    def assign_initial_layers(self, graph: Graph) -> List[List[VertexId]]:
        """Assigns vertices to initial layers in a graph.

        Args:
            graph (Graph): The graph to process.

        Returns:
            List[List[VertexId]]: The initial layers with vertices assigned.
        """
        g = graph.copy()
        layers = []

        while g.vertices:
            sinks = [
                vertex for vertex in g.vertices if not g.vertices[vertex].out_vertex_ids
            ]
            layers.append(sinks)
            for vertex in sinks:
                g.remove_vertex(vertex)

        return list(reversed(layers))

    def add_edge_dummy_vertices(
        self,
        graph: Graph,
        edge: Tuple[VertexId, VertexId],
        layers: List[List[VertexId]],
    ) -> Tuple[Graph, List[List[VertexId]]]:
        """
        Adds intermediate vertices between two layers of a graph.

        Args:
            graph: The graph on which to operate.
            edge: The edge between two vertices
                  where intermediate vertices might be needed.
            layers: The hierarchical layers of vertices
                    in the graph.

        Returns:
            The updated graph and layers with intermediate vertices added.
        """

        source_vertex, target_vertex = edge
        source_layer = graph.vertices[source_vertex].data["layer"]
        target_layer = graph.vertices[target_vertex].data["layer"]
        layer_step = -1 if target_layer < source_layer else 1

        # Remove the direct edge to be replaced by intermediate vertices
        graph.remove_edge(source_vertex, target_vertex)

        current_vertex = source_vertex
        dummy_counter = 0
        for layer in range(source_layer + layer_step, target_layer, layer_step):
            # Create a unique ID for the intermediate vertex
            intermediate_vertex_id = (
                f"dummy_{source_vertex}_{target_vertex}_{dummy_counter}"
            )
            dummy_counter += 1
            graph.add_edge(current_vertex, intermediate_vertex_id)
            graph.vertices[intermediate_vertex_id] = Vertex(
                vertex_id=intermediate_vertex_id,
                in_vertex_ids=[current_vertex],
                out_vertex_ids=[],
                data={"layer": layer},
            )
            layers[layer].append(intermediate_vertex_id)
            current_vertex = intermediate_vertex_id

        # Connect the last intermediate vertex to the target vertex
        graph.add_edge(current_vertex, target_vertex)
        return graph, layers

    def add_dummy_vertices(
        self, graph: Graph, layers: List[List[VertexId]]
    ) -> Tuple[Graph, List[List[VertexId]]]:
        """Adds intermediate vertices between non-adjacent layers of a graph.

        Args:
            graph: The graph to process.
            layers: Hierarchical layers of vertices in the graph.

        Returns:
            The updated graph and layers with intermediate vertices added.
        """
        g = graph.copy()

        for i, layer in enumerate(layers):
            for vertex in layer:
                g.vertices[vertex].data["layer"] = i

        for i, layer in enumerate(layers):
            for vertex in layer:
                for child in g.vertices[vertex].out_vertex_ids:
                    child_layer = g.vertices[child].data["layer"]
                    if math.fabs(child_layer - i) > 1:
                        g, layers = self.add_edge_dummy_vertices(
                            graph=g, edge=(vertex, child), layers=layers
                        )

        return g, layers

    def get_cost_matrix(
        self,
        graph: Graph,
        layer1_vertices: List[VertexId],
        layer2_vertices: List[VertexId],
    ) -> List[List[int]]:
        """Generates a cost matrix for edge crossings.

        Args:
            graph: The graph being processed.
            layer1_vertices: List of vertex IDs in the first layer.
            layer2_vertices: List of vertex IDs in the second layer.

        Returns:
            A matrix where each cell (i, j) represents the number
            of crossings between vertex i of layer1 and vertex j of layer2.
        """

        # Initialize the cost matrix with zeros
        cost_matrix = [[0 for _ in layer1_vertices] for _ in layer1_vertices]

        # Map each vertex in layer2 to its index for quick lookup
        layer2_indices = {
            vertex_id: idx for idx, vertex_id in enumerate(layer2_vertices)
        }

        # Iterate through all combinations of two vertices in layer1
        for (index1, vertex1), (index2, vertex2) in itertools.combinations(
            enumerate(layer1_vertices), 2
        ):
            # Get indices of layer2 vertices connected to vertex1
            edges_vertex1 = [
                layer2_indices[edge]
                for edge in graph.vertices[vertex1].out_vertex_ids
                + graph.vertices[vertex1].in_vertex_ids
                if edge in layer2_indices
            ]

            # Get indices of layer2 vertices connected to vertex2
            edges_vertex2 = [
                layer2_indices[edge]
                for edge in graph.vertices[vertex2].out_vertex_ids
                + graph.vertices[vertex2].in_vertex_ids
                if edge in layer2_indices
            ]

            # Calculate crossings between edges of vertex1 and vertex2
            for edge1, edge2 in itertools.product(edges_vertex1, edges_vertex2):
                # Increment the cost if there's a crossing
                if edge1 > edge2:
                    cost_matrix[index1][index2] += 1
                elif edge1 < edge2:
                    cost_matrix[index2][index1] += 1

        return cost_matrix

    def minimize_crossings(
        self, graph: Graph, layers: List[List[VertexId]]
    ) -> List[List[VertexId]]:
        """Minimizes edge crossings between layers in a graph.

        Args:
            graph: The graph being drawn.
            layers: The vertices in each layer of the graph.

        Returns:
            A new list of layers with vertices sorted
                                to minimize crossings.
        """
        if not layers:
            raise ValueError("Layers list is empty")

        processed_layers = [layers[-1]]

        for current_layer_index in reversed(range(len(layers) - 1)):
            current_layer = layers[current_layer_index]
            next_layer = processed_layers[-1]
            cost_matrix = self.get_cost_matrix(graph, current_layer, next_layer)
            sorted_indices = self.sort_by_cost(range(len(current_layer)), cost_matrix)
            sorted_layer = [current_layer[i] for i in sorted_indices]
            processed_layers.append(sorted_layer)

        return list(reversed(processed_layers))

    def sort_by_cost(
        self, vertices: List[VertexId], cost_matrix: List[List[int]]
    ) -> List[VertexId]:
        """Sorts vertices to minimize edge crossings based on a cost matrix.

        Args:
            vertices: The list of vertices to sort.
            cost_matrix: The cost matrix representing edge crossings.

        Returns:
            Sorted vertices.
        """
        if len(vertices) < 2:
            return vertices

        mid_point = len(vertices) // 2
        left_sorted = self.sort_by_cost(vertices[:mid_point], cost_matrix)
        right_sorted = self.sort_by_cost(vertices[mid_point:], cost_matrix)
        sorted_vertices = []

        left_index, right_index = 0, 0
        while left_index < len(left_sorted) and right_index < len(right_sorted):
            if (
                cost_matrix[left_sorted[left_index]][right_sorted[right_index]]
                <= cost_matrix[right_sorted[right_index]][left_sorted[left_index]]
            ):
                sorted_vertices.append(left_sorted[left_index])
                left_index += 1
            else:
                sorted_vertices.append(right_sorted[right_index])
                right_index += 1

        sorted_vertices.extend(left_sorted[left_index:])
        sorted_vertices.extend(right_sorted[right_index:])
        return sorted_vertices

    def get_layers(self, graph: Graph) -> List[List[VertexId]]:
        g = graph.copy()
        sequence = self.get_acyclic_sequence(graph=g)
        g = self.invert_cross_edges(graph=g, sequence=sequence)
        layers = self.assign_initial_layers(g)
        g, layers = self.add_dummy_vertices(graph=g, layers=layers)
        layers = self.minimize_crossings(graph=g, layers=layers)
        return layers
