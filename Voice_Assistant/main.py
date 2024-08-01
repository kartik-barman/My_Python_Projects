import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os
import time

def sptext():
    reconizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning......")
        reconizer.adjust_for_ambient_noise(source)
        audio = reconizer.listen(source)
        try:
            print("Reconizing..................")
            data = reconizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding.......")


def speak(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

# speak("Hi Mr Kartik Barman and welcome our community")

if __name__ == '__main__':
    
    if "hello boss" in sptext().lower():
    
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is kartik"
                speak(name)
            elif "age" in data1:
                age = "My Age is 1 year old"
                speak(age)
            
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speak(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
                
            elif "facebook" in data1:
                webbrowser.open("https://www.facebook.com/")
            
            elif "portfolio" in data1:
                webbrowser.open("https://mrkartikbarman.blogspot.com/")
                
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speak(joke_1)
            elif "song" in data1:
                folder_path = "K:\Music"
                listsong = os.listdir(folder_path)
                print(listsong)
                os.startfile(os.path.join(folder_path, listsong[0]))
            elif "arijit singh" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=8cM3j8SAvYg")
            elif "close" in data1:
                speak("Thank You...")
                break
            
            time.sleep(5)
    else:
        print("Thanks")
    