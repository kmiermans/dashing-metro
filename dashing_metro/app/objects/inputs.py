from dashing_metro.backend.imports import *
import dashing_metro as dm
from dashing_metro.backend.module_data import internals

checklist = dcc.Checklist(
    id='transport_types_checklist',
    options=[
        {'label': el, 'value': el} for el in internals.cat_data_vals.transport_types
    ],
    value=internals.cat_data_vals.transport_types
)
