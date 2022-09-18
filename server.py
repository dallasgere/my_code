# this file will launch my web server
import flask
import weather
import os
#import weather.py

class server_class:

    # this is my function to make a server
    def make_server():

        app = flask.Flask(__name__)
        @app.route('/')
        def index():
            moon = weather.weather_data.get_weather_data()
            return flask.render_template(
                "index.html",
                send_moon = moon
            )

        app.run(
            debug = True
        )