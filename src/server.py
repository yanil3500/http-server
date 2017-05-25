# -*- coding: utf-8 -*-
"""Server for http server assignment."""
from __future__ import unicode_literals
import socket
import sys


def main():  # pragma: no cover
    """Main server loop. Logs data into log variable until it finds a certain character. Then returns response."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5105)
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
            URI = parse_request(log.decode('utf8'))
            response = response_ok(URI)
            connection.sendall(response)
            connection.close()
        except KeyboardInterrupt:
            server.shutdown(socket.SHUT_WR)
            server.close()
            sys.exit(0)


def response_ok(URI):  # pragma: no cover
    response = b'HTTP/1.1 200 OK \r\n\r\nDate: ' 'Content-Type: text/plain \r\n\r\n'
    """Returns 200 response."""
    return response

def response_error(error_code):
    # Idea for switch dictionary: https://www.pydanny.com/why-doesnt-python-have-switch-case.html
    """Returns 500 response."""
    switch_dict = {
        505: "HTTP/1.1 505 HTTP Version Not Supported \r\nContent-Type: text/plain \r\n\r\n",
        501: "HTTP/1.1 501 Method Not Implemented \r\nContent-Type: text/plain \r\n\r\n",
    }
    return switch_dict.get(error_code, "HTTP/1.1 400 Bad Request \r\nContent-Type: text/plain \r\n\r\n")


def parse_request(request):
    """
    responsible for parsing http requests
    """
    print('before split'.format(request))
    words = request.split()
    parts_of_request = ['GET', 'http/1.1', 'HOST:']
    request_switch_dict = {
        'GET': 501,
        'http/1.1': 505,
        'HOST:': 400
    }

    if len(words) is not 5:
        raise Exception(request_switch_dict.get(len(words), 400))
    if words[0] != parts_of_request[0]:
        raise Exception(response_error(request_switch_dict.get(parts_of_request[0])))
    elif words[2] != parts_of_request[1]:
        raise Exception(response_error(request_switch_dict.get(parts_of_request[1])))
    elif words[3] != parts_of_request[2]:
        raise Exception(response_error(request_switch_dict.get(parts_of_request[2])))
    else:
        return words[1].encode('utf8')


if __name__ == '__main__':  # pragma: no cover
    main()



    #"GET /index.html HTTP/1.1\r\nHost: www.example.com"
# GET /path/to/index.html HTTP/1.0<CRLF>
# <CRLF>
    #message.decode('utf8').endswith(\r\n\r\n):
        #flag = False
    #also maybe some logic to ensure is a proper request?
    #IDK maybe not.