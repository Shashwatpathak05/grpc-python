# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python files and the Protocol Buffer generated files to the container
COPY ./ ./

# Install required Python dependencies
RUN pip install grpcio grpcio-tools

# Expose the gRPC server port
EXPOSE 50051

# Start the gRPC server by default
CMD ["python", "server.py"]
