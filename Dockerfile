# Base image: Alpine Linux with Python 3.6 preinstalled.
FROM python:3.6-alpine

# Specify the working directory for commands that get run in the
# container.
WORKDIR /app

# Copy everything from our project into the container.
COPY . /app

# Run a pip install on the container.
RUN pip install --trusted-host pypi.python.org .

# Set an environment variable.
ENV NAME "Docker"

# Tell Docker that this container will expose a service on port 5000.
EXPOSE 5000

# Specify the command that the container will run when it starts.
CMD ["python", "app.py"]
