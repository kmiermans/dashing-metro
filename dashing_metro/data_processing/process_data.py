from dashing_metro.backend.imports import *
import dashing_metro as dm

df = pd.read_csv(dm.variables.dataSourcePath)
print(df)