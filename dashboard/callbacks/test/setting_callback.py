from dash import Input, Output, State,html
from dashboard.index import app
import os
import pandas as pd 
import json

# Reading json file
json_setting_path = "dashboard/assets/setting.json"
with open(json_setting_path) as f:
    data = json.load(f)

number_of_images=data["setting"]["number_of_images"]
emotions_allowed=data["setting"]["emotions_to_test"]
number_of_choices=data["setting"]["number_of_choices"]

dataset_path = "dashboard/assets/images_dataset/CFEE/"
labels = os.listdir(dataset_path)
emotions=[labels[i].replace("_"," ") for i in range(len(labels))]
database = [dataset_path + label for label in labels]

@app.callback(
    Output("number_of_images_setting_testing_description", "children"),
    Output("number_of_choices_setting_testing_description", "children"),
    Output("emotions_to_test_setting_testing", "children"),
    Input("interval_update_test_setting", "n_intervals"),
    State("json_read_setting_test", "data"),
)

def update_setting(n,data):
    return f"Nombre d'images à tester : {data['setting']['number_of_images']}", f"Nombre de choix pour chaque image : {data['setting']['number_of_choices']}",[html.Li(i,style={"display": "block","width":"25%","float":"left"}) for i in data['setting']['emotions_to_test']]

@app.callback(
    Output("json_read_setting_test", "data"),
    Output("number_of_images_setting_testing", "value"),
    Output("emotionDropdown_setting_testing", "value"),
    Output("number_of_choices_setting_testing", "value"),
    Input("confirm_setting_testing", "n_clicks"),
    State("number_of_images_setting_testing", "value"),
    State("emotionDropdown_setting_testing", "value"),
    State("number_of_choices_setting_testing", "value"),
    prevent_initial_call=True,
)

def comfirm_setting(n_clicks, number_of_images_value,emotions_value,number_of_choices_value):
    # Writing to json file
    data = {
        "setting": {
            "number_of_images": number_of_images_value,
            "emotions_to_test": emotions_value,
            "number_of_choices": number_of_choices_value
        }
    }
    with open(json_setting_path, 'w') as f:
        json.dump(data, f, indent=4)
    return data,None,None,None
