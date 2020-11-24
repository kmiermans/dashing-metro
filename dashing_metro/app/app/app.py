from .server import app
from ..layout.main import main_layout
from .callbacks import *


def run_server():
    # app = dm.app
    # app.layout = dm.layout.layout
    app.layout = main_layout

    app.run_server(debug=True, dev_tools_hot_reload=True, dev_tools_hot_reload_interval=2)
