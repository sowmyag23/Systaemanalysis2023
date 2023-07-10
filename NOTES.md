# Dockernotes

## Building the image

A command such as `docker build -t image_name:latest .` can be run to prepare the image.

The image can be listed with `docker image ls`

## Running the image

The important arguments are:
* `--name` give the image a name
* `-p 3333:3333` forward local port into the container
* `-d` Run in the background
* `imagename:tagname` the image to run

To run the image, the following command can be executed:
```sh
% docker run -d --name some_container -p 3333:3333 myimage1:latest
```
## Docker-Compose.yml

Docker Compose is used when we want to run more than 1 container under a service
In the given `docker-compose.yml` file there are two containers under a service (Frontend-web server, mongodb-database)
The name of the db is `weather_stats` and frontend depends on mongodb for getting data
The port 8888:3333 is host to container mapping to access on the web browser
For the mongodb we have used the image called mongo with latest version
