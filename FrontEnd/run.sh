#!/bin/bash

# A Simple script for building and running the Docker Image

# Build the Docker Image
docker build -t pythonwebapp-frontend .

# Run the Docker Image in the background
docker run -p 80:80 -d pythonwebapp-frontend

