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
        lambda_node = Elem("AWS::Lambda::Function", "Lambda1")
        s3_node = Elem("AWS::S3::Bucket", "Bucket1")
        ec2_node = Elem("AWS::EC2::Instance", "EC2 Instance")

        lambda_node >> s3_node
        lambda_node << s3_node
        ec2_node >> s3_node
        s3_node >> ec2_node

        D.to_svg(filename=curr_dir / "diagrams" / "manual.svg")


if __name__ == "__main__":
    build_from_templates()
    build_manually()
