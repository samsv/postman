#!/usr/bin/env python


"""
Server side script to receive data through socket.
The communication protocol is TCP IPv4.
"""

import socket
import struct
from server_config import *


class Server:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(1)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


    def __del__(self):
        self.sock.close()


    def _get_data(self, data):
        data_type = "<" + data[0]
        data = data[1:]
        return struct.unpack(data_type, data)[0] 


    def connect(self, callback):
        """
        Connects to a client. Calls a callback function when data is received 
        """
        conn, addr = self.sock.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(BUFFER)
            if not data:
                break
            try:
                data = [self._get_data(d) for d in data.split(b' ')]
                callback(data)
            except Exception as e:
                print(e)    
        # Sadly, due to python 2 compatibility, so we have to manually close the connections
        conn.close()


    def close(self):
        self.sock.close()