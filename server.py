#!/usr/bin/env python3


"""
Server side script to receive data through socket.
The communication protocol is TCP IPv4.
"""

import socket
from server_config import *


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(BUFFER)
            if not data:
                break
            try:
                angles = [int(d) for d in data.split(b' ')]
                print(angles)
            except:
                print("Invalid data type")
            
