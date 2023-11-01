import cv2
import numpy as np
from base64 import b64decode
import io
import os
from PIL import Image


def create_folders():
    folders = ["photos","photos/right","photos/up","photos/down","photos/left",]
  
    for i in folders:
        try:
            os.mkdir(i)
        except:
            pass

def decode_image(image):
    image = b64decode(image)
    image = Image.open(io.BytesIO(image))
    return image

def load_arrows(image):
    image = decode_image(image)
    
    image = np.array(image)
    image = cv2.resize(image, (240, 240))
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    _,image = cv2.threshold(image,120,255,cv2.THRESH_BINARY)
    
    carpetas = ["right","down","left","up"]
    for i in carpetas:
        car = os.listdir(os.path.join(f"photos", i))
        car.sort(key=lambda car: os.path.getctime(os.path.join(f"photos/{i}", car)), reverse=True)

        try:
            num = int(os.path.splitext(os.path.basename(os.path.join(f"photos/{i}",car[0])))[0]) + 1
        except:
            num = 1
        cv2.imwrite(f"photos/{i}/{num}.jpeg",image)
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
   