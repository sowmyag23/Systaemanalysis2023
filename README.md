# Flask Weather Application
This project is a Flask web application that serves as a simple weather information API.  Developed a code file ‘app.py’ in  python for weather data using Flask Framework
The /weather is used to accept the HTTP GET requests and fetches the data from OpenWeatherMap API based on the provided city
The application runs on host 0.0.0.0 and port ‘5001’ when executed.

Built a docker file ‘appdockerfile’ for the code.
Copies ‘app.py’ and ‘requirements.txt’ into the container
Exposes port ‘5001’ to allow external access to flask app

Requirements file contains python packages and versions required for flask application
Flask(2.0.1), requests(2.26.0) and Werkzeug(2.0.2)  are specified with their versions.

running at [http://localhost](http://localhost:5001/weather?city=Fort%20Wayne)http://localhost:5001/weather?city=Fort%20Wayne
