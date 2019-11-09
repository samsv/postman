#!/usr/bin/env python3

"""
Client side script to send data through socket.
The communication protocol is TCP IPv4.
"""

import socket
from server_config import *


HOST = '10.10.16.151'  # The server's hostname or IP address
PORT = 6969        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input("Enter message to send or type 'exit': ")
        if data == "exit":
            break
        s.sendall(data.encode())