import dashing_metro.backend.module_data
from dashing_metro.backend.imports import *
from . import factories as dm_factories
import dashing_metro as dm
from dashing_metro.backend.module_data import internals


histogram_delays_all = dcc.Graph(
    id='histogram_delays_all',
    figure=dm_factories.generate_delay_histogram(internals.data.depts)
    )

scatter_mapbox = dcc.Graph(
    id='scatter_mapbox',
    figure=dm_factories.generate_delay_per_station_map()
    )
