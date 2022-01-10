#importing modules
#Reference Baseline YT video: https://www.youtube.com/watch?v=7ffhyoYZz9E&list=PLe1T0uBrDrfOuXNGWSoP5KmRIN_ESkCIE
import time
import json
from kafka import KafkaProducer
import requests

topic_name = 'weather_topic'


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],request_timeout_ms=1000000,
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'), api_version=(0, 10, 1))

openweather_api_link = None
message = None
latitude = None
longitude = None
temperature_max = None
temperature_min = None
humidity = None
appid = None

#function to get the data from the city via openweather api
def fetch_city_data(openweather_api_link):
    api_response = requests.get(openweather_api_link)
    data = api_response.json()
    humidity = data['main']['humidity']
    temperature_max = data['main']['temp_max']
    temperature_min = data['main']['temp_min']
    message = {"Latitude": latitude, "Longitude": longitude, "Temp(Max)": temperature_max,"Temp(Min)": temperature_min, "Humid": humidity, "TimeStamp": time.strftime("%Y-%m-%d %H: %M: %S")}
    return message 


#function to get app id
def get_appid(appid):...


while True:
    # Miami : 25.7617° N, 80.1918° W
    longitude = "25.7617"
    latitude = "80.1918"
    #app id : created and fetched from https://home.openweathermap.org/api_keys
    appid = "a80f229fdd72fbc17764e91b4733498a"
    openweather_api_link = "http://api.openweathermap.org/data/2.5/weather?&appid=" + appid + "&lat=" + latitude + "&lon=" + longitude
    weather_data = fetch_city_data(openweather_api_link)
    #weather_data = fetch_city_data('http://api.openweathermap.org/data/2.5/weather??q=Kolkata&appid=a80f229fdd72fbc17764e91b4733498a')
    #sending the data
    print(weather_data)
    producer.send(topic_name, weather_data)
    print("Message Published Successfully!")
    print("Message ::" +json.dumps(weather_data))
    print("Refresh time :: 1 second")
    time.sleep(1)
