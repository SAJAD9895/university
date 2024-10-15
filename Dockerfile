# Use the official Python image from the Docker Hub
# FROM python:3.12.7
FROM python:3.10

# Set the working directory in the container
WORKDIR /students

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Collect static files (if you're using Django's static files)
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on (default for Django is 8000)
EXPOSE 8000

# Command to run your app using Gunicorn (a WSGI server for Python)
CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
