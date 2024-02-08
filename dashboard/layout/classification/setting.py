from dash import dcc, html
import dash_bootstrap_components as dbc
from dashboard.layout.custom_elements import collapse_details

##For the evaluation parameter
parameter_body=collapse_details(
    elt_id="parameter_classification",
    button_text="Paramètre du test",
    collapse_children=[
        html.Div(
            children=[
                html.Div(
                children=[
                html.P("Le test de reconnaissance d'émotion complexe consiste à reconnaître des émotions complexes à partir d'expressions faciales. Les émotions complexes sont des émotions qui sont composées de plusieurs émotions de base. Par exemple, la surprise est composée de la peur et de la joie. Le test consiste à reconnaître les émotions complexes suivantes :"),
                ])
            ],
            className="cardDiv flexDiv"
        ),
    ],
)

##For the test tab

classification_setting_tab_content=html.Div(
    children=[
        parameter_body,
    ]
)
