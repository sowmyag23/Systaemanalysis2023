from flask import Flask
from os import environ
from pymongo import MongoClient

app = Flask(__name__)
listen_port = environ.get("HTTP_PORT")
db_name = environ.get("DB_NAME")

def main():
    weatherdb = connect_database()
    print(f"Database: {weatherdb.name}")
    start_http()

def connect_database():
    if db_name is None:
        print("Must set DB_NAME in environment")
        exit(1)
    client = MongoClient("mongodb", 27017)
    print(client.server_info())
    return client[db_name]

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
