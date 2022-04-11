import speech
import cv2
import os
import datetime

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "dfkey.json"
project_id = "blindbot-4f356"

# create an object from speech module
engine = speech.speech_to_text()

print("Started....")
while True:
    print("Speak...")
    resp = engine.recognize_speech_from_mic()
    print("you said:", resp)
    engine.text_speech(resp)