import threading
import socket
import record
import struct
import pickle
import imutils

class TreadClient(threading.Thread):
    def __init__(self, conn, arr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.arr = arr

    def run(self):
        imageBytes = pickle.dumps(self.arr)
        self.conn.sendall(struct.pack("L", len(imageBytes)) + imageBytes)


host, port = ("", 5566)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print("Server initialized")

s.listen(1)
conn, address = s.accept()

while True:
    frame=record.record()

    print("Connected with the address :", address)
    mt = TreadClient(conn, frame)
    mt.run()
