import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("opening youtube")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("opening linkedin")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("opening instagram")
    else:
        speak("I didn't understand that.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)   
            if (word.lower() == "jarvis"):
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            speak("Sorry, I didn't catch that. Please try again.")
            print("Error; {0}".format(e))


# hello
