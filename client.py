#!/usr/bin/env python


"""
Client side script to send data through socket.
The communication protocol is TCP IPv4.
"""

import socket
import struct
from server_config import *


class Client:


    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))


    def __del__(self):
        self.sock.close()


    def _encode_data(self, data):
        data_type = type(data)
        if data_type == int:
            return "i" + struct.pack("<i", data)
        elif data_type == float:
            return "f" + struct.pack("<f", data)


    def send_data(self, data):
        try:
            if type(data) == str: raise TypeError
            _ = iter(data)

            data = b" ".join(self._encode_data(d) for d in data)
        
        except TypeError:
            data = self._encode_data(data)

        finally:
            self.sock.sendall(data)



    def close(self):
        self.sock.close()