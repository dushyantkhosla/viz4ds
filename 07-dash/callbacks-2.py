import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import sqlite3
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import plotly.graph_objs as go

from src import list_markets, dict_pmiMarket_to_ISO

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://unpkg.com/tachyons@4.10.0/css/tachyons.min.css',
                        'https://fonts.googleapis.com/css?family=Work+Sans']

external_scripts = ['https://cdn.jsdelivr.net/npm/vega@4',
                    'https://cdn.jsdelivr.net/npm/vega-lite@2',
                    'https://cdn.jsdelivr.net/npm/vega-embed@3']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts)

app.layout = \
html.Div(className='helvetica fw3',
         children=[
             html.H1('Interactive Widgets with Multiple Inputs', className='pa4 tc bg-blue white'),

         ])

# @app.callback(Output(),
#               [Input()])
# def udf(input_value):
#     '''
#     '''
#     result = None
#     return result

if __name__ == '__main__':
    app.run_server(debug=True)
