# Python virtual desktop assistant

import datetime
import pyttsx3
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

user = "Ifath"
assistant = "Alia"

def greeting():
    hour = datetime.datetime.now().hour
    if (hour >= 1) and (hour < 6):
        speak("It's pretty late {user}")
        print("It's pretty late {user}")
    if (hour >= 6) and (hour < 12):
        speak("Good morning {user}")
        print("Good morning {user}")
    if (hour >= 12) and (hour < 18):
        speak("Good afternoon {user}")
        print("Good afternoon {user}")
    if (hour >= 18) and (hour < 23):
        speak("Good evening {user}")
        print("Good evening {user}")
    
    speak("This is Alia speaking. What do you need help with?")
    print("This is Alia speaking. What do you need help with?")

if __name__ == "__main__":
    greeting()

    continuing = True
    while continuing == True:
        query = input("State your query: ")

        if "best video game" in query:
            speak("Mega Man X4 is peak fiction, one of the best video games ever made!")
        elif "bye alia" in query:
            speak("Goodbye {user}. Alia, signing off.")
            continuing = False
        else:
            speak("Sorry, I couldn't understand what you said")