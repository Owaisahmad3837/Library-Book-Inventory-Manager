import json
from pathlib import Path


data_path = Path(__file__).parent.parent / "Data" / "Library_data.json"


def save_data(library_data):

    data_path.parent.mkdir(parents=True, exist_ok=True)

    with data_path.open("w", encoding="utf-8") as file:
        json.dump(library_data, file, indent=4)


def read_data():

    if not data_path.exists():
        return {}

    try:
        with data_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning Library data is invalid.")
        return {}