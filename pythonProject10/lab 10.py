import apiai, json, re
import pyttsx3
import speech_recognition as sr
import requests

import speech_recognition as sr


def record_volume():

    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Waiting.')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('listening...')
        audio = r.listen(source)
    print('Got it.')
    try:
        query = r.recognize_google(audio, language = 'en-EN')
        text = query.lower()
        print(query.lower())
        if text == "fact":
            req = requests.get("http://numbersapi.com/random/math")
            print(req.text)
        elif text == "delete":
            print("deleted from the file")
        elif text == "add":
            print("added to the file")
        elif text == "next":
            print("showing next file")

        else:
            print("try again")


    except:
        print('Error')

while True:
    record_volume()

