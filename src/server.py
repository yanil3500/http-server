# -*- coding: utf-8 -*-
"""Server for http server assignment."""
from __future__ import unicode_literals
from email.utils import formatdate
import html_maker
import socket
import sys
import os


CURRENT_PATH = 'src'


def main():  # pragma: no cover
    """Main server loop. Logs data into log variable until it finds a certain character. Then returns response."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 10001)
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
            content = resolve_uri(URI)
            response = response_ok(content)
            connection.sendall(response.encode('utf8'))
            connection.close()
        except KeyboardInterrupt:
            server.shutdown(socket.SHUT_WR)
            server.close()
            sys.exit(0)
        except TypeError:
            response = response_error(404)
            connection.sendall(response.encode('utf8'))
            connection.close()
        except LookupError:
            response = response_error(501)
            connection.sendall(response.encode('utf8'))
            connection.close()
        except ValueError:
            response = response_error(400)
            connection.sendall(response.encode('utf8'))
            connection.close()
        except IOError:
            response = response_error(404)
            connection.sendall(response.encode('utf8'))
            connection.close()
        except NameError:
            response = response_error(505)
            connection.sendall(response.encode('utf8'))
            connection.close()


def response_ok(body_response):  # pragma: no cover
    """
    function is responsible for returning a 200 OK response
    """
    content, file_size, content_type = body_response
    today_date = str(formatdate(usegmt=True))
    response = 'HTTP/1.1 200 OK \r\nDate: {}\r\nContent-Length: {}\r\nContent-Type: {}\r\n\r\n{}\r\n\r\n'.format(today_date, file_size, content_type, content)
    return response


def resolve_uri(URI):
    """
    function determince the content type, and generates the content for the http response
    """
    file_path = os.path.join(CURRENT_PATH, URI[1:])
    type_of_file = file_path.split('.')[-1]
    content_type_switcher = {
        'jpg': 'image/jpeg',
        'png': 'image/png',
        'txt': 'text/plain',
        'html': 'text/html',
        'py': 'text/python',
        'directory': 'directory'
    }
    if os.path.isdir(file_path):
        if not file_path.endswith('images'):
            content = html_maker.html_str_maker(os.listdir(os.path.join(os.getcwd(), file_path)), f_path=file_path)
            type_of_file = 'html'
            file_size = len(content)
        else:
            content = html_maker.html_str_maker(os.listdir(os.path.join(os.getcwd(), file_path)), file_path)
            type_of_file = 'html'
            file_size = len(content)
    else:
        if os.path.isfile(file_path):
            print('Inside of endswith(jpg): {}'.format(file_path))
            if file_path.endswith('jpg'):
                type_of_file = 'jpg'
                with (file_path, 'rb') as img:
                    content += img.read()
                print('jpgs: {}'.format(content))
                file_size = os.path.getsize(file_path)
            elif file_path.endswith('png'):
                type_of_file = 'png'
                content = open(file_path.read(file_path, 'rb'))
                file_size = os.path.getsize(file_path)
            else:
                content = open(file_path).read()
                file_size = os.path.getsize(file_path)
    return content, file_size, content_type_switcher[type_of_file]


def response_error(error_code):
    # Idea for switch dictionary: https://www.pydanny.com/why-doesnt-python-have-switch-case.html
    """Returns 500 response."""
    switch_dict = {
        505: "HTTP/1.1 505 HTTP Version Not Supported \r\nContent-Type: text/plain \r\n\r\n",
        501: "HTTP/1.1 501 Method Not Implemented \r\nContent-Type: text/plain \r\n\r\n",
        400: "HTTP/1.1 400 Bad Request \r\nContent-Type: text/plain \r\n\r\n",
    }
    response = switch_dict.get(error_code, "HTTP/1.1 404 Not Found \r\nContent-Type: text/plain \r\n\r\n")
    return response


def parse_request(request):
    """
    responsible for parsing http requests
    """
    words = request.split()
    print('Request: {}'.format(request))
    parts_of_request = ['GET', 'HTTP/1.1', 'Host:']
    if words[0] != parts_of_request[0]:
        print('Lookup Error: {} '.format(words[0]))
        raise LookupError
    elif words[2] != parts_of_request[1]:
        print('Name Error: {} '.format(words[2]))
        raise NameError
    elif words[3] != parts_of_request[2]:
        print('Value Error: {} '.format(words[3]))
        raise ValueError
    else:
        return words[1]


if __name__ == '__main__':  # pragma: no cover
    main()
