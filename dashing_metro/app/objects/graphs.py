from dashing_metro.backend.imports import *
from . import factories as dm_factories
import dashing_metro as dm


histogram_delays_all = dcc.Graph(
    id='histogram_delays_all',
    figure=dm_factories.generate_delay_histogram(dm.backend.variables.df)
    )
