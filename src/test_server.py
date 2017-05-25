# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Testing for the http server assignment"""
import pytest

PARAMETERS_FOR_CLIENT = [
    ('the quick brown fox jumped over the lazy dog!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n'),
    ('the man, a plan, and panama!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n'),
    ('a!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n'),
    ('!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n'),
    ('1234567!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n'),
    ('#()@#%^&!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n'),
    ('®!', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n'),
    ('GET /INDEX.HTML http/1.1\r\n\r\nHOST: www.hostythehostess.gov:80\r\n\r\n', 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n')
]

PARAMETERS_FOR_PARSE_CLIENT = [
    ("GET /INDEX.HTML http/1.1\r\n\r\nHOST: www.hostythehostess.gov:80\r\n\r\n", 'HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n')
]
PARAMETERS_FOR_PARSE_REQUEST_RAISE_ERROR = [
    ("GsdT /INDEX.HTML http/1.1\r\n\r\nHOST: www.hostythehostess.gov:80\r\n\r\n"),
    ("GET /INDEX.HTML http/1.2\r\n\r\nHOST: www.hostythehostess.gov:80\r\n\r\n"),
    ("GET /INDEX.HTML http/1.1\r\n\r\nH123T: www.hostythehostess.gov:80\r\n\r\n")

]
PARAMETERS_FOR_RESPONSE_ERROR = [
    (505, 'HTTP/1.1 505 HTTP Version Not Supported \r\nContent-Type: text/plain \r\n\r\n'),
    (501, 'HTTP/1.1 501 Method Not Implemented \r\nContent-Type: text/plain \r\n\r\n'),
    (400, 'HTTP/1.1 400 Bad Request \r\nContent-Type: text/plain \r\n\r\n')
]


@pytest.mark.parametrize('message, result', PARAMETERS_FOR_CLIENT)
def test_start_client(message, result):
    """Test if any request returns an HTTP status response."""
    from client import start_client
    assert start_client(message) == result


@pytest.mark.parametrize('status_code, response', PARAMETERS_FOR_RESPONSE_ERROR)
def test_response_error(status_code, response):
    """Test if the error function returns the correct status response."""
    from server import response_error
    assert response_error(status_code) == response


@pytest.mark.parametrize('http_request', PARAMETERS_FOR_PARSE_REQUEST_RAISE_ERROR)
def test_parse_request_raise_error(http_request):
    """
    tests to see if appropriate exceptions are raised
    """
    from server import parse_request
    with pytest.raises(Exception):
        parse_request(http_request)
