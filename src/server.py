# -*- coding: utf-8 -*-
import socket
import sys


def main():  # pragma: no cover
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5015)
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
                if log[-1:] == b"\xa7":
                    flag = False
            sys.stdout.write(log.decode('utf8')[:-1])
            response = response_ok()
            connection.sendall(response)
            connection.close()
        except KeyboardInterrupt:
            server.close()
            sys.exit()

def response_ok():#  pragma: no cover
    response = b"HTTP/1.1 200 OK \r\nContent-Type: text/plain \r\n \xc2\xa7"
    return response

def response_error():
    response = b"HTTP/1.1 500 Internal Server Error \r\nContent-Type: text/plain \r\n \xc2\xa7"
    return response

if __name__== '__main__':#  pragma: no cover
    main()