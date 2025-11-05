import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "consts.json"), "r") as f:
    CONSTS = json.load(f)
