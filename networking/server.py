#!/usr/bin/python           # This is server.py file
import socket               # Import socket module

import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1243               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.


while True:
   clientsocket, address = s.accept()     # Establish connection with client.
   print (f'Got connection from {address} has been established')

   msg = "Welcome to the server"
   print(f'{len(msg):<{HEADERSIZE}}' + msg)

   clientsocket.send(bytes(msg, 'utf-8'))
   
   while True:
      time.sleep(3)
      msg = f"The time is ! {time.time()}"
      msg = f'{len(msg):<{HEADERSIZE}}' + msg

      print(msg)

      clientsocket.send(bytes(msg, 'utf-8'))



