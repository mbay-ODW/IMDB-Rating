#!/usr/bin/python3
# coding=utf-8
from flask import Flask, flash, request, redirect, render_template, send_file, Response, abort
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import io
import random
import logging
import base64
from io import BytesIO
import requests
import json
from flask import Response
import time
import urllib.parse
import os

token = os.getenv("TOKEN", default="k_123456789")
app = Flask(__name__,static_url_path='/static')
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
app.config['DEBUG'] = True

logger = logging.getLogger('Server Logging')
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info('Logger for Upload Server was initialized')



@app.route('/home', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('./home.html')
    else:
        abort(403)


@app.route('/result',methods=['POST'])
def plot_png():
    if request.method == 'POST':
        try:
            title = urllib.parse.quote(request.form["title"])
            url = f'https://imdb-api.com/en/API/SearchSeries/{token}/{title}'
            payload = {}
            headers= {}
            response = requests.request("GET", url, headers=headers, data = payload)
            result = json.loads(response.text.encode('utf8'))
            if result["errorMessage"] == "Invalid API Key":
                flash("Incorrect API key")
                return redirect('/home')
            if not result["results"]:
                flash("No Serieses found")
                return redirect('/home')
            imDbId = result["results"][0]["id"]
            logger.debug(request.args)
            logger.debug(title)
            # Generate the figure **without using pyplot**.
            fig = Figure()
            ax = fig.subplots()
            season = 1
            allRatings = []
            while True:
                url = f'https://imdb-api.com/en/API/SeasonEpisodes/{token}/{imDbId}/{season}'
                payload = {}
                headers= {}
                response = requests.request("GET", url, headers=headers, data = payload)
                array = {}
                ratings = {}
                array = json.loads(response.text.encode('utf8'))
                logger.debug(array)
                if not array["episodes"]:
                    try:
                        # No more seasons left
                        logger.debug("Breaking the loop")
                        # Creating overall Trend
                        trend_x, p = create_trend(y)
                        ax.plot(trend_x,p(trend_x),"r--")
                    except:
                        pass
                    finally:
                        break
                for i in array["episodes"]:
                    ratings[f'S{season}E{i["episodeNumber"]}'] = i["imDbRating"]
                episodeNumber = []
                rating = []
                for i in ratings:
                    episodeNumber.append(i)
                    rating.append(float(ratings[i]))
                    # Collecting all episodes and ratings for overall trend
                    allRatings.append(float(ratings[i]))
                x = episodeNumber
                y = rating
                mean = sum(rating)/len(rating)
                trend_x, p = create_trend(y)
                ax.plot(trend_x,p(trend_x),"r--")
                if season%2:
                    ax.plot(x,y,x,y,"or")
                else:
                    ax.plot(x,y,x,y,"oy")
                ax.hlines(mean,x[0],x[-1])
                season += 1
            
            # Save it to a temporary buffer.
            buf = BytesIO()
            fig.savefig(buf, format="png")
            # Embed the result in the html output.
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return f"<img src='data:image/png;base64,{data}'/>"
        except Exception as e:
            flash(f'The following error occured: {e}')
            return redirect('/home')
    else:
        return redirect('/home')

def create_trend(y):
            a = []
            for i in range(len(y)):
                a.append(i)
            trend_x = np.array(a)
            trend_y = np.array(y)
            trend = np.polyfit(trend_x, trend_y, 1)
            p = np.poly1d(trend)
            return trend_x, p

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
