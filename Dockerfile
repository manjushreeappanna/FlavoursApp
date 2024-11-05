# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY cho/ /app

# Install any dependencies specified in requirements.txt
RUN pip install flask sqlalchemy

# Expose the port that Flask uses (default is 5000)
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
