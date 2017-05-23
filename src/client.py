import socket


addr_info = socket.getaddrinfo('127.0.0.1', 5001)

stream_info = [attr for attr in addr_info if attr[1] == socket.SOCK_STREAM][0]

client = socket.socket(*stream_info[:3])


msg = "This is a long string mesage, transmitted with a size of 8!"

client.connect(stream_info[-1])
client.sendall(msg.encode('utf8'))

flag = True
res = ""
while flag is True:
    more = client.recv(8)
    res += more.decode('utf8')
    if res[-1] == "!":
        flag = False
print(res)
client.close()

