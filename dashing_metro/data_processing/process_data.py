from dashing_metro.backend.imports import *
import dashing_metro as dm
from dashing_metro.backend.module_data import internals


def add_geographical_coordinates_to_df(df_depts: pd.DataFrame, df_stations: pd.DataFrame):
    return df_depts.join(df_stations, on=internals.col_names.station_id)
