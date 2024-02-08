from dash import html, dcc
import dash_bootstrap_components as dbc
from math import ceil


def details(class_name):
    return html.Details(children=[html.Summary(children=[html.Img(src="../../assets/chevron-down.svg",
                                                                  style={'float': 'right',
                                                                         'margin': "4px 16px",
                                                                         'display': 'inline-block'})],
                                               className=class_name + "Summary"),
                                  html.Div(html.Div(className=class_name + "Content"), style={'border-top': "1px solid lightgrey"})],
                        className=class_name,
                        style={'border': "1px solid lightgrey"})


def collapse_details(elt_id, button_text, collapse_children, is_open=False):
    return html.Div(
        children=[
            html.Button(children=[html.Div(children=[html.Div(button_text, style={'display': "inline-block"}),
                                                     html.Img(src="../../assets/chevron-down.svg",
                                                              style={'float': 'right',
                                                                     'margin-top': 4,
                                                                     'margin-right': 12}),
                                                     ],
                                           className="collapseButtonChildren")],
                        id={'type': "details-button", 'index': elt_id},
                        className="collapseButton"),
            dbc.Collapse(
                style={'border-top': "solid 1px lightgrey"},
                is_open=is_open,
                id={'type': "details-collapse", 'index': elt_id},
                children=collapse_children
            ),
        ],
        className="collapseDetailsDiv",
        id=f"{elt_id}Div"
    )


def label_meter(value, class_name, step):
    return html.Meter(value=str(ceil(value / step) * step) if value <= 1 else "0",
                      title=str(round(value, 3)),
                      min='0', max='1', low='0.4', high='0.7', optimum='1',
                      className=class_name)

