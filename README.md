# draws: lightweight AWS Diagram Automation

**draws** is a dependency-free tool for automating AWS architecture diagram creation.

![AppSync GraphQL example AWS architecture diagram](./examples/diagrams/AppSyncGraphQLDynamoDBExample.template.svg)

![S3 Trigger example AWS architecture diagram](./examples/diagrams/s3Trigger.template.svg)

## Install

```bash
pip install draws
```

## Example Usage (from template)

```python
import os
from pathlib import Path

from draws import Diagram


if __name__ == "__main__":
    curr_dir = Path(os.path.abspath(os.path.dirname(__file__)))
    templates_dir = curr_dir / "cdk.out"

    D = Diagram.from_template(
        filename=templates_dir / "my-stack.template.json",
        title="My AWS Stack",
    )

    D.to_svg()
```

## Example Usage (manual)

```python
import os
from pathlib import Path

from draws import Diagram, Elem


if __name__ == "__main__":
    with Diagram(title="My AWS Stack") as D:
        rest_api = Elem("AWS::ApiGateway::RestApi", "Rest API")
        lambda_func = Elem("AWS::Lambda::Function", "Lambda")
        bucket = Elem("AWS::S3::Bucket", "Bucket")

        rest_api >> lambda_func
        rest_api << lambda_func
        lambda_func >> bucket

        D.to_svg()
```

<img src="./examples/diagrams/manual.svg" width="400">
