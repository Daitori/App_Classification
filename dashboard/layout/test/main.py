from dash import dcc, html
import dash_bootstrap_components as dbc
from dashboard.layout.custom_elements import collapse_details
from dashboard.callbacks.test import setting_callback
import json

# Reading json file
emotions=setting_callback.emotions
number_of_images=setting_callback.data["setting"]["number_of_images"]
emotions_allowed=setting_callback.data["setting"]["emotions_to_test"]
number_of_choices=setting_callback.data["setting"]["number_of_choices"]

##For the description
description_body=collapse_details(
    elt_id="description_test",
    button_text="Description du test",
    collapse_children=[
        html.Div(
            children=[
                html.Div(
                children=[
                html.P("Le test de reconnaissance d'émotion complexe consiste à reconnaître des émotions complexes à partir d'expressions faciales. Les émotions complexes sont des émotions qui sont composées de plusieurs émotions de base. Par exemple, la surprise est composée de la peur et de la joie. Le test consiste à reconnaître les émotions suivantes :"),
                html.Ul(children=[html.Li(i,style={"display": "block","width":"25%","float":"left"}) for i in emotions])
                ])
            ],
            className="cardDiv flexDiv"
        ),
    ],
)


##For the evaluation

emotions_dropdown=dcc.Dropdown(emotions_allowed, id="emotionDropdown",multi=True,style={"margin-right":"1%","margin-top":"1%"},disabled=True)
emotions_comfirm=html.Div(children=[dbc.Button("Confirmer", id="confirm_button", className="confirmButton", n_clicks=0,style={"margin-right":"1%","margin-top":"1%"},disabled=True)],style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr","grid-gap":"1%"})
emotions_selection_interface=html.Div(children=[emotions_dropdown,emotions_comfirm],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%","margin-top":"10%"},className="cardDiv flexDiv")

start_stop_selection=html.Div(children=[dbc.Button("Start", id="start_button", className="startButton", n_clicks=0,style={"margin-right":"1%","margin-top":"1%"}),dbc.Button("Stop", id="stop_button", className="stopButton",disabled=True, n_clicks=0,style={"margin-right":"1%","margin-top":"1%"})],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"})
current_image_count=html.Div(children=[html.P(id="image_count",style={"margin-right":"1%","margin-top":"1%"})],style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr","grid-gap":"1%"})
start_stop_current_interface=html.Div(children=[start_stop_selection,current_image_count],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%","margin-top":"10%"},className="cardDiv flexDiv")

result_interface=html.Div(children=[emotions_selection_interface,start_stop_current_interface],style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr 1fr","grid-gap":"1%","margin-top":"5%"},className="cardDiv flexDiv")

user_selection=html.Div(children=[result_interface],className="cardDiv flexDiv",style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr "})

image_to_guess=html.Div(children=[html.Img(id="image-placeholder", src="", style={"width": "1000px", "height": "750px"})])

test_interface=html.Div(children=[user_selection,image_to_guess],className="cardDiv flexDiv",style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"})


tester=html.Div(children=[test_interface])

test_body=collapse_details(
    elt_id="test_body",
    button_text="Evaluation",
    collapse_children=[
        html.Div(
            children=[
                html.Div(
                children=[
                html.P("Pour le test, on affiche une image d'une personne qui exprime une émotion complexe. Ensuite, on demande à l'utilisateur de sélectionner l'émotion qui correspond. Ensuite, on affiche la bonne réponse et on demande à l'utilisateur de noter sa confiance en sa réponse. On répète ce processus pour une centaine d'image. À la fin du test, on affiche un bilan des résultats."),
                tester,
                ])
            ],
            className="cardDiv flexDiv",
        ),
    ],
)


##For the test tab

test_tab_content=html.Div(
    children=[
        description_body,
        test_body,
        dcc.Store(id="random_dataframe", storage_type="session", data={}),
        dcc.Store(id="json_read_test",storage_type="session",data={}),
        dcc.Interval(
            id='interval_update_test_main',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ]
)
