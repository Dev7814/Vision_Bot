import pyttsx3  # pip install pyttsx3(for text-to-speech conversion )
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser  # allows display of web-based documents
import os  # for interacting with the operating system
import smtplib  # for sending mail

print("Initializing ")
MASTER = "Abhinav"

engine = pyttsx3.init('sapi5')  # voice recognition system
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# Speak function will speak/Pronounce the string which is passed to it


def speak(text):
    engine.say(text)
    engine.runAndWait()

# This funtion will wish you as per the current time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("good morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    speak("I am your personal voice assistant. How may I help you?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhinavsingh312001@gmail.com', 'password')
    server.sendmail("devyanshbansal123@gmail.com", to, content)
    server.close()


# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

# main program starting


def main():
    speak("Initializing Vision...")
    wishMe()
    query = takeCommand()

    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open('youtube.com')
        url = "youtube.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        # webbrowser.open('youtube.com')
        url = "google.com"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\SAVITA SINGH\\Music\\MEmu Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "D:\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to devyansh' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = "devyanshbansal123@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent to Devyansh")
        except Exception as e:
            print(e)


main()
