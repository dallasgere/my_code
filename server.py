# this file will launch my web server
import flask
import weather
import os
import json

class server_class:

    # this is my function to make a server
    def make_server():

        app = flask.Flask(__name__)
        @app.route('/')
        def index():
            return flask.render_template("index.html")
        
        @app.route('/process_user_info/<string:user_info>', methods=['POST'])
        def process_user_info(user_info):
            user_info = json.loads(user_info)
            print()
            print("user info recieved")
            print("-------------------")
            print(f"user name: {user_info['name']}")
            print(f"user type: {user_info['type']}")
            print()
            
            return "information received!"

        app.run(
            debug = True
        )