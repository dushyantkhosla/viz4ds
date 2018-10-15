# Building Apps with Dash

Dash apps are composed of two parts.

- "layout": describes what the application looks like and is composed of a *tree* of HTML and Dash components
- "engine": describes the interactivity of the application
- Example

```
# app.py

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = Div(children=[
    H1(children='Hello Dash'),

    Div(children='''
        Dash: A web application framework for Python.
    '''),

    Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

- The `app` object is created by calling the `dash.Dash()` constructor.
- We the DOM tree assign to `app.layout`
  - The tree is created using HTML and Dash components
  - Here, the `Graph` object creates a Plotly visualization
- Finally, we start the app with `app.run_server()`  

## 1. Layout

- Dash provides Python classes for all visual **components** of an application. Each component is described entirely through keyword attributes.
- Components are sourced from the `dash_core_components` and the `dash_html_components` modules
  - A DOM tree can be constructed using these components and assigned to `app.layout`
  - The `children` property of each component accepts Python objects (like strings, numbers) or other components.

### HTML Components

This module  contains a component class for every HTML tag as well as keyword arguments for all of the HTML arguments. The `html.H1(children='Hello World')` component generates a `<h1>Hello World</h1>` HTML element in your application.

```
A           Blockquote    Del         Form        Ins         Multicol    Progress    Source     Thead
Abbr        Br            Details     Frame       Isindex     Nav         Q           Spacer     Time
Acronym     Button        Dfn         Frameset    Kbd         Nextid      Rb          Span       Title
Address     Canvas        Dialog      H1          Keygen      Nobr        Rp          Strike     Tr
Area        Caption       Div         H2          Label       Noscript    Rt          Strong     Track
Article     Center        Dl          H3          Legend      ObjectEl    Rtc         Sub        U
Aside       Cite          Dt          H4          Li          Ol          Ruby        Summary    Ul
Audio       Code          Element     H5          Link        Optgroup    S           Sup        Var
B           Col           Em          H6          Listing     Option      Samp        Table      Video
Base        Colgroup      Embed       Header      Main        Output      Script      Tbody      Wbr
Basefont    Command       Fieldset    Hgroup      MapEl       P           Section     Td         Xmp
Bdi         Content       Figcaption  Hr          Mark        Param       Select      Template   version
Bdo         Data          Figure      I           Marquee     Picture     Shadow      Textarea
Big         Datalist      Font        Iframe      Meta        Plaintext   Slot        Tfoot
Blink       Dd            Footer      Img         Meter       Pre         Small       Th
```

These are constructed with the following essential parameters

- `children`: a _list_ of, or singular dash component from `dash_html_components` or `dash_core_components`
- `id`: a _string_ used to identify dash components in callbacks, must be unique across components
- `style`: a _dict_ used to apply in-line CSS styles through {`css-propery`: value} pairs
- `className`: a _string_ used with CSS to style the element

### Core components

These are higher-level components that are interactive and are generated with JavaScript, HTML, and CSS through the React.js library.

```
Checklist                   Interval              SyntaxHighlighter
ConfirmDialog               Link                  Tab
ConfirmDialogProvider       Location              Tabs
DatePickerRange             Markdown              Textarea
DatePickerSingle            RadioItems            Upload
Dropdown                    RangeSlider           version
Graph                       Slider
Input                       Store
```

The `Graph` object is used for constructing data visualizations using `plotly.js`. Available events include 'click', 'hover', 'selected', 'relayout', 'unhover'. The constructor takes the following arguments

- `figure`: Plotly.js `figure` object (or a Python callable), a _dict_ with `data` (list of dicts) and `layout` (dict)
- `config`: Plotly.js config options, a _dict_ with keys like `staticplot`, `editable`,
- `id`: string, a unique id used to identify the component in callbacks
- `className`
- `style`

### Custom CSS and JS

Custom CSS (and JS) scripts should be put inside an `/assets` directory living alongside `app.py`
  - All `.css` and `.js` files in this directory will be automatically included
  - Your custom CSS will be included after the Dash component CSS
  - Components can then be styled by using the `className` parameter, or in-line with the `style` argument.
    - Note: The keys in the `style` dictionary are _camelCased_. So, instead of 'text-align', it's 'textAlign'.
  - CSS and JS scripts can also be sourced from a URL by using the `assets_external_path=list('<URL-to-assets>')` in the `dash.Dash()` constructor.
