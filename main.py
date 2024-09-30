import speech_recognition as sr
import webbrowser
import pyttsx3

import musicLib

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    if "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command.lower():
        webbrowser.open("https://www.google.com/")
    elif "open github" in command.lower():
        webbrowser.open("https://github.com/Akshit-Vig01")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)
    elif "who developed you" in command.lower():
        speak("Lucifer sir")


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                wake_word = recognizer.recognize_google(audio)

            if "jarvis" in wake_word.lower():
                speak("Yes sir...")

                # Listen for the command after wake word is recognized
                print("Listening for command...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")

                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
