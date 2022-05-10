import speech
import cv2
import os
import datetime
import detect

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "drishti-tsrd-1b0f94978e8d.json"
project_id = "drishti-tsrd"

# create an object from speech module
engine = speech.speech_to_text()

listning = False

print("Started....")
while True:

    if not listning:
        print("speak...")
        resp = engine.recognize_speech_from_mic()
        print("you said:", resp)

        if resp != None:
            intent, text = detect.detect_intent_texts(project_id, 0, [resp], 'en')
            print("intent:", intent, "text:", text)
        if(resp != None and intent == 'Drishti'):
            listening = True
    
    else:
        engine.text_speech("what can i help you with?")
        intent = ''
        engine.text_speech("Listening")
        resp = engine.recognize_speech_from_mic()
        print("you said:", resp)

        engine.text_speech("Processing")
        if(resp!=None):
            print(resp)
            intent, text = detect.detect_intent_texts(project_id, 0, [resp], 'en')
            print("intent:", intent, "text:", text)

        if resp is not None:
            engine.text_speech(text)
