# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project directory into the container at /app
COPY web /app/web

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Run database migrations
RUN python manage.py migrate

# Expose the port that the app will run on
EXPOSE 8000

# Start the app using the Django development server
CMD gunicorn hack.wsgi:application --bind 0.0.0.0:8000
