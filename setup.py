from setuptools import setup

tests_require = ['pytest', 'pytest-docker-compose']

setup(
    name='hello-pytest-docker-compose',
    description='Small app for getting acquainted with pytest-docker-compose',
    url='https://github.com/BlockchainLabsNZ/hello-pytest-docker-compose',

    version='1.0.0',

    install_requires=['klein', 'redis'],
    extras_require={'test-runner': tests_require,},

    setup_requires=['pytest-runner'],
    tests_require=tests_require,

    author='Phoenix Zerin',
    author_email='phoenix@blockchainlabs.nz',
)
