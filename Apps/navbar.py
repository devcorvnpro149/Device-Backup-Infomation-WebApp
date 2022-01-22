import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container


def create_navbar():
    # Create the Navbar using Dash Bootstrap Components
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu", # Label given to the dropdown menu
                children=[
                    # In this part of the code we create the items that will appear in the dropdown menu on the right
                    # side of the Navbar.  The first parameter is the text that appears and the second parameter
                    # is the URL extension.
                    dbc.DropdownMenuItem("Home", href='/'), # Hyperlink item that appears in the dropdown menu
                    dbc.DropdownMenuItem(divider=True), # Divider item that appears in the dropdown menu
                    dbc.DropdownMenuItem("Page 2", href='/page-2'), # Hyperlink item that appears in the dropdown menu
                    dbc.DropdownMenuItem("Page 3", href='/page-3'), # Hyperlink item that appears in the dropdown menu
                ],
            ),
        ],
        brand="Home",  # Set the text on the left side of the Navbar
        brand_href="/",  # Set the URL where the user will be sent when they click the brand we just created "Home"
        sticky="top",  # Stick it to the top... like Spider Man crawling on the ceiling?
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for light text)
    )

    return navbar


def create_navbar2():

    dropdown = dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu", # Label given to the dropdown menu
            color="warning",
            toggle_style={"color": "#dfe6e9"},
            toggleClassName="p-4",
            children=[
                dbc.DropdownMenuItem("Home", href='/'), # Hyperlink item that appears in the dropdown menu
                dbc.DropdownMenuItem(divider=True), # Divider item that appears in the dropdown menu
                dbc.DropdownMenuItem("Page 2", href='/page-2'), # Hyperlink item that appears in the dropdown menu
                dbc.DropdownMenuItem("Page 3", href='/page-3'), # Hyperlink item that appears in the dropdown menu
            ],
    ),

    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="/assets/pie-chart.png", height="65px")),
                            dbc.Col(dbc.NavbarBrand("Dash", className="ms-2")),
                            dbc.Col('===================================================================================', style={'color': '#343A40'}),
                            dbc.Col(dropdown),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                )
            ]
        ),
        color="dark",
        dark=True,
    )
    return navbar

