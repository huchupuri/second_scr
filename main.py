import cv2
import win32gui, win32ui, win32con, win32api
import time
import numpy as np
start_time = time.time()
width = 1920
height = 1080
left = 1920
top = 0

hwin = win32gui.GetDesktopWindow()

hwindc = win32gui.GetWindowDC(hwin)
srcdc = win32ui.CreateDCFromHandle(hwindc)
memdc = srcdc.CreateCompatibleDC()
bmp = win32ui.CreateBitmap()
bmp.CreateCompatibleBitmap(srcdc, width, height)
memdc.SelectObject(bmp)
memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
print("--- %s seconds ---" % (time.time() - start_time))
signedIntsArray = bmp.GetBitmapBits(True)
img = np.fromstring(signedIntsArray, dtype='uint8')
img.shape = (height, width, 4)
print(type(signedIntsArray))
srcdc.DeleteDC()
memdc.DeleteDC()
win32gui.ReleaseDC(hwin, hwindc)
win32gui.DeleteObject(bmp.GetHandle())
#oimg = img.astype(np.float32)/255
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert it to hsv
img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR) # convert back to BGR
"""cv2.imwrite("output.png", img)  #(img*255).astype(np.uint8)"""
print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow('screenshot', img)
cv2.waitKey(0)
"""import time

import mss.tools
import numpy as np
with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 2
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    monitor = {
        "top": 0,  # 100px from the top
        "left": 1920,  # 100px from the left
        "width": 1920,
        "height": 1080,
        "mon": monitor_number,
    }
    # Grab the data
    sct_img = sct.grab(monitor)
    png = mss.tools.to_png(sct_img.rgb, sct_img.size)
    print(type(png))

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output='monitor-2.png')"""