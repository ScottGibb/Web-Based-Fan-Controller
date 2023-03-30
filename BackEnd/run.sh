# Simple Script for building and running the Docker Image

# Build the Docker Image
docker build -t pythonwebapp-backend .

# Run the Docker Image

# Run the Docker Image in the background
docker run -p 5000:5000 -d pythonwebapp-backend
