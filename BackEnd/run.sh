# Simple Script for building and running the Docker Image

# Build the Docker Image
docker build -t pythonwebapp-backend .

# Run the Docker Image

# Run the Docker Image in the background

if[$# -eq 0]; then
    docker run -p 5000:5000 -d pythonwebapp-backend
else
    docker run -p 5000:5000 -d -e MOCK=$1 pythonwebapp-backend 
fi
