import io
import urllib, base64
from shapely.geometry import Point
from flask import Response
from adjustText import adjust_text
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from flask import Flask, send_file, render_template, request

from twitter_tools import get_friends

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    screen_name = request.form['text']
    friends = get_friends(screen_name)
    friends = pd.DataFrame(friends)
    geometry = [Point(xy) for xy in zip(friends.longitude, friends.latitude)]
    gdf = gpd.GeoDataFrame(friends, geometry=geometry)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = gdf.plot(ax=world.plot(figsize=(20, 9)), marker='o', color='red', markersize=25)
    texts = []
    for x, y, label in zip(gdf.longitude, gdf.latitude, gdf.screen_name):
        texts.append(ax.text(x, y, label, horizontalalignment='center', color='r'))
    adjust_text(texts)
    buf = io.BytesIO()
    ax.figure.savefig(buf, format='jpg', dpi=400)
    buf.seek(0)

    return send_file(buf, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
