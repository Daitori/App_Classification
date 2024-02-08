from dash import dcc, html
import dash_bootstrap_components as dbc
from dashboard.layout.custom_elements import collapse_details
from dashboard.callbacks.classification import main_callback

##For the description
description_body=collapse_details(
    elt_id="description_classification",
    button_text="Description",
    collapse_children=[
        html.Div(
            children=[
                html.Div(
                children=[
                html.P("Avec l'apprentissage actif, on donne à un utilisateur le rôle de l'oracle et on lui demande de fournir des annotations pour des échantillons sélectionnés par un algorithme. L'objectif est de minimiser le nombre d'échantillons annotés nécessaires pour atteindre un certain niveau de performance. L'apprentissage actif est particulièrement utile lorsqu'il est coûteux d'annoter des échantillons. Par exemple, dans le cas de l'annotation d'images, l'annotation manuelle peut être coûteuse en temps et en argent. L'apprentissage actif est également utile lorsque l'ensemble de données est très grand et que l'annotation de l'ensemble de données est impossible"),
                ])
            ],
            className="cardDiv flexDiv"
        ),
    ],
)


##For the classification

emotions_dropdown=dcc.Dropdown(id="emotionClassifierDropdown",multi=True,style={"margin-right":"1%","margin-top":"1%"},disabled=True)
emotions_comfirm=html.Div(children=[dbc.Button("Confirmer", id="confirm_button", className="confirmButton", n_clicks=0,style={"margin-right":"1%","margin-top":"1%"},disabled=True)],style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr","grid-gap":"1%"})
emotions_selection_interface=html.Div(children=[emotions_dropdown,emotions_comfirm],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%","margin-top":"10%"},className="cardDiv flexDiv")

start_stop_selection=html.Div(children=[dbc.Button("Start", id="start_button", className="startButton", n_clicks=0,style={"margin-right":"1%","margin-top":"1%"}),dbc.Button("Stop", id="stop_button", className="stopButton",disabled=True, n_clicks=0,style={"margin-right":"1%","margin-top":"1%"})],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"})
start_stop_current_interface=html.Div(children=[start_stop_selection],style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%","margin-top":"10%"},className="cardDiv flexDiv")

result_interface=html.Div(children=[emotions_selection_interface,start_stop_current_interface],style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr 1fr","grid-gap":"1%","margin-top":"5%"},className="cardDiv flexDiv")

file_upload=html.Div(children=
        dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'height': '200px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin-top':'1%',
            'margin-right':'1%',
            'width':'500px',
            },
        # Allow multiple files to be uploaded
        multiple=True
        ),className="cardDiv flexDiv",
        style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"})


user_selection=html.Div(children=[result_interface,file_upload],className="cardDiv flexDiv",style={"display":"grid","grid-template-columns":"1fr","grid-template-rows":"1fr "})

image_to_guess=html.Div(children=[html.Img(id="image-placeholder", src="", style={"width": "1000px", "height": "750px"})])

test_interface=html.Div(children=[user_selection,image_to_guess],className="cardDiv flexDiv",style={"display":"grid","grid-template-columns":"1fr 1fr","grid-template-rows":"1fr","grid-gap":"1%"})

classification_main=html.Div(
    children=[
        test_interface,
    ],
)

classification_body=collapse_details(
    elt_id="classification",
    button_text="Classification",
    collapse_children=[
        html.Div(
            children=[
                html.Div(
                children=[classification_main
                ])
            ],
            className="cardDiv flexDiv"
        ),
    ],
)



##For the test tab

classification_tab_content=html.Div(
    children=[
        description_body,
        classification_body
    ]
)
