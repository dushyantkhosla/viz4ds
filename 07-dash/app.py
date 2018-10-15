import dash
import dash_core_components as dcc
import dash_html_components as html

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

# import altair as alt
# from vega_datasets import data
#
# chart = alt.Chart(data.cars.url).mark_point().encode(
#     x='Horsepower:Q',
#     y='Miles_per_Gallon:Q',
#     color='Origin:N'
# )
#
# chart.save('assets/altair.html')

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
                   ])



if __name__ == '__main__':
    app.run_server(debug=True)
