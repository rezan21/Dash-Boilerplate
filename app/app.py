import base64
import json

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plots
import utils
import views
from dash import Dash, Input, Output, dcc, html

# import dash_bootstrap_components as dbc
# from dash import no_update


app = Dash(
    __name__,
    # external_stylesheets=[dbc.themes.BOOTSTRAP],
)
pio.templates.default = "plotly_dark"

# load data
with open("app/data/source1.json") as file:
    _list = json.load(file)

with open("app/data/image.png", "rb") as f:
    img = base64.b64encode(f.read()).decode()

df = pd.read_csv("app/data/source2.csv")

# tabs
tabs = dcc.Tabs(
    [
        dcc.Tab(
            views.tab1.get_tab(df, _list),
            label="Tab 1",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
        dcc.Tab(
            html.H2("Tab 2 content"),
            label="Tab 2",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
    ]
)

# layout
app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="menu",
            children=[
                html.Div(className="showcase", children=tabs),
                html.Img(src=f"data:image/png;base64,{img}", style={"width": "500px", "height": "500px"}),
            ],
        ),
    ],
)


@app.callback(
    Output(component_id="temp_fig_c", component_property="figure"),
    Input(component_id="dropdown_id", component_property="value"),
)
def update_drift_barchart(x):
    if x:
        y = utils.dummy_get_y(x)
        fig = plots.plot_line(df, x=x, y=y)
        return fig
    return go.Figure()


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)
