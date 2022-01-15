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


host = input("Give the host of the streamer")
if host=="":
    host="localhost"
port = 8080
socket   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

print("Connected")

try:
    Reception(socket)
    print("End")
except ConnectionRefusedError:
    print("Connection failed")
except Exception as e:
    print(e)
finally:
    socket.close()
