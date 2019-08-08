from setuptools import setup

tests_require = ['pytest', 'pytest-docker-compose']

setup(
    name='hello-docker',
    description='Example app showing how to use Docker.',
    url='https://docs.docker.com/get-started/',

    version='1.0.0',

    install_requires=['flask', 'redis'],
    extras_require={'test-runner': tests_require,},

    setup_requires=['pytest-runner'],
    tests_require=tests_require,

    author='Phoenix Zerin',
    author_email='phx@phx.ph',
)
