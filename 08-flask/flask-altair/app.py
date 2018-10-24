from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
import sqlite3
import altair as alt
import pandas as pd

# Import data
conn = sqlite3.connect('altair.db')
cars = pd.read_sql('select * from cars', con=conn, index_col='index')

# ===== Chart 1 =====
chart_1 = alt.Chart(data=cars).mark_circle(size=60).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
).interactive()

# ===== Chart 2 =====
brush = alt.selection(type='interval')

points = alt.Chart().mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart().mark_bar().encode(
    y='Origin:N',
    color='Origin:N',
    x='count(Origin):Q'
).transform_filter(
    brush
)

chart_2 = alt.vconcat(points, bars, data=cars)

# ===== Payload for Jinja =====
payload_ = [
    {
        'chart_as_json': json.loads(chart_1.to_json()),
        'div_id': 'scatter-01',
        'div_class': 'pa4 bb'
        },
    {
        'chart_as_json': json.loads(chart_2.to_json()),
        'div_id': 'scatter-02',
        'div_class': 'center pa4'
        }
    ]

# ===== Start App, deliver payload =====
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           payload=payload_)

if __name__ == '__main__':
    app.run(debug=True)
