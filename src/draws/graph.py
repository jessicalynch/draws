from typing import Dict, List, Tuple, Union

VertexId = Union[int, str]
GraphEdge = Tuple[VertexId, VertexId]


class Vertex:
    def __init__(
        self,
        vertex_id: VertexId,
        in_vertex_ids: List[VertexId] = None,
        out_vertex_ids: List[VertexId] = None,
        data: dict = None,
    ):
        self.vertex_id: VertexId = vertex_id
        self.in_vertex_ids = in_vertex_ids if in_vertex_ids is not None else []
        self.out_vertex_ids = out_vertex_ids if out_vertex_ids is not None else []
        self.data = data if data is not None else {}


class Graph:
    def __init__(self):
        self.vertices: Dict[VertexId, Vertex] = {}

    @classmethod
    def from_edges(cls, edges: List[GraphEdge]) -> "Graph":
        """Create a Graph from a list of edges."""

        graph = cls()
        for u, v in edges:
            graph.add_edge(u, v)
        return graph

    def add_vertex(self, vertex_id: VertexId):
        """Add a vertex to the graph."""

        if not self.vertices.get(vertex_id):
            self.vertices[vertex_id] = Vertex(vertex_id=vertex_id)

    def add_edge(self, u: VertexId, v: VertexId):
        """Add an edge to the graph."""

        if not self.vertices.get(u):
            self.add_vertex(u)
        if not self.vertices.get(v):
            self.add_vertex(v)
        self.vertices[u].out_vertex_ids.append(v)
        self.vertices[v].in_vertex_ids.append(u)

    def remove_edge(self, u: VertexId, v: VertexId):
        """Remove an edge from the graph."""

        if u in self.vertices and v in self.vertices[u].out_vertex_ids:
            self.vertices[u].out_vertex_ids.remove(v)
        if v in self.vertices and u in self.vertices[v].in_vertex_ids:
            self.vertices[v].in_vertex_ids.remove(u)

    def remove_vertex(self, vertex_id: VertexId):
        """Remove a vertex and its associated edges from the graph."""

        if vertex_id not in self.vertices:
            return

        for in_vertex in self.vertices[vertex_id].in_vertex_ids:
            if in_vertex in self.vertices:
                self.vertices[in_vertex].out_vertex_ids.remove(vertex_id)

        for out_vertex in self.vertices[vertex_id].out_vertex_ids:
            if out_vertex in self.vertices:
                self.vertices[out_vertex].in_vertex_ids.remove(vertex_id)

        del self.vertices[vertex_id]

    def invert_edges(self, edges: List[GraphEdge]) -> List[GraphEdge]:
        """Invert the direction of given edges."""

        self.remove_edges(edges)
        inv_edges = [(v, u) for u, v in edges]
        for u, v in inv_edges:
            self.add_edge(u, v)
        return inv_edges

    def remove_edges(self, edges: List[GraphEdge]):
        """Remove multiple edges."""

        for u, v in edges:
            self.remove_edge(u, v)

    def copy(self) -> "Graph":
        """Create a deep copy of the graph."""

        cloned_graph = Graph()
        for vertex_id, vertex in self.vertices.items():
            cloned_graph.vertices[vertex_id] = Vertex(
                vertex_id=vertex_id,
                in_vertex_ids=list(vertex.in_vertex_ids),
                out_vertex_ids=list(vertex.out_vertex_ids),
                data=dict(vertex.data),
            )
        return cloned_graph

    def __str__(self) -> str:
        """String representation of the graph."""

        vertices_str = "Vertices: " + ", ".join(map(str, self.vertices.keys()))
        edges_str = "Edges: "
        edge_list = []
        connections = []

        for vertex_id, vertex in self.vertices.items():
            connections.append(f"{vertex_id}")
            connections.append("\tOut:")
            for out_vertex_id in vertex.out_vertex_ids:
                connections.append(f"\t\t{out_vertex_id}")
                edge_list.append(f"({vertex_id}, {out_vertex_id})")
            connections.append("\tIn:")
            for in_vertext_id in vertex.in_vertex_ids:
                connections.append(f"\t\t{in_vertext_id}")

        edges_str += ", ".join(edge_list)
        connections_str = "\n".join(connections)

        ret_str = vertices_str + "\n" + edges_str + "\n" + connections_str
        return ret_str
