from pathlib import Path

import pytest

from draws.template import Template


def test_init_with_dict(mock_template_dict: dict):
    template = Template(mock_template_dict)
    assert template.template == mock_template_dict


def test_init_with_file(mock_template_file: Path, mock_template_dict: dict):
    template = Template(mock_template_file)
    assert template.template == mock_template_dict


def test_invalid_init():
    with pytest.raises(TypeError):
        Template(123)


def test_resources_property(mock_template_dict: dict):
    template = Template(mock_template_dict)
    assert template.resources == mock_template_dict["Resources"]


def test_dependencies_property(mock_template_dict: dict):
    template = Template(mock_template_dict)
    dependencies = template.dependencies
    assert "MyLambda" in dependencies
    assert "MyBucket" in dependencies["MyLambda"]["dependencies"]


def test_find_references(mock_template_dict: dict):
    template = Template(mock_template_dict)
    references = template.find_references({"Fn::GetAtt": ["MyRole", "Arn"]})
    assert "MyRole" in references


def test_parse_fn_sub(mock_template_dict: dict):
    template = Template(mock_template_dict)
    references = template.parse_fn_sub(
        "arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:${MyLambda}"
    )
    assert "MyLambda" in references
