# A Simple Dockerfile for hosting the backend of the PythonWebApp

# Use the official Python image
FROM python:3.7

ARG mock="" # No MOCK by default

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD src /app

ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py",${mock}]

