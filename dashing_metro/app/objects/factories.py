from dashing_metro.backend.imports import *
import dashing_metro as dm
from dashing_metro.backend.module_data import internals


def generate_delay_histogram(transport_types=internals.cat_data_vals.line_labels):
    sub_df = internals.data.depts.copy()
    sub_df = sub_df[sub_df['product'].isin(transport_types)]
    fig = px.histogram(sub_df, x='delay', histnorm='probability density', nbins=200)
    return fig


def generate_delay_per_station_map(transport_types=None):
    if transport_types is not None:
        raise NotImplementedError

    delays_by_station = internals.data.depts_w_stations.groupby(by=internals.col_names.station_id).agg(
        {'dep_id': 'count', 'delay': 'mean', 'latitude': 'first', 'longitude': 'first', 'station_name': 'first'})

    delays_by_station[delays_by_station['delay'].isna()] = 0
    # pivot_delays = pivot_delays.rename(columns={'dep_id': 'count'})
    #
    # pivot_delays['pivot_delays_as_frac'] = pivot_delays['count'] / df_d.groupby('station_id').count()['dep_id']
    # pivot_delays['depts_as_frac'] = df_d.groupby('station_id').count()['dep_id'] / len(df_d)

    # fig = px.scatter_mapbox(df_w_s, lat="latitude", lon="longitude", size='count')

    fig = px.scatter_mapbox(delays_by_station, lat="latitude", lon="longitude", size='delay')
                            # hover_data=['station_name'])

    fig.update_layout(mapbox_zoom=11)
    fig.update_layout(height=600, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(mapbox_style="light", mapbox_accesstoken=internals.plotting.token_mapbox)

    return fig

