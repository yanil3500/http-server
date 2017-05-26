"""Tests for the echo server."""
# -*- coding: utf-8 -*-
import pytest
import sys

PARAMETERS_FOR_CLIENT = [
    ('the quick brown fox jumped over the lazy dog!', 'the quick brown fox jumped over the lazy dog!'),
    ('the man, a plan, and panama!', 'the man, a plan, and panama!'),
    ('a!', 'a!'),
    ('!', '!'),
    ('1234567!', '1234567!'),
    ('#()@#%^&!', '#()@#%^&!'),
    ('®!', '®!')
]


@pytest.mark.parametrize('message, result', PARAMETERS_FOR_CLIENT)
def test_start_client(message, result):
    """Check to make sure the message the client receives is the same as the one it sent."""
    from client import start_client
    assert start_client(message) == result

