# -*- coding: utf-8 -*-
"""Server for http server assignment."""

import socket
import sys


def main():  # pragma: no cover
    """Main server loop. Logs data into log variable until it finds a certain character. Then returns response."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5007)
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
    response = b"HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n\r\n"
    """Returns 200 response."""
    return response

def response_error(error_code):
    # Idea for switch dictionary: https://www.pydanny.com/why-doesnt-python-have-switch-case.html
    """Returns 500 response."""
    switch = {
        505: "HTTP/1.1 505 HTTP Version Not Supported \r\nContent-Type: text/plain \r\n\r\n",
        501: "HTTP/1.1 501 Method Not Implemented \r\nContent-Type: text/plain \r\n\r\n",
    }
    return switch.get(error_code, "HTTP/1.1 400 Bad Request \r\nContent-Type: text/plain \r\n\r\n")


def parse_request(request):
    """
    responsible for parsing http requests
    """
    words = request.split()
    parts_of_request = ['GET', 'http/1.1', 'HOST']

    for index in range(len(parts_of_request)):
        if index != 1:
            if word[index] is not parts_of_request[index]:
                return  

    if len(words) is not 5:
        raise Exception(response_error(400))
    if words[0] == 'GET':
        if words[2] == "http/1.1":
            if words[3] == "HOST:":
                return words[1].encode('utf8')
            else:
                raise Exception(response_error(400))
        else:
            raise Exception(response_error(505))
    else:
        raise Exception(response_error(501))


if __name__ == '__main__':  # pragma: no cover
    main()



    #"GET /index.html HTTP/1.1\r\nHost: www.example.com"
# GET /path/to/index.html HTTP/1.0<CRLF>
# <CRLF>
    #message.decode('utf8').endswith(\r\n\r\n):
        #flag = False
    #also maybe some logic to ensure is a proper request?
    #IDK maybe not.