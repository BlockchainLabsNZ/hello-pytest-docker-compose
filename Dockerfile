# Base image: Alpine Linux with Python 3.6 preinstalled.
FROM python:3.6-alpine

# Install g++ so that we can compile Twisted.
# Note that we do this before the ``COPY`` command, so that the layer
# gets cached, and we don't have to rebuild it every time we update the
# application code.
RUN apk add g++

# Specify the working directory for commands that get run in the
# container.
WORKDIR /app

# Copy everything from our project into the container.
COPY . /app

# Run a pip install on the container.
RUN pip install .

# Set an environment variable.
ENV NAME "Docker"

# Tell Docker that this container will expose a service on port 80.
EXPOSE 80

# Specify the command that the container will run when it starts.
CMD ["python", "app.py"]
