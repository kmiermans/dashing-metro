import json
import os

_rel_path = os.path.join(os.path.dirname(__file__), '../config.json')

with open(_rel_path, 'r') as fp:
    d = json.load(fp)

dataSourcePath = d['dataSourcePath']
