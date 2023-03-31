
# A Simple Dockerfile for hosting the backend of the PythonWebApp

FROM raspbian/stretch

# Set the working directory to /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install build-essential -y
RUN apt-get install python3-pip -y

COPY requirements.txt /app

#RUN apt-get update
#RUN apt-get install -y build-essential
#RUN apt-get install python3-pip -y
# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir


# Copy the current directory contents into the container at /app
COPY src /app

EXPOSE 5000

ENV MOCK=""
# Run app.py when the container launches
CMD ["sh", "-c","python3 app.py $MOCK"]






