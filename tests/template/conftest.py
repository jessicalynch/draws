import json
from pathlib import Path

import pytest


@pytest.fixture
def mock_template_dict():
    return {
        "Resources": {
            "MyBucket": {
                "Type": "AWS::S3::Bucket",
                "Properties": {"BucketName": "my-bucket"},
            },
            "MyLambda": {
                "Type": "AWS::Lambda::Function",
                "DependsOn": "MyBucket",
                "Properties": {
                    "Handler": "index.handler",
                    "Role": {"Fn::GetAtt": ["MyRole", "Arn"]},
                },
            },
            "MyRole": {"Type": "AWS::IAM::Role"},
        }
    }


@pytest.fixture
def mock_template_file(mock_template_dict):
    temp_file = Path("temp_template.json")
    with open(temp_file, "w") as f:
        json.dump(mock_template_dict, f)
    yield temp_file
    temp_file.unlink()
