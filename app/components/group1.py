from dash import dcc, html


def temp_h1_c(text):
    comp_name = "temp_h1_c"
    return html.H1(id=comp_name, children=text)


def temp_fig_c(figure):
    comp_name = "temp_fig_c"
    return dcc.Graph(id=comp_name, figure=figure)
