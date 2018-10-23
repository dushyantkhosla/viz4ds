from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
import sqlite3
import altair as alt
import pandas as pd

external = {
    'stylesheet': "https://unpkg.com/tachyons@4.10.0/css/tachyons.min.css",
    'scripts': ['https://cdn.jsdelivr.net/npm/vega@3',
                'https://cdn.jsdelivr.net/npm/vega-lite@2',
                'https://cdn.jsdelivr.net/npm/vega-embed@3']
    }

# Import data
conn = sqlite3.connect('altair.db')
list_tables = [x[0] for x in conn.cursor().execute('select name from sqlite_master where type="table"').fetchall()]

df = pd.read_sql('select * from cars', con=conn)

chart = alt.Chart(df).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chart-1.html',
                           page_title='An Altair Plot',
                           css=external['stylesheet'],
                           js=external['scripts'],
                           chart_as_json=json.loads(chart.to_json()),
                           chart_id='scatter-01'
                           )

if __name__ == '__main__':
    app.run(debug=True)
