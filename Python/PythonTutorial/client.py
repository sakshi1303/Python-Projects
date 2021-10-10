# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:54:39 2020

@author: Sakshi Agarwal
"""

import socket

c=socket.socket()

c.connect(('192.168.56.1', 9999))
#c.connect(('localhost',9999))
#print(c.recv(1024))
c.send(b'Aditya')
print(c.recv(1024).decode())
c.close()