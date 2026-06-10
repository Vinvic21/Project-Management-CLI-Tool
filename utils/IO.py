import json
import os

DATA_FILES = "data"

def load_json(filename):
    path = os.path.join(DATA_FILES, filename)
    if not os.path.exists(path):
        return[]
    with open(path, "r") as file:
        try:
            return json.load(file)
        except ValueError:
            return[]

def save_data(filename, data):
    path = os.path.join(DATA_FILES, filename)
    with open(path, "w") as file:
        return json.dump(data, file)