Hello, pytest-docker-compose!
=============================
This is a small app for getting acquainted with the
`pytest-docker-compose plugin`_.


Deploying with Docker
---------------------
1. ``docker build -t hello-pdc .``
2. ``docker network create --driver=bridge hello-pdc``
3. ``docker run --rm --name app --net hello-pdc -d -p 5000:80 hello-pdc``

You can access the app on http://localhost:5000/ however the counter won't work
because Redis isn't running.

To spin up a Redis instance and connect the app, do the following:

1. ``docker run --rm --name redis --net hello-pdc -d redis:alpine``

Now if you go to http://localhost:5000/ you should see that the counter will now
increment as you refresh the page.

To stop the containers from running:

1. ``docker stop app redis``

For more information, refer to ``Dockerfile`` in this repository.


Deploying with docker-compose
-----------------------------
We only had to deploy two containers, but it ended up being a fair amount of
work — there were several moving parts and lots of command-line options to keep
track of!

docker-compose makes the whole process considerably easier:

1. ``docker-compose up``

This will spin up the app and redis containers and configure everything
correctly.  After running the above command, you can view the app on
http://localhost:5000/ and the counter will work straightaway.

Press Control-C to bring the containers back down.

For more information, refer to ``docker-compose.yml`` in this repository.


Running Unit Tests
------------------
.. important::
  This project was written & tested using Python 3.6 — other versions of Python
  might work, but we never tried.

1. (optional but highly recommended) Create a new virtualenv.
2. ``pip install -e '.[test-runner]'``
3. ``python setup.py test``

This runs the unit tests in ``unit_tests/counter_test.py``.  Both tests should
pass.


Running Integration Tests
-------------------------
Because integration tests take considerably longer to run, they are not enabled
by default.  Instead, you will need to use the ``pytest`` command explicitly.

*Note: the ``pytest`` command was installed when you ran ``pip install`` in the
previous step.*

1. ``docker-compose down``
2. ``pytest integration_tests/homepage_test.py``

This runs the integration tests in ``integration_tests/homepage_test.py``.  Both
tests should pass.


.. _pytest-docker-compose plugin: https://pypi.org/project/pytest-docker-compose/
