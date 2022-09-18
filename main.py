# this is my main filei
import server 
import weather
import flask

def main():
    weather.weather_data.get_weather_data()
    server.server_class.make_server()


if __name__ == '__main__':
    main()