import os
import socket

from flask import Flask
from redis import Redis, RedisError


def increment_counter(redis_client: Redis) -> int:
    """
    Increments the page hits counter and returns the new count.
    """
    try:
        return redis_client.incr("counter")
    except RedisError:
        return 0


app = Flask(__name__)


@app.route("/")
def hello():
    """
    Displays the number of page hits.
    """
    visits = (
            increment_counter(redis)
            or "<i>cannot connect to Redis, counter disabled</i>"
    )

    html = (
        "<h3>Hello {name}!</h3>"
        "<b>Hostname:</b> {hostname}<br/>"
        "<b>Visits:</b> {visits}"
    )

    return html.format(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        visits=visits,
    )


@app.route("/health_check")
def health_check():
    """
    Used to verify that the app is up and running.
    """
    return "ok"


if __name__ == "__main__":
    # Connect to the Redis container.  The hostname must match the name
    # of the corresponding service in ``docker-compose.yml``.
    redis = Redis("redis", db=0, socket_timeout=2, socket_connect_timeout=2)

    # Listen for incoming connections on port 80.
    # Note that we map this to port 5000 in ``docker-compose.yml``, so
    # that we can access the webapp by going to http://localhost:5000/
    app.run(host="0.0.0.0", port=80)
