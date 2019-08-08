FROM python:3.6-alpine
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org .
EXPOSE 5000
ENV NAME "Docker"
CMD ["python", "app.py"]
