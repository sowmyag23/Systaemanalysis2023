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
