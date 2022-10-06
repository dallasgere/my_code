# this file will launch my web server
import os
import weather
import flask
import json

class ServerClass:
    '''
    This is the class to make my server
    '''

    # this is my function to make a server
    def make_server():
        '''
        this is the function that will make my server, called in main
        '''

        app = flask.Flask(__name__)
        @app.route('/')
        def index():
            moon = weather.WeatherData.get_weather_data("Austin")
            return flask.render_template(
                "index.html",
                time = moon
            )
        
        # @app.route('/process_user_info/<string:user_info>', methods=['POST'])
        # def process_user_info(user_info):
        #     user_info = json.loads(user_info)
        #     print()
        #     print("user info recieved")
        #     print("-------------------")
        #     print(f"user name: {user_info['name']}")
        #     print(f"user type: {user_info['type']}")
        #     print()
            
        #     return "information received!"

        app.run(
            debug = True
        )