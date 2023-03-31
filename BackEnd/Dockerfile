# A Simple Dockerfile for hosting the backend of the PythonWebApp

# Use the official Python image
FROM python:3.7
# Required for Raspberry Pi Builds
# FROM arm32v7/python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src /app

COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 5000

ENV MOCK=""
# Run app.py when the container launches
CMD ["sh", "-c","python app.py $MOCK"]

