import pytest
from redis import Redis


@pytest.fixture(name="redis_client")
def fixture_redis_client():
    """
    Creates a mock Redis client for testing.
    """
    return Redis()
