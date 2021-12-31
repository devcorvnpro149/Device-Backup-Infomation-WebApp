import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame
from dash.dependencies import Input, Output
# from dash import Dash, dcc, html, Input, Output

import pandas as pd
import plotly.express as px


#Dash app
app = dash.Dash(__name__)

#data
df = pd.read_csv('switch_backup2.csv') #data frame
df['Date'] = pd.to_datetime(df['Date'])

#My Graph
fig = px.line(df, x='Date', y= 'Hosts', color='Status', title='Backup status', height=550, 
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
app.layout = html.Div(children=[
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

# #Callback
# @app.callback(
#     Output(component_id='price-graph', component_property='figure'),
#     [Input(component_id='geo-dropdown', component_property='value')]
# )
# def update_graph(selected_geography):
#     filtered_avocado = avocado[avocado['geography'] == selected_geography]
#     line_fig = px.line(filtered_avocado,
#                        x='date', y='average_price',
#                        color='type',
#                        title=f'Avocado Prices in {selected_geography}')
#     return line_fig


# Run app
if __name__ == '__main__':
    app.run_server(port=8151, debug=True, use_reloader=False)

'''

import dash
import dash_html_components as html
import numpy as np
import pandas as pd

from dash.dependencies import Output, Input
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame

# Generate some example data.
data = np.column_stack((np.arange(10), np.arange(10) * 2))
df = pd.DataFrame(columns=["a column", "another column"], data=data)
# Create app.
app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div([html.Button("Download csv", id="btn"), Download(id="download")])

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def generate_csv(n_nlicks):
    return send_data_frame(df.to_csv, filename="some_name.csv")

if __name__ == '__main__':
    app.run_server()


'''