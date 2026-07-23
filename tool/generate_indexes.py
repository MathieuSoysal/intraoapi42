import yaml
import os
from pathlib import Path

index_file_name = "_index.yaml"
directories = ["paths", "schemas", "parameters"]

def normalize_object_ref(ref: str) -> str:
    """
    Normalize the second part of a $ref string
    Eg: "/languages/{id}" -> "~1languages~1{id}"
    https://swagger.io/docs/specification/v3_0/using-ref/#escape-characters
    """
    return ref.replace("~", "~0").replace("/", "~1")

def generate_index_file(directory: Path):
    index_file_path = directory / index_file_name
    index_data = {}

    for file in directory.glob("*.yaml"):
        if file.name == index_file_name:
            continue

        with open(file, "r") as f:
            data = yaml.safe_load(f)

        for top_level_key in data.keys():
            ref_path = f"./{file.name}"
            normalized_top_level_key = normalize_object_ref(top_level_key)
            index_data[top_level_key] = {"$ref": f"{ref_path}#/{normalized_top_level_key}"}

    with open(index_file_path, "w") as f:
        yaml.dump(index_data, f, default_flow_style=False)

def main():
    cwd = os.getcwd()
    base_path = Path(cwd) / "specs"
    for directory_name in directories:
        directory_path = base_path / directory_name
        generate_index_file(directory_path)

if __name__ == "__main__":
    main()