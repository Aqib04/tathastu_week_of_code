import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time
import os
from gtts import gTTS
import pygame
from pygame import mixer
import requests
import json

def speak(audioString):
    global x
    b = audioString
    if len(b) == 0:
        return
    tts = gTTS(text=b, lang='en-us')
    tts.save("voice%s.mp3"%(x))
    pygame.init()
    pygame.display.set_mode((2, 1))
    mixer.music.load("voice%s.mp3" % (x))
    mixer.music.play(0)

    x += 1

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source)
        print("heard...")
    data = ""

    try:
        data = r.recognize_google(audio)
        print("You said : " + data )
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Aqib while I show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")

    elif "weather details of" in data:
        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "607fe2eac6ced3399d24c848c76dccb2"
        
        data = data.split(" ")
        city = data[3]
        url = weather_url + "q=" + city + "&appid=" + api_key
        js = requests.get(url).json()

        speak("Hold on Aqib while I show you the weather details of " + city + ".")

        if js["cod"] != "404": 
            weather = js["main"] 
            temp = weather["temp"] 
            hum = weather["humidity"] 
            desc = js["weather"][0]["description"]
            resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
            speak(resp_string)
        else: 
            speak("City Not Found")

    else :
        speak("I did not get what you said !!!!!")


time.sleep(0.5)
x = 0
print("start..")
speak("Hi Aqib! What can I do for you?")
data = recordAudio()
jarvis(data)
speak("Turning off the program.")
print("Run complete")
