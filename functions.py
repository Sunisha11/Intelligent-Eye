import cv2
import numpy as np
import os
import modules.speech as speech

engine = speech.speech_to_text()


def getBrightness(cam):
    ret, frame = cam.read()
    if ret == None:
        engine.text_speech("Not getting any frame. Quitting now...")
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg = np.sum(frame) / (frame.shape[0] * frame.shape[1])
        avg = avg / 255
        if(avg > 0.6):
            return ("Very bright", avg)
        if(avg > 0.4):
            return ("Bright", avg)
        if(avg > 0.2):
            return ("Dim", avg)
        else:
            return ("Dark", avg)


def play_file(fname):
    return os.system("mpg123 " + fname)
