import pytest

from draws import Diagram, Elem
from draws.graph import Graph


@pytest.fixture
def mock_diagram():
    return Diagram(title="Test Diagram")


@pytest.fixture
def mock_elem():
    return Elem(resource_type="AWS::S3::Bucket", label="MyBucket")


@pytest.fixture
def mock_edges():
    return [(1, 2), (2, 3), (3, 4)]


@pytest.fixture
def mock_graph(mock_edges):
    return Graph.from_edges(mock_edges)
