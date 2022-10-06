# this is my main filei
import server 
import weather
import flask

def main():
    '''
    this is simply my main function
    '''
    server.ServerClass.make_server()
    #moon = weather.WeatherData.get_weather_data("Austin")
    #print(moon)

if __name__ == '__main__':
    main()