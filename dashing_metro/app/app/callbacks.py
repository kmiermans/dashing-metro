import dashing_metro.backend.module_data
from dashing_metro.backend.imports import *
# from dashing_metro import app
# import dashing_metro.layout.objects as gm_obj
from .app import app
from ..objects import graphs, inputs, factories
import dashing_metro as dm
from dashing_metro.backend.module_data import internals


@app.callback([Output(graphs.histogram_delays_all.id, 'figure'),
               Output(graphs.scatter_mapbox.id, 'figure')],
                      Input(inputs.checklist.id, 'value'))
def update_delay_histogram_based_on_transport_types(transport_types):
    return [factories.generate_delay_histogram(transport_types),
            factories.generate_delay_per_station_map(transport_types)]



