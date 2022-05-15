import cv2
import numpy as np

def getBrightness(cam):
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg = np.sum(frame) / (frame.shape[0] * frame.shape[1])
    avg = avg / 255
    if(avg > 0.6):
        return ("Very bright", avg)
    if(avg > 0.4):
        return ("Bright", avg)
    if(avg >0.2):
        return ("Dim", avg)
    else:
        return ("Dark",avg)
