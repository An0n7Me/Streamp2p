import socket, struct, pickle, cv2, record


def Reception(socket):
    data = b""
    payload_size = struct.calcsize("L")
    while True:
        data += socket.recv(payload_size)
        packedImageSize = data[:payload_size]
        imageSize = struct.unpack("L", packedImageSize)[0]
        data = data[payload_size:]
        while len(data) < imageSize:
            data += socket.recv(65000)
        frameData = data[:imageSize]
        data = data[imageSize:]
        frame = pickle.loads(frameData)
        record.display(frame,isresize=False)
        if cv2.waitKey(1) == ord('q'):break
    return None


host = "localhost"
port = 5566
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
try:
    while True:
        Reception(socket)
        print("Good connect")
except ConnectionRefusedError:
    print("Connection failed")
finally:
    socket.close()
