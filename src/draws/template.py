import json
import re
from pathlib import Path
from typing import Any, Dict, List, Union


class Template:
    def __init__(self, template_source: Union[Dict[str, Any], str, Path]):
        if isinstance(template_source, dict):
            self.template = template_source
        elif isinstance(template_source, (str, Path)):
            with open(template_source, "r") as file:
                self.template = json.load(file)
        else:
            raise TypeError("template_source must be a dictionary or a file path")

        self._resources = None
        self._dependencies = None

    @property
    def resources(self) -> Dict[str, Any]:
        if self._resources is None:
            self._resources = self.template.get("Resources", {})
        return self._resources

    @property
    def dependencies(self) -> Dict[str, Dict[str, Any]]:
        if self._dependencies is None:
            self._dependencies = self.find_dependencies()
        return self._dependencies

    def find_dependencies(self) -> Dict[str, Dict[str, Any]]:
        """Find dependencies between resources in the CloudFormation template.

        Returns:
            Dependency graph.
        """
        graph = {}
        for resource_id, resource_details in self.resources.items():
            resource_type = resource_details.get("Type")
            dependencies = set()

            if "DependsOn" in resource_details:
                dep = resource_details["DependsOn"]
                if isinstance(dep, list):
                    dependencies.update(dep)
                else:
                    dependencies.add(dep)

            properties = resource_details.get("Properties", {})
            implicit_deps = self.find_references(properties)
            dependencies.update(implicit_deps)

            graph[resource_id] = {
                "type": resource_type,
                "dependencies": list(dependencies),
            }

        return graph

    def find_references(self, value: Any) -> List[str]:
        """Recursively searches for references to resources in a given value.

        Args:
            value: A value from a CloudFormation template which could be a dict, list,
                   or other types. The function will search references in this value.

        Returns:
            A list of resource identifiers that are referenced within the value.
        """
        references = []
        if isinstance(value, dict):
            for key, val in value.items():
                if key == "Ref" and val in self.resources:
                    references.append(val)
                elif key == "Fn::GetAtt":
                    ref = val[0]
                    if ref in self.resources:
                        references.append(ref)
                elif key == "Fn::Sub":
                    extracted_refs = self.parse_fn_sub(val)
                    references.extend(extracted_refs)
                else:
                    references.extend(self.find_references(val))
        elif isinstance(value, list):
            for item in value:
                references.extend(self.find_references(item))
        return references

    def parse_fn_sub(self, fn_sub_expression: Union[str, List[str]]) -> List[str]:
        """Extracts resource references from Fn::Sub expression.

        Args:
            fn_sub_expression: The value of Fn::Sub.

        Returns:
            A list of resource identifiers referenced within the 'Fn::Sub' expression.
        """
        extracted_refs = []

        if isinstance(fn_sub_expression, list):
            sub_string, sub_vars = fn_sub_expression
        else:
            sub_string = fn_sub_expression
            sub_vars = {}

        placeholders = re.findall(r"\${([A-Za-z0-9_-]+)}", sub_string)
        for placeholder in placeholders:
            if placeholder not in sub_vars and placeholder in self.resources:
                extracted_refs.append(placeholder)

        return extracted_refs
