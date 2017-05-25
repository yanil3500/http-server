# -*- coding: utf-8 -*-
"""Client for the http server assignment."""
from __future__ import unicode_literals
import socket


def main(words=''):  # pragma: no cover
    """
    Joins list of words from system args, then runs start_client with them.
    """
    if words is not '':
        start_client(' '.join(words))


def start_client(msg):
    """
    Adds a signature character to the end of the message. Connects to server and sends
    string message. Then parses the response using the special character. Removes character
    to output response.
    """
    msg = msg + '\r\n\r\n'
    addr_info = socket.getaddrinfo('127.0.0.1', 5179)
    stream_info = [attr for attr in addr_info if attr[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(msg.encode('utf8'))
    flag = True
    res = b""
    while flag:
        more = client.recv(8)
        res += more
        if res.decode('utf8').endswith('\r\n\r\n'):
            flag = False
    client.shutdown(socket.SHUT_WR)
    client.close()
    return res.decode('utf8')


if __name__ == '__main__':  # pragma: no cover
    main('GET /a_web_page.html http/1.1\r\n\r\nHOST: www.hostythehostess.gov:80\r\n\r\n'.split(' '))
