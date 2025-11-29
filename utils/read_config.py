import json
import os

def read_testdata():
    # Path of this file (read_config.py)
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Go up one folder and then into testdata/credentials.json
    file_path = os.path.join(base_path, "..", "testdata", "credentials.json")

    # Normalize path (Windows friendly)
    file_path = os.path.abspath(file_path)

    # Read JSON file
    with open(file_path, "r") as file:
        return json.load(file)
