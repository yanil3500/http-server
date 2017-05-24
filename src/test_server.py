# -*- coding: utf-8 -*-
"""Testing for the http server assignment"""
import pytest
import sys

PARAMETERS_FOR_CLIENT = [
    ('the quick brown fox jumped over the lazy dog!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n '),
    ('the man, a plan, and panama!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n '),
    ('a!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n '),
    ('!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n '),
    ('1234567!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n '),
    ('#()@#%^&!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n '),
    ('®!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n ')
]


@pytest.mark.parametrize('message, result', PARAMETERS_FOR_CLIENT)
def test_start_client(message, result):
    """Test if any request returns an HTTP status response."""
    from client import start_client
    assert start_client(message) == result


def test_error():
    """Test if the error function returns the correct status response."""
    from server import response_error
    assert response_error() == b"HTTP/1.1 500 Internal Server Error \r\nContent-Type: text/plain \r\n \xc2\xa7"

