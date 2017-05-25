# -*- coding: utf-8 -*-
"""Server for http server assignment."""
from __future__ import unicode_literals
from email.utils import formatdate
import socket
import sys
import os

"<div>hello</div>"

CURRENT_PATH = '../src'

def main():  # pragma: no cover
    """Main server loop. Logs data into log variable until it finds a certain character. Then returns response."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5215)
    server.bind(address)
    server.listen(1)
    while True:
        try:
            connection, address = server.accept()
            log = b""
            flag = True
            while flag is True:
                more = connection.recv(8)
                log += more
                if log.decode('utf8').endswith('\r\n\r\n'):
                    flag = False
            sys.stdout.write(log.decode('utf8'))
            URI = parse_request(log.decode('utf8'), connection)
            content = resolve_uri(URI, connection)
            response = response_ok(content)
            connection.sendall(response.encode('utf8'))
            connection.close()
        except KeyboardInterrupt:
            server.shutdown(socket.SHUT_WR)
            server.close()
            sys.exit(0)

# foo.jpeg - Content-Type: image/jpeg
# foo.png - Content-Type: image/png
# bar.txt - Content-Type: text/plain
# baz.html - Content-Type: text/html

def response_ok(body_response):  # pragma: no cover 
    content, file_size, content_type = body_response
    today_date = str(formatdate(usegmt=True))
    response = 'HTTP/1.1 200 OK \r\nDate: {}\r\nContent-Length: {}\r\nContent-Type: {}\r\n\r\n{}\r\n\r\n'.format(today_date, file_size, content_type, content)
    """Returns 200 response."""
    print(response)
    return response


def resolve_uri(URI, connection):
    file_path = os.path.join(CURRENT_PATH, URI[1:])
    print(file_path)
    type_of_file = file_path.split('.')[-1]
    content_type_switcher = {
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'txt': 'text/plain',
        'html': 'text/html',
        'py': 'text/python',
        'directory': 'directory'
    }
    if os.path.isdir(file_path):
        content = os.listdir(os.path.join(os.getcwd(), file_path))
        type_of_file = 'directory'
        file_size = 0
    elif os.path.isfile(file_path) and URI is not '.' or '..':
        content = open(file_path).read()
        file_size = os.path.getsize(file_path)
    else:
        raise Exception(response_error(404, connection))
    return (content, file_size, content_type_switcher[type_of_file])


def response_error(error_code, connection):
    # Idea for switch dictionary: https://www.pydanny.com/why-doesnt-python-have-switch-case.html
    """Returns 500 response."""
    switch_dict = {
        505: "HTTP/1.1 505 HTTP Version Not Supported \r\nContent-Type: text/plain \r\n\r\n",
        501: "HTTP/1.1 501 Method Not Implemented \r\nContent-Type: text/plain \r\n\r\n",
        400: "HTTP/1.1 400 Bad Request \r\nContent-Type: text/plain \r\n\r\n",
    }
    response = switch_dict.get(error_code, "HTTP/1.1 404 Not Found \r\nContent-Type: text/plain \r\n\r\n")
    connection.sendall(response.encode('utf8'))
    return response


def parse_request(request, connection):
    """
    responsible for parsing http requests
    """
    words = request.split()
    parts_of_request = ['GET', 'HTTP/1.1', 'Host:']
    request_switch_dict = {
        'GET': 501,
        'http/1.1': 505,
        'HOST:': 400
    }
    if words[0] != parts_of_request[0]:
        raise Exception(response_error(request_switch_dict.get(parts_of_request[0]), connection))
    elif words[2] != parts_of_request[1]:
        raise Exception(response_error(request_switch_dict.get(parts_of_request[1]), connection))
    elif words[3] != parts_of_request[2]:
        raise Exception(response_error(request_switch_dict.get(parts_of_request[2]), connection))
    else:
        return words[1]


if __name__ == '__main__':  # pragma: no cover
    main()



    #"GET /index.html HTTP/1.1\r\nHost: www.example.com"
# GET /path/to/index.html HTTP/1.0<CRLF>
# <CRLF>
    #message.decode('utf8').endswith(\r\n\r\n):
        #flag = False
    #also maybe some logic to ensure is a proper request?
    #IDK maybe not.