# -*- coding: utf-8 -*-
import socket
import sys
"""A basic server that listens to a message and sends a parroted response back to whoever sent it."""

def main():  # pragma: no cover
    """Listen for a message, then respond with same message."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5009)
    server.bind(address)
    server.listen(1)
    while True:
        try:
            connection, address = server.accept()
            res = b""
            flag = True
            while flag is True:
                more = connection.recv(8)
                res += more
                print(res)
                print(res[-1:])
                if res[-1:] == b"\xa7":
                    flag = False
            print("Message sent: ", res)
            connection.sendall(res)
            connection.close()
        except KeyboardInterrupt:
            server.close()
            sys.exit()


if __name__=='__main__':  # pragma: no cover
    """Run main on start."""
    main()