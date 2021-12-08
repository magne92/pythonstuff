#!/usr/bin/python           # This is client.py file

import socket

from server import HEADERSIZE               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
# Create a socket object

host = socket.gethostname() # Get local machine name
port = 12435                # Reserve a port for your service.

s.connect((host, port))


while True:
    full_msg = ''
    new_msg = True
    msg = s.recv(8)
    if new_msg:
        print(f"new message length: {msg[:HEADERSIZE]}")
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    print(f'full message length: {msglen}')

    full_msg += msg.decode('utf-8')

    if len(full_msg)-HEADERSIZE == msglen:
        print("full msg recived")
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = ''


    print(full_msg)