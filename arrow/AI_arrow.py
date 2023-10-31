from tensorflow.keras.models import load_model
import cv2
import numpy as np
from base64 import b64decode
from PIL import Image
import io
import os

cnn = load_model(os.path.abspath("arrow/AIs/CC64-CC128-CD256.h5"), compile=False)

def decode_image(image):
    image = b64decode(image)
    image = Image.open(io.BytesIO(image))
    image = np.array(image)
    image = cv2.resize(image, (240, 240))
    return image.reshape(-1,240,240,1)



def analyze_arrow(image):
    image = decode_image(image)
   
    prediction =cnn.predict(image)
    prediction = prediction.tolist()
    directions = ["right","up","left","down"]

    max_val = max(prediction)

    for i,dir in enumerate(directions):

        if max_val == prediction[i]: return dir
    
    return directions[-1]
    
