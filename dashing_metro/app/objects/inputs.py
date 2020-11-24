from dashing_metro.backend.imports import *
import dashing_metro as dm


checklist = dcc.Checklist(
    id='transport_types_checklist',
    options=[
        {'label': el, 'value': el} for el in dm.backend.variables.transport_types
    ],
    value=dm.backend.variables.transport_types
)
