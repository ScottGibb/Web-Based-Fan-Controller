# Web Based Fan Controller

[![Build and Test Docker](https://github.com/ScottGibb/Web-Based-Fan-Controller/actions/workflows/docker.yml/badge.svg)](https://github.com/ScottGibb/Web-Based-Fan-Controller/actions/workflows/docker.yml)[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)


## Summary

This project contains a very simple web based application for controlling a Fan. This was my first time creating a web app and as such is not the best app ever built. However it was done as an educational project to explore different aspects of web development. The project consists of both a backend and frontend component. The backend is written in Python and uses the Flask framework. The frontend is written in HTML and CSS and uses Bootstrap for styling. The backend and frontend are packaged together in a Docker compose file, the system is designed to run on a raspberry pi. However the frontend docker container can be moved to a seperate server if desired.


## Architecture

The architecture of the system is as follows:


## Installation

### Update Pins

Firstly, navigate to the `PythonWebApp/BackEnd/src` directory and open the `app.py` file. In this file you will need to update the constructor of FanController to the pins you have connected the fan to. The pin number should be the BCM pin number.

Once this is completed, save the file and close it.

### Build Docker Images through Docker Compose

Next, navigate to the `PythonWebApp` directory and run the following command:

```bash
docker-compose up -d --build
```

After this the docker image will be built and the containers will be started. The web app should now be accessible at `http://localhost:8000`.

### Build and run Docker Images Manually

Alternatively, you can build the docker images manually. To do this, navigate to the `PythonWebApp/BackEnd` directory and run the following command:

```bash
sh run.sh
```

The same can be done for the frontend by navigating to the `PythonWebApp/FrontEnd` directory and running the following command:

```bash
sh run.sh
```

## Useful Links

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Bootstrap](https://getbootstrap.com/)
- [Docker](https://www.docker.com/)
