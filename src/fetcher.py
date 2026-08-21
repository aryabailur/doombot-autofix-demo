"""Small HTTP fetch helper."""

import requests

DEFAULT_TIMEOUT = 30


def _session():
    return requests.Session()


def fetch(url, timeout):
    """Fetch a URL and return its text."""
    response = _session().get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def head(url):
    """Return the response headers for a URL."""
    return _session().head(url, timeout=DEFAULT_TIMEOUT).headers
