import pyttsx3
import speech_recognition as sr
import pyaudio #to get the audio of the user
import datetime #to get the real time date and time
import os #os module is use to access all querries related to the system 
import socket # I use this module to get my system ip address
import webbrowser #to access in the browser
import pywhatkit as kit #i use this module to play a song on youtube as i want.
import sys #as i use this to end my task just by using my voics as a command
import psutil # use this to get the battery percentage of the system
import speedtest #here i'm using this to know my internet speed.


engine = pyttsx3.init('sapi5') #this is a engine use to convert text to voice
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#Now we make a function which coverts speech into text

#Wish function
def wishFun():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good evening sir")
    
    speak("I am Jarvish sir. Please tell me how can i help you")



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand(): #i use this function to convert voice recieved from user into text.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=7)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said:{query}")
    except Exception as e:
        speak("Sorry, Can't hear you")
        return "none"
    return query

def task():
    wishFun()
    while True:
    #if 1:
        querry = takecommand().lower()
        if "open notepad" in querry:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)
            speak("opening notepad")
        elif "open command prompt" in querry:
            path = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(path)
            speak("opening command prompt")
        elif "open chrome" in querry:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif "play music" in querry:
            music = "F:\\music_dir"
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))
        elif "ip address" in querry:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            speak("Your ip address is"+IPAddr)
            print(IPAddr)
        elif "open youtube" in querry:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif "open google" in querry:
            speak("Sir, what should I search for you on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "play song on youtube" in querry:
            speak("Sir, please tell me the song name")
            cm = takecommand().lower()
            kit.playonyt(cm)
        elif "you can sleep" in querry:
            speak("Okay Sir, wake me when you want")
            break
        elif "close notepad" in querry:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "hello" in querry or "hey" in querry:
            speak("hello sir may I help you with something")
        elif "how are you" in querry:
            speak("I am fine sir, what about you")
        elif "how much power left" in querry or "how much power we have" in querry or "battery" in querry:
            power = psutil.sensors_battery()
            rem = power.percent
            speak(f"Sir we have {rem} percent power")
        elif "internet speed" in querry or "data speed" in querry:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")




if __name__ == "__main__":
    while True:
        value = takecommand().lower()
        if "wake up" in value:
            task()
        elif "goodbye" in value:
            speak("Thanks for using me, Sir")
            sys.exit()
        
    
        

        


         
    #takecommand()
    #speak("Hello, this is jarvish")