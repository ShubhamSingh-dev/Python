import speech_recognition as sr
import webbrowser
import pyttsx3

recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say("I will speak this text")

if __name__ == '__main__':
  speak("Hey sir how may i help you")