#!/usr/bin/env python


"""
Client side script to send data through socket.
The communication protocol is TCP IPv4.
"""

import socket
from server_config import *



class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))


    def __del__(self):
        self.sock.close()


    def send_data(self):
        data = input("Enter message to send or type 'exit': ")
        if data == "exit":
            break
        self.send.sendall(data.encode())


    def close(self):
        self.sock.close()