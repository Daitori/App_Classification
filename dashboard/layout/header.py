from dashboard.callbacks import callbacks_header
from dashboard.callbacks import callbacks_customelements
from dashboard.callbacks.callbacks_header import page_dict
import dash_bootstrap_components as dbc

##We add the new page from callbacks_header when we add a new page/card with page

index=[dbc.DropdownMenuItem("Plus de pages", header=True)]+[dbc.DropdownMenuItem(id='page-'+str(i)+'-link') for i in range(2,len(page_dict)+1)]
navbar = dbc.NavbarSimple( #current page
    children=[
        dbc.NavItem(dbc.NavLink(id='page-1-link')), #menu
        dbc.DropdownMenu(
            children=index,
            nav=True,
            in_navbar=True,
            label="Autres",
            style={'margin-left': 10}
        ),
    ],
    brand="Affective Computing",
    brand_href="/",
    color="primary",
    dark=True,
)
header = navbar

