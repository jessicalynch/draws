from typing import List
from draws.graph import Graph, GraphEdge


def test_add_vertex():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex("1")
    assert 1 in graph.vertices
    assert graph.vertices[1].vertex_id == 1
    assert graph.vertices["1"].vertex_id == "1"


def test_add_edge_creates_vertices():
    graph = Graph()
    graph.add_edge(1, 2)
    assert 1 in graph.vertices and 2 in graph.vertices
    assert 2 in graph.vertices[1].out_vertex_ids
    assert 1 in graph.vertices[2].in_vertex_ids


def test_remove_vertex():
    graph = Graph()
    graph.add_vertex(1)
    graph.remove_vertex(1)
    assert 1 not in graph.vertices


def test_remove_edge():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.remove_edge(1, 2)
    assert 2 not in graph.vertices[1].out_vertex_ids


def test_mock_graph(mock_graph: Graph, mock_edges: List[GraphEdge]):
    for u, v in mock_edges:
        assert v in mock_graph.vertices[u].out_vertex_ids
        assert u in mock_graph.vertices[v].in_vertex_ids


def test_copy_graph(mock_graph: Graph):
    copy_graph = mock_graph.copy()
    for vertex_id, vertex in copy_graph.vertices.items():
        original_vertex = mock_graph.vertices[vertex_id]
        assert vertex.vertex_id == original_vertex.vertex_id
        assert vertex.in_vertex_ids == original_vertex.in_vertex_ids
        assert vertex.out_vertex_ids == original_vertex.out_vertex_ids
        assert vertex.data == original_vertex.data


def test_invert_edges(mock_graph: Graph, mock_edges: List[GraphEdge]):
    inverted_edges = mock_graph.invert_edges(mock_edges)
    for u, v in inverted_edges:
        assert v in mock_graph.vertices[u].out_vertex_ids
        assert u in mock_graph.vertices[v].in_vertex_ids


def test_remove_edges(mock_graph: Graph, mock_edges: List[GraphEdge]):
    mock_graph.remove_edges(mock_edges)
    for u, v in mock_edges:
        assert v not in mock_graph.vertices[u].out_vertex_ids
