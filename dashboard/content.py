from dashboard.index import app
from dashboard.layout.header import header
from dash import html, dcc

page_content = html.Div(
    children=[],
    id='pageContent'
)

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        header,
        page_content
    ]
)

