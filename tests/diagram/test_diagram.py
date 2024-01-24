from draws import Diagram, Elem


def test_add_elem_to_diagram(mock_diagram: Diagram, mock_elem: Elem):
    mock_diagram.add_elem(mock_elem)
    assert mock_elem in mock_diagram.elems


def test_elem_initialization(mock_elem: Elem):
    assert mock_elem.resource_type == "AWS::S3::Bucket"
    assert mock_elem.label == "MyBucket"
    assert mock_elem.id.startswith("elem_")
    assert mock_elem.x == 0
    assert mock_elem.y == 0


def test_connect_elements(mock_elem: Elem):
    other_elem = Elem(resource_type="AWS::Lambda::Function", label="MyLambda")
    mock_elem.connect(other_elem)
    assert other_elem in mock_elem.connections


def test_position_setting(mock_elem: Elem):
    mock_elem.set_position(10, 20)
    assert mock_elem.position == (10, 20)
