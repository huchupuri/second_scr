import socket
import select
import time
import os
import io
import PIL.Image as Image
start_time = time.time()
HOST = 'localhost'
PORT = 65439
path = 'my.png'

def main():
    mes = bytearray(b'')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('---socket instantiated---')
    connectionSuccessful = False
    while not connectionSuccessful:
        try:
            sock.connect((HOST, PORT))
            print('---socket connected---')
            connectionSuccessful = True
        except:
            pass
    socks = [sock]
    len = receiveTextViaSocket(sock).decode('utf-8')
    len = int(len)
    while True:
        readySocks, _, _ = select.select(socks, [], [], 5)
        for sock in readySocks:
            message = receiveTextViaSocket(sock)
            mes = message + mes
            sock.sendall(mes)
    print(mes)
    print("--- %s seconds ---" % (time.time() - start_time))

def receiveTextViaSocket(sock):
    encodedMessage = sock.recv(1024)
    encodedMessage = bytearray(encodedMessage)
    return encodedMessage
if __name__ == '__main__':
    main()