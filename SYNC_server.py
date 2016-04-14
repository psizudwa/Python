__author__ = 'pridachin'

import socket
import os
"""
HOST = ''
PORT = 9090
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(HOST, PORT)
sock.listen(3)
conn, addr = sock.accept()
"""
fp = open("file.jpg", "wb")
while 1:
    data = sock.read(4096)
    if not data: break
    fp.write(data)
fp.close()
"""
while True:
    data = conn.recv(1024)
    print()
    if not data:
        break
    conn.send(1024)
conn.close()
"""