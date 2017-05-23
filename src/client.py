# -*- coding: utf-8 -*-
import socket
import sys


def main(words):  # pragma: no cover
    """
    main function
    """
    if words is not '':
        print(start_client(' '.join(words)))


def start_client(msg):
    """
    creates the client
    """
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

if __name__ == '__main__':

    if len(sys.argv) > 1:
        main(sys.argv[1:])
