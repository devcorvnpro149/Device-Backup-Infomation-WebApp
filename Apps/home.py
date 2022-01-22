import dash_html_components as html
import dash_bootstrap_components as dbc

from navbar import create_navbar, create_navbar2


nav = create_navbar2()   

body = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the devices dashboard", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='THIS WEB APP IS BUILT ON PLOTLY, DASH AND BOOTSTRAP, AND USE NETMIKO TO GET INFORMATION ABOUT NETWORK DEVICES'
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='IT HAS TWO MAIN PAGES, HOME PAGE TO CONTAIN INFORMATION ABOUT THIS DASHBOARD '
                                     'AND BACK-UP STATUS PAGE TO DISPLAY DEVICE CONFIGURATION BACK-UP INFORMATION.')
                    , className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='The main libraries used in this dashboard',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Dash Plotly", 
                                                                    href="https://dash.plotly.com/",
                                                                    outline=True,
                                                                    size="sm", color="primary"),
                                                        className="d-grid gap-2 col-6 mx-auto"),
                                                dbc.Col(dbc.Button("Netmiko",
                                                                    href="https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md#simple-example",
                                                                    outline=True, 
                                                                    size="sm", 
                                                                    color="primary", ),
                                                        className="d-grid gap-2 col-6 mx-auto")], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access the code used to build this dashboard',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/devcorvnpro149/Device-Backup-Infomation-WebApp",
                                                  outline=True,
                                                  color="primary",
                                                  size="sm",
                                                  className="d-grid gap-2 col-6 mx-auto"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='GET CSV FILE USED IN THIS DASHBOARD',
                                               className="text-center"),
                                       dbc.Button("file csv",
                                                  href="https://raw.githubusercontent.com/devcorvnpro149/Device-Backup-Infomation-WebApp/main/switch_backup2.csv",
                                                  download="device_backup.csv",
                                                  external_link=True,
                                                  outline=True,
                                                  color="primary",
                                                  size="sm",
                                                  className="d-grid gap-2 col-6 mx-auto"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5"),

    ])

])

#header = html.H3('Welcome to home page!')

def create_page_home():
    layout = html.Div([
        nav,
        body,
    ])
    return layout