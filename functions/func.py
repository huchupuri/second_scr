import cv2
import win32gui, win32ui, win32con, win32api
import time
import numpy as np

def scrshot(width = 1920, height = 1080, left = 1920, top = 0):
    hwin = win32gui.GetDesktopWindow()

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    return signedIntsArray
def sendTextViaSocket(message, sock):
    sock.sendall(message)

def receiveTextViaSocket(sock):
    encodedMessage = sock.recv(1024)
    encodedMessage = bytearray(encodedMessage)
    return encodedMessage
def readimage(path):
    with open(path, "rb") as f:
        return bytearray(f.read())