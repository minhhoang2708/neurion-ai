import pytest
from functions.request-consumer.main import handler

def test_handler_basic():
    event = {}
    context = None
    result = handler(event, context)
    assert result is not None
