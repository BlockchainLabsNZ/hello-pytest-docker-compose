from requests import get

pytest_plugins = ["docker_compose"]


def test_homepage_visit_counter(homepage: str):
    """
    Loads the homepage and verifies that the counter is working.
    """
    assert get(homepage).text.endswith("<b>Visits:</b> 1")

    # Send another request, to verify the counter is working.
    assert get(homepage).text.endswith("<b>Visits:</b> 2")


def test_containers_reset_between_tests(homepage: str):
    """
    Demo showing that containers are reset between tests.
    """
    assert get(homepage).text.endswith("<b>Visits:</b> 1")
