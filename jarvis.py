import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')                      #sapi5 microsoft speech api
voices = engine.getProperty('voices')               #gives voices present in the system
# print(voices[1])
engine.setProperty('voices',voices[0].id)           #set which voice to be used

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 17:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am Jarvis. How may I help you?')

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('madhusamudra77@gmail.com','Basanti1945')
    server.sendmail('madhusamudra777@gmail.com',to,content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1                           #time given for user to speak
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}")
    except Exception:
        print('Say that again please...')
        return "None"
    return query

wishMe()

if 1:
    query = takeCommand().lower()

    # tasks to be executed
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query, sentences = 2)
        speak('According to wikipedia...')
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak('Openning Youtube...')
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        speak('Openning Google...')
        webbrowser.open("google.com")

    elif 'play music' in query:
        ran_num = random.randint(0,12)
        music_dir = 'C:\\Users\\Archita\\Music\\4K YouTube to MP3'
        songs = os.listdir(music_dir)
        print(songs)
        print(ran_num)
        os.startfile(os.path.join(music_dir, songs[ran_num]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"The time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\Archita\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to madhu' in query:
        try:
            speak('What should I say ?')
            content = takeCommand()
            to = 'madhusamudra77@gmail.com'
            sendEmail(to,content)
            speak('Email is sent!')
        except Exception:
            speak('Sorry, the email could not be sent!')





