from dash import Input, Output, State
from dashboard.index import app
from PIL import Image

import os
import pandas as pd 
import datetime
import json

dataset_path = "dashboard/assets/images_dataset/CFEE/"
labels = os.listdir(dataset_path)
emotions=[labels[i].replace("_"," ") for i in range(len(labels))]
database = [dataset_path + label for label in labels]
date_today = datetime.datetime.now().strftime("%Y-%m-%d")
json_setting_path = "dashboard/assets/setting.json"

def multiple_dir_files_to_df(dirs, label):
    df = pd.DataFrame()
    for idx,dir in enumerate(dirs):      
        if dir.split("/")[-1] in label:
            files = os.listdir(dir)
            files = [dir + "/" + file for file in files]
            df = pd.concat([df,pd.DataFrame({"file": files, "label": dir.split("/")[-1]})])
    return df

@app.callback(
    Output("json_read_test", "data"),
    Input("interval_update_test_setting", "n_intervals"),
)

def update_setting(n):
    with open(json_setting_path) as f:
        data = json.load(f)
    return data


@app.callback(  
    Output("image-placeholder", "src",allow_duplicate=True),
    Output("image_count", "children",allow_duplicate=True),
    Output("random_dataframe", "data",allow_duplicate=True),
    Output("emotionDropdown", "options",allow_duplicate=True),
    Output("start_button", "disabled",allow_duplicate=True),
    Output("emotionDropdown","disabled"),
    Output("confirm_button","disabled"),
    Output("stop_button","disabled"),
    Input("start_button", "n_clicks"),
    State("json_read_test", "data"),
    prevent_initial_call=True,
)

def start_test(n_clicks,json_data):
    print(json_data["setting"]["emotions_to_test"])
    df = multiple_dir_files_to_df(database,json_data["setting"]["emotions_to_test"])
    df_random = df.sample(json_data["setting"]["number_of_images"])
    df_random["Guess"] = ""
    df_random["Correct"] = ""
    return Image.open(df_random["file"].iloc[0]), f"Image 1/{json_data['setting']['number_of_images']}", df_random.to_dict("records"),[{"label": i, "value": i} for i in json_data["setting"]["emotions_to_test"]], True, False, False, False

@app.callback(
    Output("image-placeholder", "src",allow_duplicate=True),
    Output("image_count", "children",allow_duplicate=True),
    Output("random_dataframe", "data",allow_duplicate=True),
    Output("start_button", "disabled",allow_duplicate=True),
    Output("emotionDropdown","disabled",allow_duplicate=True),
    Output("confirm_button","disabled",allow_duplicate=True),
    Output("stop_button","disabled",allow_duplicate=True),
    Input("stop_button", "n_clicks"),
    prevent_initial_call=True,
)

def stop_test(n_clicks):
    return "", "", pd.DataFrame().to_dict("records"), False, True, True, True

@app.callback(
    Output("image-placeholder", "src",allow_duplicate=True),
    Output("image_count", "children",allow_duplicate=True),
    Output("random_dataframe", "data",allow_duplicate=True),
    Output("emotionDropdown", "value"),
    Output("start_button", "disabled",allow_duplicate=True),
    Output("stop_button","disabled",allow_duplicate=True),
    Output("emotionDropdown","disabled",allow_duplicate=True),
    Output("confirm_button","disabled",allow_duplicate=True),
    Input("confirm_button", "n_clicks"),
    State("emotionDropdown", "value"),
    State("image_count", "children"),
    State("random_dataframe", "data"),
    State("json_read_test", "data"),
    prevent_initial_call=True,
)

def confirm_emotion(n_clicks,values,image_count,data,json_data):
    number = int(image_count.split("/")[0].split(" ")[1])
    df = pd.DataFrame(data)
    df["Guess"][number-1] = values
    df["Correct"][number-1] = True if df["label"][number-1] in values else False
    if number == json_data["setting"]["number_of_images"]:
        accuracy = df["Correct"].sum()/json_data["setting"]["number_of_images"]
        df.to_csv(f"dashboard/assets/testing_result/test_sample_{json_data['setting']['number_of_images']}_{date_today}.csv") 
        return "", f"Accuracy: {accuracy}", pd.DataFrame().to_dict("records"), [], False,True, True, True
    return Image.open(df["file"][number]), f"Image {number+1}/{json_data['setting']['number_of_images']}", df.to_dict("records"), [] ,True ,False, False, False 

@app.callback(
    Output("emotionDropdown", "options",allow_duplicate=True),
    Input("emotionDropdown", "value"),
    State("json_read_test", "data"),
    prevent_initial_call=True,
)

def update_emotion_dropdown(values,json_data):
    if len(values) == json_data["setting"]["number_of_choices"]:
        return [{"label": i, "value": i} for i in json_data["setting"]["emotions_to_test"] if i in values]
    else:
        return [{"label": i, "value": i} for i in json_data["setting"]["emotions_to_test"]]
