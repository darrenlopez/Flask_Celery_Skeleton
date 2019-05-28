# Flask Celery Skeleton

This project was designed to easily deploy flask projects using docker leveraging celery and rabbitmq. This is simply to cut down time in the future for development by having a simple project skeleton ready for plug and build.  

## Getting Started

Set up a Sentry account to maintain error logging, in the settings.py file, simply add sentry token. Sentry is free on a base account.

## Architecture

The architecture of this project was standard to the python/flask documenetation. Only thing to look for is that the celery tasks are added in the exchange directory.

## Prerequisites

Installing Docker on the machine that is in use. Go to website and install the software, and then run the docker commands to build the software.

## Deployment

To Build this project, the machine must have Docker installed. To build, change into the file directory, and run the following command:

```
docker-compose up --build
```

This command will build the containers, and once loaded, simply going to http://localhost:5000/, and will display a simple "Hello World", this route can be easily removed and this project can have the celery worker simply make requests and pull data into a DB or routes can be added to make this a proper API.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Celery](http://www.celeryproject.org/) - Asynchronous task queue
* [Docker](https://www.docker.com/) - Development and delivery of software inside standardized containers.

## Authors

* **Darren Lopez** - *Engineer* - [github](https://github.com/darrenlopez)

## Acknowledgments

* The structure of this code was from a project I had previously built.
* Inspiration for the architecture was Asynchronous deployment.
