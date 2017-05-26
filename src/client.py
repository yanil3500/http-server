"""A sample client for our echo server. This code sends any message you give it to the server, and then waits for and prints the response."""
# -*- coding: utf-8 -*-
import socket
import sys


def main(words):  # pragma: no cover
    """Joins words, which should be a list. Then it calls start_client with the words, and prints the result."""
    if words is not '':
        print(start_client(' '.join(words)))


def start_client(msg):
    """Initialize and send the message, placing a special character at the end so that the server can recognize when to stop. Then waits for and returns the response."""
    msg = msg + '§'
    if sys.version_info.major == 2:
        msg = msg.decode('utf8')
    addr_info = socket.getaddrinfo('127.0.0.1', 5009)
    stream_info = [attr for attr in addr_info if attr[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(msg.encode('utf8'))
    flag = True
    res = b""
    while flag is True:
        more = client.recv(8)
        res += more
        if res[-1:] == b"\xa7":
            flag = False
    client.close()
    if sys.version_info.major == 2:
        return res[:-2]
    return res.decode('utf8')[:-1]

if __name__ == '__main__':  # pragma: no cover
    """Start main with the system argument words on start."""

    if len(sys.argv) > 1:
        main(sys.argv[1:])
