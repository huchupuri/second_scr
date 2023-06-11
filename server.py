import socket
import os
import io
import PIL.Image as Image

HOST = 'localhost'
PORT = 65439
path = 'my.png'
def readimage(path):
    with open(path, "rb") as f:
        return bytearray(f.read())

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()
    print('---socket now listening---')
    conn, addr = sock.accept()
    print('---socket accepted---')
    byts = readimage(path)
    lenb = bytes(str(len(byts)), 'utf-8')
    sendTextViaSocket(lenb, conn)
    y = 1024
    a = 0
    while True:
        data = byts[1024*a:y+1024*a]
        sendTextViaSocket(data, conn)
        encodedMessage = receiveTextViaSocket(sock)
        encodedMessage = encodedMessage.decode('utf-8')
        if encodedMessage == lenb:
            break

def sendTextViaSocket(message, sock):
    sock.sendall(message)
def receiveTextViaSocket(sock):
    encodedMessage = sock.recv(1024)
    encodedMessage = bytearray(encodedMessage)
    return encodedMessage
if __name__ == '__main__':
    main()