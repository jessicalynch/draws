import os
from pathlib import Path

from draws import Diagram, Elem

curr_dir = Path(os.path.abspath(os.path.dirname(__file__)))


def build_from_templates():
    template_dir_name = "templates"
    templates_dir = curr_dir / template_dir_name

    if templates_dir.is_dir():
        for file in templates_dir.iterdir():
            if file.is_file() and file.suffix == ".json":
                title = file.stem.replace("_", " ").replace(".template", "").title()

                D = Diagram.from_template(
                    filename=file,
                    title=title,
                )
                D.to_svg(
                    filename=curr_dir / "diagrams" / f"{file.stem}.svg",
                )
                print(f"Diagram generated for {file}")
    else:
        print(f"No '{template_dir_name}' directory found in {curr_dir}")


def build_manually():
    with Diagram(title="My AWS Stack") as D:
        rest_api = Elem("AWS::ApiGateway::RestApi", "Rest API")
        lambda_func = Elem("AWS::Lambda::Function", "Lambda")
        bucket = Elem("AWS::S3::Bucket", "Bucket")

        rest_api >> lambda_func
        rest_api << lambda_func
        lambda_func >> bucket

        D.to_svg()

        D.to_svg(filename=curr_dir / "diagrams" / "manual.svg")


if __name__ == "__main__":
    build_from_templates()
    build_manually()
