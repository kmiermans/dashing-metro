from dashing_metro.backend.imports import *
# import dashing_metro as dm
from ..objects import graphs as dm_graphs
from ..objects import inputs as dm_inputs



checklist = dm_inputs.checklist

main_layout = html.Div([dm_graphs.histogram_delays_all,
                        dm_graphs.scatter_mapbox,
                        checklist
                        ])