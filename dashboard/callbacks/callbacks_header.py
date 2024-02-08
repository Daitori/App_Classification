from dashboard.index import app
from dashboard.layout.test.main import test_tab_content
from dashboard.layout.test.setting import test_setting_tab_content
from dashboard.layout.classification.main import classification_tab_content
from dashboard.layout.classification.setting import classification_setting_tab_content
from dashboard.layout.menu import menu_content
from dash.dependencies import Input, Output, State
from dash import dcc, html


## Add a new list if you add a new page/card
test_tab_content=dcc.Tabs(id="selectTestTab", value='testTab', children=[
    dcc.Tab(test_tab_content, label="Evaluation de reconnaissance d'émotion complexe", value='testTab'),
    dcc.Tab(test_setting_tab_content, label="Paramètres", value='settingTab')
])

classification_tab_content=dcc.Tabs(id="selectClassificationTab",value='classificationTab',children=[
    dcc.Tab(classification_tab_content,label="Classification et ajout d'émotion", value='classificationTab'),
    dcc.Tab(classification_setting_tab_content,label="Paramètres", value='settingTab')
])

#Dictionnary for "url" and what to show
#in the menu "Autres"

page_dict = {
    "/": ["Page d'accueil", menu_content],
    "/evaluation": ["Reconnaissance d'émotion complexe", test_tab_content],
    "/classification": ["Classification et rajout d'émotion ",classification_tab_content]
}

#if you add a new element dont forget to add new link in header
@app.callback(
    [(Output(f"page-{i}-link", "href"), Output(f"page-{i}-link", "children")) for i in range(1, len(page_dict)+1)]+[Output("pageContent", "children")],
    [Input("url", "pathname")],
)


##No need to change
def update_current_page(pathname):
    """updates current page when header dropdown clicked"""
    page_list = list(page_dict.keys())
    page_list.remove(pathname)
    return [(link, page_dict[link][0]) for link in [pathname]+page_list]+[page_dict[pathname][1]]

@app.callback(
    Output("my-checklist", "value"),
    [Input("all-or-none", "value")],
    [State("my-checklist", "options")],
)
def select_all_none(all_selected, options):
    all_or_none = []
    all_or_none = [option["value"] for option in options if all_selected]
    return all_or_none

