import socket
import os
import io
import PIL.Image as Image
import time
from functions.init import scrshot, sendTextViaSocket, receiveTextViaSocket, readimage

HOST = 'localhost'
PORT = 65439
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    # socket connection

    byts = scrshot()
    print(len(byts))
    lb = str(len(byts))
    lenb = bytes(lb, 'utf-8')
    sendTextViaSocket(lenb, conn)
    for i in range(len(byts) // 1024):
        message = byts[i * 1024:1024 + i * 1024]
        sendTextViaSocket(message, conn)
        ms = receiveTextViaSocket(conn).decode("utf-8")
        if ms == "ok":
            continue
        else:
            break
    if len(byts) % 1024 != 0:
        message = byts[len(byts) - len(byts) % 1024:]
        sendTextViaSocket(message, conn)



if __name__ == '__main__':
    main()