import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

address = ('127.0.0.1', 5001)

server.bind(address)


server.listen(1)
while True:
    try:
        connection, address = server.accept()
        res = ""
        flag = True
        while flag is True:
            more = connection.recv(8)       
            res += more.decode('utf8')
            if res[-1] == "!":
                flag = False
            # if len(more.decode('utf8') == 0):
            #     flag = False
        print(res)
        connection.sendall(str(res).encode('utf8'))

    except KeyboardInterrupt:
        server.close()
        sys.exit()