import json
import os
import pandas as pd

_rel_path = os.path.join(os.path.dirname(__file__), '../config.json')

with open(_rel_path, 'r') as fp:
    d = json.load(fp)

dataSourcePath = d['dataSourcePath']

df = pd.read_csv(dataSourcePath)

transport_labels = df['label'].unique()

transport_types = df['product'].unique()

