import pytest

from draws import Diagram, Elem


@pytest.fixture
def mock_diagram():
    return Diagram(title="Test Diagram")


@pytest.fixture
def mock_elem():
    return Elem(resource_type="AWS::S3::Bucket", label="MyBucket")
