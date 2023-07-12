from flask import Flask
from os import environ
from pymongo import MongoClient
import requests
import json
from datetime import datetime, timedelta

app = Flask(__name__)
listen_port = environ.get("HTTP_PORT")
db_name = environ.get("DB_NAME")
update_interval = int(environ.get("UPDATE_INTERVAL", 3600))
weather_location = environ.get("WEATHER_LOCATION")

def main():
    weatherdb = connect_database()
    print(f"Database: {weatherdb.name}")
    start_http()
    update_weather_data(weatherdb)

def connect_database():
    if db_name is None:
        print("Must set DB_NAME in environment")
        exit(1)
    client = MongoClient("mongodb", 27017)
    print(client.server_info())
    return client[db_name]

def update_weather_data(db):
    while true:
    weather_data=retrieve_weather_data()
    store_weather_data(db, weather_data)
    sleep(update_interval)

def retrieve_weather_data():
    api_key="7050ff93230770172103ab380dbcc811"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid={7050ff93230770172103ab380dbcc811}"
    response=requests.get(url)
    if response.status_code==200:
        weather_data=response.json()
       return weather_data
    else:
        print("Error retrieving weather data")
        return None

def store_weather_data(db, weather_data):
    if weather_data is not None:
        collection = db["weather"]
        collection.insert_one(weather_data)

def calculate_statistics(weather_data_list):
    temperatures = [data['main']['temp'] for data in weather_data_list]
         pressures = [data['main']['pressure'] for data in weather_data_list]

         avg_temperature = sum(temperatures) / len(temperatures)
         min_temperature = min(temperatures)
         max_temperature = max(temperatures)

         avg_pressure = sum(pressures) / len(pressures)
         min_pressure = min(pressures)
         max_pressure = max(pressures)

    statistics = {
        "avg_temperature": avg_temperature,
        "min_temperature": min_temperature,
        "max_temperature": max_temperature,
        "avg_pressure": avg_pressure,
        "min_pressure": min_pressure,
        "max_pressure": max_pressure,
    }

    return statistics

@app.route('/weather')
def get_weather():
    db = connect_database()
    collection = db["weather"]

    past_24_hours = datetime.now() - timedelta(hours=24)
    weather_data_list = list(collection.find({"timestamp": {"$gte": past_24_hours}}))

    if len(weather_data_list) > 0:
        statistics = calculate_statistics(weather_data_list)
        return jsonify(statistics)
    else:
        return "No weather data available."
       
def start_http():
    global listen_port
    if listen_port is None:
        listen_port = "3333"
    @app.route('/')
    def index():
        return 'Hello World'
    app.run(host='0.0.0.0', port=int(listen_port))

if __name__ == "__main__":
    main()
