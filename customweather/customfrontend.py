# frontend.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Endpoint to get the latest weather data from the backend
@app.route('/')
def get_weather():
    # Connect to the backend to fetch the latest weather data
    backend_url = 'http://localhost:5001/latest_weather'
    response = requests.get(backend_url)
    weather_data = response.json()

    return jsonify(weather_data)

if __name__ == '__main__':
    # Run the Flask app for the frontend on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)

