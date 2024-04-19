import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("D:\\Project1\\Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

#Greet
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok  boss ,  You can me call  anytime")
                    break 


#Conversations
                elif "hello" in query:
                    speak("Hello boss, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, boss")
                elif "how are you" in query:
                    speak("Perfect, boss")
                elif "thank you" in query:
                    speak("you are welcome, boss")
                elif "get lost" in query:
                    speak("boss, Its  too  rude")  
                elif "shut up" in query:
                    speak("Fine boss ,   Going to shut up")      


#Open Apps
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query) 


#Open Any APP
                elif "open" in query: 
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 


#Searching from web
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)


#Temperature
                elif "temperature" in query:
                    search = "Temperature in Jaipur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "Weather in Jaipur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")


#Playlist
                elif "tired" in query:
                    speak("Playing your favourite songs, Boss")
                    a = (1,2,3) 
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=qLbjezR_zNw&ab_channel=TanzeelKhan")                  
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=ZmDBbnmKpqQ&ab_channel=OliviaRodrigoVEVO")
                    else:
                        webbrowser.open("https://www.youtube.com/watch?v=bNtOvlT9ZCQ&ab_channel=GeetMP3")                      


#Time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"boss, the time is {strTime}")  


#Alarm
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,boss") 
                    
                       
#Rock Paper Scissors
                elif "play a game" in query:
                    from game import game_play
                    game_play()   

#Youtube Controls
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up , boss")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down , boss")
                    volumedown()    


#Remember
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())   


#News
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()    


#Calculate
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)   

#Whatsapp
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()  


#Show shedule                                
                elif "show my schedule" in query:
                        file = open("D:\\Project1\\tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("D:\\Project1\\notification.mp3")
                        mixer.music.play()
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                        )

#Shedule My Day
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO) : ")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()   


#FinallySleep
                elif "finally sleep" in query:
                    speak("Say yonaraa boss , Going to sleep")
                    exit()                        


#Internet Speed
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload() / 1024 / 1024  # Convert to Mbps 
                    download_net = wifi.download() / 1024 / 1024  
                    print(f"Wifi Upload Speed is: {upload_net:.2f} Mbps")  
                    print(f"Wifi download speed is: {download_net:.2f} Mbps")  
                    speak(f"Wifi download speed is {download_net:.2f} Mbps")  
                    speak(f"Wifi Upload speed is {upload_net:.2f} Mbps") 


#live score
                elif "live score" in query:
                    from plyer import notification 
                    import requests 
                    from bs4 import BeautifulSoup
                    url = "https://www.cricbuzz.com/cricket-match/live-scores"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")
                    a = speak(f"{team1} : {team1_score}")
                    b = speak(f"{team2} : {team2_score}")
                    notification.notify(
                        title = "LIVE SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )


#ScreenShot and Photo
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")


#Translate
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)    

#Shutdown
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no) : ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break    



  