import components
import plotly.graph_objects as go
from dash import dcc, html


def get_tab(df, _list):
    return html.Div(
        [
            html.H1("Choose X:"),
            dcc.Dropdown(_list, id="dropdown_id"),
            components.group1.temp_h1_c("Hello World!"),
            components.group1.temp_fig_c(go.Figure()),
            components.group2.temp_table_c(df),
        ]
    )
