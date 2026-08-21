"""Retry backoff helpers."""

BASE_DELAY = 0.5
MAX_DELAY = 30.0
RETRYABLE = (429, 500, 502, 503, 504)


def backoff(attempt):
    """Seconds to wait before retry number `attempt`, capped at MAX_DELAY."""
    if attempt < 0:
        attempt = 0
    delay = BASE_DELAY * (2 ** attempt)
    return min(delay, MAX_DELAY)


def should_retry(status):
    """Whether an HTTP status code is worth another attempt."""
    return status in RETRYABLE
