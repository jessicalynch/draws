from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_apigatewayv2 as apigatewayv2
from aws_cdk import aws_apigatewayv2_integrations as apigatewayv2_integrations
from aws_cdk import aws_s3 as s3
from constructs import Construct


class ApiToS3Stack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        bucket: s3.IBucket = None,
        bucket_prefix: str = "",
        **kwargs,
    ):
        super().__init__(scope, id, **kwargs)

        http_api = apigatewayv2.HttpApi(self, "HttpApi", create_default_stage=True)

        s3_integration = apigatewayv2_integrations.HttpUrlIntegration(
            "S3Integration",
            f"https://{bucket.bucket_regional_domain_name}/{bucket_prefix}",
        )

        http_api.add_routes(
            path="/{proxy+}",
            methods=[apigatewayv2.HttpMethod.GET],
            integration=s3_integration,
        )

        self.url = http_api.api_endpoint
        CfnOutput(self, "ApiUrlOutput", description="HTTP API URL", value=self.url)
