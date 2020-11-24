from .server import app
from ..layout.main import layout


def run_server():
    app.layout = layout

    app.run_server(debug=True, dev_tools_hot_reload=True, dev_tools_hot_reload_interval=2)
