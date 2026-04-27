import os
import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def ensure_dirs():
    config = load_config()

    for path in config["folders"].values():
        os.makedirs(path, exist_ok=True)
