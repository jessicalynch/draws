from typing import Optional

from aws_cdk import CfnOutput, RemovalPolicy, Stack
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from constructs import Construct


class S3BucketStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        bucket_props: Optional[s3.BucketProps] = None,
        public_prefix: Optional[str] = "",
        **kwargs,
    ):
        super().__init__(scope, id, **kwargs)

        default_bucket_props = s3.BucketProps(
            cors=[
                s3.CorsRule(
                    allowed_headers=["*"],
                    allowed_methods=[s3.HttpMethods.GET, s3.HttpMethods.HEAD],
                    allowed_origins=["*"],
                    max_age=3000,
                )
            ],
            block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        final_bucket_props = default_bucket_props
        if bucket_props is not None:
            final_bucket_props = s3.BucketProps(
                **{**default_bucket_props._values, **bucket_props._values}
            )
        public_prefix = public_prefix.strip("/")

        bucket = s3.Bucket(self, "Bucket", **final_bucket_props._values)

        self.bucket = bucket

        if public_prefix:
            bucket.add_to_resource_policy(
                iam.PolicyStatement(
                    actions=["s3:GetObject"],
                    resources=[f"{bucket.bucket_arn}/{public_prefix}/*"],
                    principals=[iam.AnyPrincipal()],
                )
            )
            self.public_url = f"{bucket.bucket_website_url}/{public_prefix}"

            CfnOutput(self, "S3BucketPublicUrlOutput", value=self.public_url)

        CfnOutput(self, "S3BucketUrlOutput", value=bucket.bucket_website_url)
