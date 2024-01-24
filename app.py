#!/usr/bin/env python3

import os
import sys

from aws_cdk import App

from draws import Diagrams
from infra.api_to_s3_stack import ApiToS3Stack
from infra.s3_bucket_stack import S3BucketStack

env = {
    "account": os.environ["CDK_DEFAULT_ACCOUNT"],
    "region": os.environ["CDK_DEFAULT_REGION"],
}


account_to_stage = {os.environ["DRAWS_DEV_ACCOUNT"]: "dev"}
try:
    stage_name = account_to_stage[os.environ.get("CDK_DEFAULT_ACCOUNT")]
except KeyError:
    print("Invalid account")
    sys.exit(1)

prefix = f"draws-{stage_name}"

app = App()

bucket_stack = S3BucketStack(app, f"{prefix}-bucket", public_prefix="public")
docs_ui_stack = ApiToS3Stack(app, f"{prefix}-docs-ui", bucket=bucket_stack.bucket)

Diagrams.of(app, directory="examples/output")

app.synth()
