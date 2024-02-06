# backend.py
from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta
import time
import requests

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb://mongo:27017/')
db = client['weather']

# OpenWeatherMap API key
api_key = '7050ff93230770172103ab380dbcc811'
default_city = 'Fort Wayne'

def fetch_and_store_weather():
    while True:
        # Calculate timestamp for the current time
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Fetch weather data from OpenWeatherMap for the default city
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={default_city}&appid={api_key}'
        response = requests.get(weather_url)
        weather_data = response.json()

        # Store weather data in MongoDB with timestamp
        db.weather_data.insert_one({'timestamp': timestamp, 'data': weather_data})

        print(f"Weather data fetched and stored at {timestamp}")

        # Sleep for 10 minutes before fetching again
        time.sleep(10 * 60)

# Endpoint to get the latest weather data from MongoDB
@app.route('/latest_weather')
def get_latest_weather():
    # Fetch the latest stored weather data from MongoDB
    latest_data = db.weather_data.find_one(sort=[('_id', -1)])
    return jsonify(latest_data['data'])

if __name__ == '__main__':
    # Start a separate thread to fetch and store weather data
    import threading
    threading.Thread(target=fetch_and_store_weather).start()

    # Run the Flask app for the backend on port 5001
    app.run(debug=True, host='0.0.0.0', port=5001)

