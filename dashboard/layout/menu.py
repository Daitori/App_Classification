from dash import dcc, html
import dash_bootstrap_components as dbc
import json
import os

#Image file format list
image_format = ["png","jpg","jpeg","svg","gif"]

#Menu description, peut être stocké dans un fichier json
menu_description = {
    "Testing humans": "On donne une série d'images à classifier pour obtenir une baseline de performance à comparer avec les modèles de classification d'images.",
    "Classification image": "Classification de l'image et ajout d'une nouvelle émotion ou d'images dans la base de données."

}

##Card seeing in menu page (/)
def create_card(title,desc,child,href,class_name="cardDiv menuCard"):
    #Check if the image file exist
    for i in image_format:
        img_file="dashboard/assets/images/"+desc+'.'+i
        if os.path.isfile(img_file):
                return html.Div(
                    children=[
                        html.H1(title,style={"font-size": "1.2rem"}),
                        html.Div(children=(html.P(menu_description[desc], className="menuDescription"),
                                        html.Img(src="/assets/images/"+desc+'.'+i, className="menuImage"), 
                                        dbc.Button(children=child, className="menuButton", href=href))),               
                    ],className=class_name,)
    return html.Div(
    children=[
        html.H1(title,style={"font-size": "1.2rem"}),
        html.Div(children=(html.P(menu_description[desc], className="menuDescription"),
                           dbc.Button(children=child, className="menuButton", href=href))),
    ],
    className=class_name,)

#add here new card for the page with href the url in callbacks_header and add necessary callback in callbacks_header
test_card = create_card("Test sur les humains","Testing humans","ENTRER",href="/evaluation")
classification_card= create_card("Ajout d'une nouvelle émotion","Classification image","ENTRER",href='/classification')

#Menu content
menu_content = html.Div(
    children=[
        test_card,
        classification_card
    ],
    className="tabContent flexDiv"
)