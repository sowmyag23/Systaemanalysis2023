from os import environ
from pymongo import MongoClient
import requests
import time

db_name = environ.get("DB_NAME")
update_interval = int(environ.get("UPDATE_INTERVAL", 3600))
weather_location = environ.get("WEATHER_LOCATION")

def main():
    weatherdb = connect_database()
    print(f"Database: {weatherdb.name}")
    update_weather_data(weatherdb)

def connect_database():
    if db_name is None:
        print("Must set DB_NAME in environment")
        exit(1)
    client = MongoClient("mongodb", 27017)
    print(client.server_info())
    return client[db_name]

def update_weather_data(db):
    while True:
        print("Weather Data Updated")
        weather_data=retrieve_weather_data()
        store_weather_data(db, weather_data)
        time.sleep(update_interval)

def retrieve_weather_data():
    api_key="7050ff93230770172103ab380dbcc811"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid={api_key}"
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

if __name__ == "__main__":
    main()
