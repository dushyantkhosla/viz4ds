import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://unpkg.com/tachyons@4.10.0/css/tachyons.min.css',
                        'https://fonts.googleapis.com/css?family=Work+Sans']

external_scripts = ['https://cdn.jsdelivr.net/npm/vega@4',
                    'https://cdn.jsdelivr.net/npm/vega-lite@2',
                    'https://cdn.jsdelivr.net/npm/vega-embed@3']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts)

df = pd.DataFrame({
    'A': range(10),
    'B': range(20, 30)
    })

def make_html_table_from_df(df: pd.DataFrame, max_rows: int = 20):
    '''
    '''
    return html.Table(children=[html.Tr([html.Th(i) for i in df.columns])] + \
                               [html.Tr([html.Td(i) for i in row]) for row in df.head(max_rows).values.tolist()]
    )

app.layout = \
html.Div(children=[html.H1(children='Hello World!',
                           className='pa3 bg-washed-red f-subheadline ba',
                           style={'fontFamily': 'Work Sans'}),
                   html.P(children='Dash: A web application framework for Python',
                          className='ph4 ba'),
                   dcc.Graph(id='example-graph',
                             figure={
                                 'data': [
                                     {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                     {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}],
                                 'layout': {
                                     'title': 'Dash Data Visualization'}
                                 }),
                   dcc.Markdown(children='''
                                # Markdown Section

                                Lorem Ipsum bla bla bla

                                - Bullet 01
                                - Bullet 02

                                > Premature optimization is the root of all evil.
                                '''.replace('  ', ''),
                                className='bg-washed-green container ba'
                                ),
                   html.Div(id='bar-chart-01'),
                   make_html_table_from_df(df=df, max_rows=6),
                   html.Div(id='dropdown-1',
                            className='container pa3',
                            children=[html.H4('Please select an option:'),
                                      dcc.Dropdown(
                                          options=[
                                              {'label': 'New York City', 'value': 'NYC'},
                                              {'label': 'Montréal', 'value': 'MTL'},
                                              {'label': 'San Francisco', 'value': 'SF'}],
                                          multi=True,
                                          value='MTL')
                                      ]
                            ),
                   html.Div(id='sliders',
                            className='container mt5',
                            children=[
                                html.P('Use the slider to pick a value:', className='f3 courier'),
                                dcc.Slider(min=0, max=10, step=0.5, value=5),
                                dcc.Slider(min=0, max=9, marks={i: f'Label {i}' for i in range(12)}, value=5)
                            ]),
                   html.Div(id='radio-buttons',
                            className='container mt5 pa3 bg-black',
                            children=[
                                html.P('Choose either: ', className='f3 helvetica white'),
                                dcc.RadioItems(options=[
                                    {'label': 'True', 'value': True},
                                    {'label': 'False', 'value': False}],
                                    value=False,
                                    className='f3 white'
                                )

                            ])


                   ])



if __name__ == '__main__':
    app.run_server(debug=True)
