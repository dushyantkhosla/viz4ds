import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np
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

MARKDOWN_COMPONENT = dcc.Markdown(children='''
* Construct `Input` and `Output` using components from the `dash.dependencies` module (**not** `dcc`)
 * Use the `value` and `children` properties of these components + a decorated user-defined function to add interactivity
 * The `@app.callback()` decorator
   - wraps around the UDF that is called each time the `Input` changes
   - passes the new value to the function and updates the `Output` with the returned object

> _Frequently we'll update the children of a component to display new text or the figure of a `dcc.Graph` component to display new data,
but we could also update the `style` of a component or even the available `options` of a `dcc.Dropdown` component_

Here's an example that updates a `Graph` based on the value from a `Slider`

---
```python
# Set up the I/O components

app.layout = html.Div([
   dcc.Graph(id='driven-plot'),
   dcc.Slider(id='driver-slider',
              min=0, max=10, value=4)
])

# Define the callback function

@app.callback(Output(component_id='driven-plot', component_property='figure'),
            [Input(component_id='driver-slider', component_property='value')])
def update_plot(slider_value):
   '''
   '''
   df = pd.DataFrame(data=np.random.randn(100, slider_value), columns=[f'Col_{i}' for i in range(slider_value)]).cumsum()
   data_ = [go.Scatter(x=df.index.values,
                       y=df.loc[:, c].values,
                       name=c) for c in df.columns]
   result = {
       'data': data_,
       'layout': go.Layout(xaxis={'title': 'horz-axis'},
                           yaxis={'title': 'vert-axis'},
                           margin={'l': 40, 'b': 40, 't': 10, 'r': 10})
   }
   return result
```
---
''',
className='container mt4 ph4')

app.layout = \
html.Div(className='avenir fw3',
         children=[
             html.H1(children='Understanding Dash Callbacks',
                     className='tc'),
             MARKDOWN_COMPONENT,
             # Declare inputs and outputs
             html.Div(className='container mt4 ph4',
                      children=[
                          html.H4('Please select a value on the slider below:'),
                          dcc.Slider(id='driver-slider', min=1, max=10, value=4, marks={f'{1+i}': 1+i for i in range(10)},
                                     className='mb4'),
                          dcc.Graph(id='driven-plot')
                          ]),
             ])

@app.callback(Output('driven-plot', 'figure'),
              [Input('driver-slider', 'value')])
def update_plot(slider_value):
    '''
    '''
    df = pd.DataFrame(data=np.random.randn(100, slider_value), columns=[f'Col_{1+i}' for i in range(slider_value)]).cumsum()
    data_ = [go.Scatter(x=df.index.values,
                        y=df.loc[:, c].values,
                        name=c) for c in df.columns]
    result = {
        'data': data_,
        'layout': go.Layout(xaxis={'title': 'horz-axis'},
                            yaxis={'title': 'vert-axis'},
                            margin={'l': 40, 'b': 40, 't': 40, 'r': 40}
                            )
    }
    return result

if __name__ == '__main__':
    app.run_server(debug=True)
