from dash import dcc, html
import dash_bootstrap_components as dbc
import json
from dashboard.layout.custom_elements import collapse_details
from dashboard.callbacks.test import main_callback, setting_callback


emotions=setting_callback.emotions
number_of_images=setting_callback.number_of_images
emotions_allowed=setting_callback.emotions_allowed
number_of_choices=setting_callback.number_of_choices
data=setting_callback.data
##For the evaluation parameter
#For the description
description_setting_testing=html.Div(children=[html.P("Les paramètres du test de reconnaissance d'émotion complexe sont les suivants :"),
                                               html.Ul(children=[html.Li(f"Nombre d'images à tester : {number_of_images}",id="number_of_images_setting_testing_description"),
                                                                 html.Li(f"Nombre de choix pour chaque image : {number_of_choices}",id="number_of_choices_setting_testing_description"),
                                                                html.Li(children=["Emotions à tester:",html.Ul(children=[html.Li(i,style={"display": "block","width":"25%","float":"left"}) for i in emotions_allowed],id="emotions_to_test_setting_testing")])
                                                            ])],className="cardDiv flexDiv")

#For selection of the parameters
parameter_selection=html.Div(children=[html.Div(children=[html.P("Nombre d'images à tester : "),dcc.Input(id="number_of_images_setting_testing",type="number",value=number_of_images,style={"margin-right":"1%","margin-top":"1%"})],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"}),
                                        html.Div(children=[html.P("Nombre de choix pour chaque image : "),dcc.Input(id="number_of_choices_setting_testing",type="number",value=number_of_choices,style={"margin-right":"1%","margin-top":"1%"})],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"}),
                                        html.Div(children=[html.P("Emotions à tester : "),dcc.Dropdown(emotions,value=emotions_allowed, id="emotionDropdown_setting_testing",multi=True,style={"margin-right":"1%","margin-top":"1%"})],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"}),
                                        dbc.Button("Confirmer", id="confirm_setting_testing", className="confirmButton", n_clicks=0,style={"margin-right":"1%","margin-top":"1%"}),],
                                        style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr 1fr","grid-gap":"1%","margin-top":"10%"},className="cardDiv flexDiv")

parameter_body=collapse_details(
    elt_id="parameter_test",
    button_text="Paramètre du test (Fonctionnel mais améliorable)",
    collapse_children=[
        html.Div(
            children=[
                html.Div(
                children=[description_setting_testing,
                          parameter_selection
                ])
            ],
            className="cardDiv flexDiv"
        ),
    ],
)

##For the test tab

test_setting_tab_content=html.Div(
    children=[
        parameter_body,
        dcc.Store(id="json_read_setting_test",storage_type="session",data=data),
        dcc.Interval(
            id='interval_update_test_setting',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ],
)
