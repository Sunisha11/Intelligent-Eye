import cv2
import os
import datetime
import functions
import modules.speech as speech
import modules.detect as detect

# setting up dialogflow credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "drishti-srck-a65fae3e7146.json"
DIALOGFLOW_PROJECT_ID = "drishti-srck"
DIALOGFLOW_LANGUAGE_CODE = "en"

# create an object from speech module
engine = speech.speech_to_text()

listening = False
intent = None

while True:
    cam = cv2.VideoCapture(0)
    
    if not listening:
        resp = engine.recognize_speech_from_mic()
        print(resp)
        if(resp != None):
            intent, text = detect.detect_intent_texts(
                DIALOGFLOW_PROJECT_ID, 0, [resp], DIALOGFLOW_LANGUAGE_CODE)
        if(intent == 'Drishti' and resp != None):
            listening = True

    else:
        engine.text_speech("What can I help you with?")
        intent = ''
        engine.text_speech("Listening")
        resp = engine.recognize_speech_from_mic()
        engine.text_speech("Processing")
        if(resp != None):
            print(resp)
            intent, text = detect.detect_intent_texts(DIALOGFLOW_PROJECT_ID, 0, [resp], DIALOGFLOW_LANGUAGE_CODE)
        if intent == 'Describe':
            detect.describeScene(cam, engine)
        elif intent == 'Brightness':
            engine.text_speech("It is {} outside".format((functions.getBrightness(cam))[0]))
        elif intent == "Time":
            currentDT = datetime.datetime.now()
            engine.text_speech("The time is {} hours and {} minutes".format(currentDT.hour, currentDT.minute))
        elif intent == "Read":
            print("read")
            detect.detect_text(cam, engine)
        elif intent == 'endconvo':
            print(text)
            listening = False
            engine.text_speech(text)
        elif resp != 'None':
            engine.text_speech(text)
  
    cam.release()
