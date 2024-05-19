import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
engine.say("I am Sezu, your AI assistant")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year) 
    month = datetime.datetime.now().month   
    day = int(datetime.datetime.now().day)  
    speak("The current date is:")   
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sanjana")
    
    time()
    
    date()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning Sanjana")
    elif 12 <= hour < 18:
        speak("Good afternoon Sanjana") 
    elif 18 <= hour < 24:
        speak("Good evening Sanjana") 
    else:
        speak("Good night Sanjana")   

    speak("Sezu at your service. Please tell me how can I help you?")

# wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
       
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that.")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('21egjcs129@gitjaipur.com','90523@git')
    server.sendmail('21egjcs129@gitjaipur.com',to,content)
    server.close()

if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()   
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)  
        elif 'send email' in query:
            try:
                speak("what should i send")
                content=takeCommand()
                to = 'sanjanasuthar59@gmail.com'
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("unable to send the email, sorry try again") 

        # elif 'search in chrome' in query:
        #     speak("what should i search")
        #     # chromepath ="https://google.com" 
        #     search = takeCommand().lower()
        #     webbrowser.get(chromepath).open_new_tab(search+'.com')
 
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")        
        elif 'play songs' in query:
            songs_dir = "https://open.spotify.com/track/2RNsweBBb1a6tAHXQtt2xH?si=baea3ab191fe413d" 
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))  
        elif 'remember that':
            speak("what should i remember")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()      
        elif 'offline' in query:
            quit()