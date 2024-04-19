import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=5 and hour<=12:
        speak("Good Morning , boss")
    elif hour >12 and hour<=17:
        speak("Good Afternoon , boss")
    elif hour>17 and hour <=21:
        speak("Good Evening , boss")
    else:
        speak("Good Night  ,  boss")
    speak("Tell me, How can I help you ?")
