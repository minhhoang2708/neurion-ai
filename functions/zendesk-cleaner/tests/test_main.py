import pytest
from functions.zendesk-cleaner.main import handler

def test_handler_basic():
    event = {}
    context = None
    result = handler(event, context)
    assert result is not None
