import speech_recognition as sr
import pyttsx3

listener =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('I am your omen')
engine.say('How can I help you')
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)

        print(command)
except:
    pass