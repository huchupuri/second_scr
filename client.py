import socket
import select
import time
import io
import PIL.Image as Image
import mss
from functions.init import receiveTextViaSocket
import numpy as np
import cv2

start_time = time.time()
HOST = 'localhost'
PORT = 65439
path = 'my.png'

def main(height = 1080, width = 1920):
    mes = b''
    ans = b'ok' #заменить true/false
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('--- socket instantiated ---')
    connectionSuccessful = False
    while not connectionSuccessful:
        try:
            sock.connect((HOST, PORT))
            print('--- socket connected ---')
            connectionSuccessful = True
        except:
            pass
    socks = [sock]
    len = int(receiveTextViaSocket(sock).decode('ср1251'))
    for i in range(len // 1024):
        readySocks, _, _ = select.select(socks, [], [], 5)
        for sock in readySocks:
            message = receiveTextViaSocket(sock)
            mes = mes + message
            sock.sendall(ans)
            print(i)
    if len % 1024 != 0:
        message = receiveTextViaSocket(sock)
        mes = mes + message
    img = np.fromstring(mes, dtype='uint8')
    img.shape = (height, width, 4)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert it to hsv
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow('a', img)
    cv2.waitKey(0)
    print("--- %s seconds ---" % (time.time() - start_time))
    cv2.imshow('screenshot', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
