from email.mime import audio
from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
#to reconginse voices
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good moring")
    elif hour>=12 and hour<12:
        speak("Good afternoon")
    else:
        speak("good evening")
    speak("i m kalorine ")
def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        #threshold is time to complete the sentence
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("user said:", query)
        
    except Exception as e:
       # print(e)
        print("Say that gain please...")
        return "none"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smntp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('vanshita.1512@gmail.com','"C:\\sers\\vansh\\Documents\\pa.txt"')
    server.sendmail('vanshita.1512@gmail.com',to, content)
    server.close()
    
if __name__ == "__main__":
   wishMe()
   speak("what is your name")
   name = takeCommand()
   speak(f"hey {name}, please tell me how may I help you")
   while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
          speak('searching wikipedia...')
          query = query.replace ("wikipedia", "")
          results = wikipedia.summary(query, sentences=2)
          speak("according to wikipedia")
          print(results)
          speak(results)
        elif 'youtube' in query:
            webbrowser.open ("youtube.com")
        elif 'google' in query:
            webbrowser.open ("google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now ().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'pictures' in query:
            codePath="C:\\Users\\vansh\\Pictures"
            os.startfile(codePath)

        elif 'play song' in query :
            music = "C:\\Users\\vansh\\Music\on"
            # or you have list of aongs use random variable
            songs = os.listdir(music)
            os.startfile(os.path.join(music , songs[1]))
        elif 'bye' in query:
            sys.exit()
