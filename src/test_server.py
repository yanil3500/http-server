# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Testing for the http server assignment"""
import pytest


PARAMETERS = [
    ("GET /webroot/sample.txt HTTP/1.1\r\n\r\nHost: www.hostythehostess.gov:80\r\n\r\n", ['HTTP/1.1', '200', 'OK'])
]
PARAMETERS_FOR_PARSE_REQUEST_RAISE_ERROR = [
    ("GsdT /INDEX.HTML HTTP/1.1\r\n\r\nHost: www.hostythehostess.gov:80\r\n\r\n", "HTTP/1.1 501 Method Not Implemented \r\nContent-Type: text/plain \r\n\r\n"),
    ("GET /INDEX.HTML HTTP/1.2\r\n\r\nHost: www.hostythehostess.gov:80\r\n\r\n", "HTTP/1.1 505 HTTP Version Not Supported \r\nContent-Type: text/plain \r\n\r\n"),
    ("GET /INDEX.HTML HTTP/1.1\r\n\r\nH123T: www.hostythehostess.gov:80\r\n\r\n", "HTTP/1.1 400 Bad Request \r\nContent-Type: text/plain \r\n\r\n"),
    ("GET /webroot/a_web_page_that_does_not_exist.html HTTP/1.1\r\n\r\nHost: www.hostythehostess.gov:80\r\n\r\n", "HTTP/1.1 404 Not Found \r\nContent-Type: text/plain \r\n\r\n")

]


@pytest.mark.parametrize('http_request, response', PARAMETERS_FOR_PARSE_REQUEST_RAISE_ERROR)
def test_parse_request_raise_error(http_request, response):
    """Tests all error types from the server."""
    from client import start_client
    assert start_client(http_request) == response

@pytest.mark.parametrize('http_request, response', PARAMETERS)
def test_parse_request_raise_error(http_request, response):
    """Tests a properly formatted GET request, looking for a 200 response."""
    from client import start_client
    assert start_client(http_request).split(' ')[:3] == response
