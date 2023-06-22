from flask import Flask
from os import environ

app = Flask(__name__)
listen_port = environ.get("HTTP_PORT")
if listen_port is None:
    listen_port = "3333"

@app.route('/')
def index():
    return 'Hello World'
app.run(host='0.0.0.0', port=int(listen_port))
