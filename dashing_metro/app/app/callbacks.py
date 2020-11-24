from dashing_metro.backend.imports import *
# from dashing_metro import app
# import dashing_metro.layout.objects as gm_obj
from .app import app
from ..objects import graphs, inputs, factories
import dashing_metro as dm


@app.callback(Output(graphs.histogram_delays_all.id, 'figure'),
                      Input(inputs.checklist.id, 'value'))
def update_delay_histogram_based_on_transport_types(transport_types):
    return factories.generate_delay_histogram(dm.backend.variables.df, transport_types)



