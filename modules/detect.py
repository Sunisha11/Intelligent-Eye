import io
import cv2
from google.oauth2 import service_account
import google.cloud.vision_v1 as vision
from google.cloud.vision_v1 import types
import google.cloud.dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
# import speech


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    # print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        try:
            response = session_client.detect_intent(
                session=session, query_input=query_input)

        except InvalidArgument:
            raise

        # print("Query text:", response.query_result.query_text)
        # print("Detected intent:", response.query_result.intent.display_name)
        # print("Detected intent confidence:",
        #       response.query_result.intent_detection_confidence)
        # print("Fulfillment text:", response.query_result.fulfillment_text)

    return response.query_result.intent.display_name, response.query_result.fulfillment_text


def describeScene(cam, engine):
    print(__file__)
    ret, frame = cam.read()
    cv2.imwrite('op.jpg', frame)
    credentials = service_account.Credentials.from_service_account_file(
        "united-monument-350013-0e8fdf2efe4a.json")
    client = vision.ImageAnnotatorClient(credentials=credentials)
    path = 'op.jpg'
    # path = 'images/road2.jpg'
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    engine.text_speech("Description of the view")

    tellObjects(client, image, engine)


def tellObjects(client, image,  engine):
    objects = client.object_localization(
        image=image).localized_object_annotations
    engine.text_speech("I will tell you the objects near you")
    for object_ in objects:
        # print('{} '.format(object_.name))
        engine.text_speech(object_.name)
    lbldict = {}
    for i in objects:
        if i.name in lbldict:
            lbldict[i.name] += 1
        else:
            lbldict[i.name] = 1
    once = True
    length = len(lbldict)
    r = 0
    for i, j in lbldict.items():
        if once:
            if j != 1:
                engine.text_speech("There are")
            else:
                engine.text_speech("There is")
            once = False
        engine.text_speech("{} {}".format(j, i))
        r += 1
        if r != length:
            engine.text_speech("and")
    if (length == 0):
        engine.text_speech("No objects found")

