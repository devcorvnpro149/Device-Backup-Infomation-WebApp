from navbar import create_navbar, create_navbar2

import dash
import dash_bootstrap_components as dbc
# from dash import html
# from dash import dcc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame

import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

nav = create_navbar2()

header = html.H3('Welcome to page 2!')

#data
df = pd.read_csv('./Data/my_backup.csv') #data frame
df['Date'] = pd.to_datetime(df['Date'])

#My Graph
fig = px.line(df, x='Date', y= 'Hosts', color='Status', title='Daily Status', height=550, 
            color_discrete_map={'successful':'#27ae60','failed':'#e55039'},
            line_shape='linear', template='presentation') #markers=True

fig.update_traces(line=dict(width=2.5))

fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(step="all"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=7, label="1w", step="day", stepmode="backward"),
            dict(count=1, label="24h", step="day", stepmode="backward"),
            dict(count=1, label="today", step="day", stepmode="todate")
        ])
    ),
    #type= 'date'
    #autorange= False,
    rangeslider=dict(
            visible=True
    ),
)

colors = {
    'background': '#111111',
    'text': '#8cc1fa',
    'sub_text':'#1b5ea6'
}

#Layout

body = html.Div([
    dbc.Container([
        html.Br(),

        dbc.Row([
            dbc.Col(html.H1(children='Dashboard'), className="mb-2")
        ]),

        dbc.Row([
            dbc.Col(html.H6(children='Visualize device backup status.'), className="mb-4")
        ]),

        dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Backup situation on cisco device',
                                 className="text-center text-light bg-dark"), body=True, color="dark")
        , className="mb-4")
        ]),

        dcc.Graph(id='line-chart',
        figure=fig),
        
        html.Button("Download csv", id="btn"), 
        Download(id="download")
    ]),
])



def create_page_2():
    layout = html.Div([
        nav,
        body,
    ])
    return layout





'''
body = html.Div(children=[
html.H1(children='Dashboard',
        style={
        'textAlign': 'center',
        'color': colors['text'],
        'fontSize': 50
        }
),

html.H3(children='Describe devices backup status.', style={
    'textAlign': 'center',
    'color': colors['sub_text'],
    'fontSize': 20
}),

html.Div(
    [
    html.Br(),
    dcc.Graph(id='line-chart',
        figure=fig),
    
    html.Button("Download csv", id="btn"), 
    Download(id="download")
    ]
)
])

@app.callback(
    Output("download", "data"), 
    [Input("btn", "n_clicks")]
)

def generate_csv(n_nlicks):
    return send_data_frame(df.to_csv, filename="BACKUP_INFO.csv")

'''