# -*- coding: utf-8 -*-
"""Client for the http server assignment."""
import socket
import sys


def main(words):  # pragma: no cover
    """
    Joins list of words from system args, then runs start_client with them.
    """
    if words is not '':
        print(start_client(' '.join(words)))


def start_client(msg):
    """
    Adds a signature character to the end of the message. Connects to server and sends
    string message. Then parses the response using the special character. Removes character
    to output response.
    """
    msg = msg + '§'
    if sys.version_info.major == 2:
        msg = msg.decode('utf8')
    addr_info = socket.getaddrinfo('127.0.0.1', 5015)
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

if __name__ == '__main__':#  pragma: no cover
    if len(sys.argv) > 1:
        main(sys.argv[1:])
