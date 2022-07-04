from dash import dash_table

# import pandas as pd


def temp_table_c(df):
    comp_name = "temp_table_c"
    shared_style = {
        "color": "white",
        "textAlign": "left",
        "fontSize": "13px",
        "fontFamily": "arial",
        "border": "1px solid black",
    }
    return dash_table.DataTable(
        id=comp_name,
        data=df.to_dict("records"),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_as_list_view=True,
        # tooltip_data=[
        #     {column: {"value": str(value), "type": "markdown"} for column, value in row.items()}
        #     for row in pd.DataFrame(df["feature"]).to_dict("records")
        # ],
        # tooltip_duration=None,
        fixed_rows={"headers": True},
        # page_size=10, # pagination
        # filter_action="native",
        style_header={
            "backgroundColor": "#636efa",
            "fontWeight": "bold",
            **shared_style,
        },
        style_filter={"backgroundColor": "#636efa", **shared_style},
        style_data={
            "backgroundColor": "#111111",
            **shared_style,
        },
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "black",
            }
        ],
        style_cell={
            "minWidth": "15px",
            "width": "15px",
            "maxWidth": "100px",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
        },
        css=[{"selector": ".dash-table-tooltip", "rule": "background-color: black; font-family: arial; color: white"}],
    )
