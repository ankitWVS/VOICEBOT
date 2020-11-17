import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("A very Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("CREATING VIRTUAL ENVIRONMENT")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold * 1

        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        speak("say that again please...")
        return "None"
    return query
if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching internet',)
            results = wikipedia.summary(query, sentences=2)
            speak("According to internet")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")
        elif 'open gate' in query:
            webbrowser.open("github.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'E:\\music\\UCDownloads'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M,%S")
            speak(f"the time is {strTime}")
        elif 'open pycharm' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
            os.startfile(codepath)
        elif 'open tor' in query:
            itspath = "C:\\Users\\LENOVO\\Desktop\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(itspath)
