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

        #conn.send(pickle.dumps(frame).encode("utf-8"))
        #frame = imutils.resize(self.arr,width=320)
        #a = pickle.dumps(frame)
        #message = struct.pack("Q",len(a))+a
        #conn.sendall(message)
        #while len(self.arr) > 0:
        #    msg = self.arr[:4096]
        #    print(msg)
        #    print(len(msg))
        #    conn.send(bytes(str(msg), 'utf-8'))
        #    self.arr = self.arr[4096:]
        #print("End")
        #data = self.arr
        #data = self.conn.send(data)
        #message = struct.pack("Q",len(a))+a
        #client_socket.sendall(message)


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
