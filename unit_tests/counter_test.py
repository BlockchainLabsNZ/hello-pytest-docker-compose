from redis import Redis, TimeoutError

from app import increment_counter


def test_increment_counter_happy_path(monkeypatch, redis_client: Redis):
    """
    Successfully incrementing the counter.
    """
    def mock_incr(key):
        return 42

    monkeypatch.setattr(redis_client, "incr", mock_incr)

    assert increment_counter(redis_client) == 42


def test_increment_counter_fail(monkeypatch, redis_client: Redis):
    """
    Incrementing the counter fails.
    """
    def mock_incr(key):
        raise TimeoutError()

    monkeypatch.setattr(redis_client, "incr", mock_incr)

    assert increment_counter(redis_client) == 0
