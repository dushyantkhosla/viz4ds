import sqlite3
import datetime
import pandas as pd
from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.embed import components

def sql_to_df(db, table_name):
    '''
    Fetch table_name from database db into a Pandas DataFrame
    '''
    conn = sqlite3.connect(db)
    df = pd.read_sql(sql=f"select * from {table_name}", con=conn)
    df.loc[:, 'time'] = pd.to_datetime(df['time'])
    return df

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart')
def chart():
    '''
    Create a Bokeh Figure object, add glyphs
    Export components of Figure as html, css and js resources
    '''
    df = sql_to_df(db='greenhouse.db', table_name='greenhouse')

    p = figure(plot_width=800,
               plot_height=300,
               x_axis_type='datetime')

    p.line(x=df.index.values,
           y=df['temp'].values,
           line_width=2)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    script, div = components(p)

    return render_template('chart.html',
                           page_title='Temperature over Time',
                           plot_script=script,
                           plot_div=div,
                           js_resources=js_resources,
                           css_resources=css_resources)


if __name__ == '__main__':
    app.run(debug=True)
