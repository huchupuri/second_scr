import os
import io
import PIL.Image as Image
import time

from array import array
path = 'my.png'
newb = bytearray()
def readimage(path):
    with open(path, "rb") as f:
        return bytearray(f.read())
bytes = readimage(path)
blen = len(bytes)
y = 1024
a = 0
while blen != len(newb):
    newb = newb + bytes[1024*a:y+1024*a]
    a += 1
print(bytes)
print(newb)
image = Image.open(io.BytesIO(newb))
image.save('asd.png')