# Use the official Python 3.13.2 slim image
FROM python:3.13.2-slim

# Set the working directory inside the container
WORKDIR /app

# Ensure output is not buffered
ENV PYTHONUNBUFFERED=1

# Default command to run the script (will be relative to the working directory set via the run command)
CMD ["python", "main.py"]