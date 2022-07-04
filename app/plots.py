import plotly.express as px
import plotly.graph_objects as go


def plot_line(df, x, y):
    fig = px.line(df, x=x, y=y)
    return fig


def plot_table(df, title="", dp=3, plot_header=True, col_widths=None):
    df = df.round(dp)  # round to d.p.

    h_values = [f"<b>{col}</b>" for col in df.columns]
    c_values = [df[col] for col in df.columns]

    blue, gray, black, white = "#636efa", "#000", "#3c3c3c", "#fff"
    alternate_row_colors = [[black, gray] * len(df)]

    # cells
    cells = dict(
        values=c_values,
        fill_color=alternate_row_colors,
        # line_color=blue,
        align="left",
        font=dict(color="white", size=13, family="arial"),
        height=30,
    )

    # header
    if plot_header:
        header = dict(
            values=h_values,
            fill_color=blue,
            # line_color=white,
            align="left",
            font=dict(color=white, size=14, family="arial"),
        )

    table = go.Table(columnwidth=col_widths, cells=cells, header=header if "header" in locals() else None)
    fig = go.Figure(data=table)
    fig.update_layout(
        title=dict(
            text=title,
            y=0.99,
            x=0.5,
            xanchor="center",
            yanchor="top",
            font=dict(size=17, family="arial"),
        ),
        margin=dict(l=20, r=20, b=0, t=35, pad=50),
        template="plotly_dark",
    )
    return fig
