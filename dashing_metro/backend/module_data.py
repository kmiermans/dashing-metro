from dashing_metro.backend.imports import *
from dashing_metro.backend.util import _immutable_object_


_rel_path_ = os.path.join(os.path.dirname(__file__), '../config.json')
with open(_rel_path_, 'r') as fp:
    _json_d_ = json.load(fp)


class __data_paths(_immutable_object_):
    depts = _json_d_['data_loc']['departures']
    stations = _json_d_['data_loc']['stations']
_data_paths_ = __data_paths()


_df_depts_ = pd.read_csv(_data_paths_.depts)
_df_stations_ = pd.read_csv(_data_paths_.stations)


class __col_names(_immutable_object_):
    _sub_dict_ = _json_d_['col_names']
    station_id = _sub_dict_['station_id']
    dep_id = _sub_dict_['dep_id']
    line_label = _sub_dict_['line_label']
    transport_type = _sub_dict_['transport_type']
_col_names_ = __col_names()



class __cat_data_vals(_immutable_object_):
    line_labels = _df_depts_[_col_names_.line_label].unique()
    transport_types = _df_depts_[_col_names_.transport_type].unique()
    station_ids = _df_depts_[_col_names_.station_id].unique()
_cat_data_vals_ = __cat_data_vals()


def add_geographical_coordinates_to_df(df_depts: pd.DataFrame, df_stations: pd.DataFrame):
    return df_depts.merge(df_stations, left_on=_col_names_.station_id, right_on=_col_names_.station_id)


class __dataframes(_immutable_object_):
    depts = _df_depts_
    stations = _df_stations_
    depts_w_stations = add_geographical_coordinates_to_df(depts, stations)
_dataframes_ = __dataframes()


class _plotting(_immutable_object_):
    token_mapbox = _json_d_['plotting']['mapbox_token']


class __module_data(_immutable_object_):
    col_names = _col_names_
    cat_data_vals = _cat_data_vals_
    data = _dataframes_
    plotting = _plotting()

internals = __module_data()
