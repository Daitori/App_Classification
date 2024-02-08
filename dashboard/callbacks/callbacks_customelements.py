from dashboard.index import app
from dash import callback_context
from dash.dependencies import Input, Output, State, MATCH
from dash.exceptions import PreventUpdate


@app.callback(
    Output({'type': "details-collapse", 'index': MATCH}, 'is_open'),
    Input({'type': "details-button", 'index': MATCH}, 'n_clicks'),
    State({'type': "details-collapse", 'index': MATCH}, 'is_open')
)
def collapse_details(clicked, opened):
    """collapses or extends custom collapse_details element on button click"""
    if clicked:
        return not opened
    raise PreventUpdate


@app.callback(
    Output({'type': "modInput", 'index': MATCH}, 'value'), Output({'type': "modSlider", 'index': MATCH}, 'value'),
    Input({'type': "modInput", 'index': MATCH}, 'value'), Input({'type': "modSlider", 'index': MATCH}, 'value'),
)
def input_thr(txt_input, slider):
    """circular callback of matching index and slider, refreshes both value attributes if any input changes"""
    trigger_id = callback_context.triggered_id['type'] if callback_context.triggered_id else "modSlider"
    try:
        value = eval(txt_input) if trigger_id == "modInput" else slider
        return value, value
    except SyntaxError or NameError: raise PreventUpdate
