import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def u_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sage'in command:
                command = command.replace('sage','') 
                print(command)

    except:
        pass
    return command

def run_sage():
    command = u_command()
    print(command)
    if 'play' in command:
        song =command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('the time is'+time)

    elif 'who is' in command:
        title = command.replace('who is','')
        info  = wikipedia.summary(title,1)
        print(info)
        talk(info)
    
    else:
        talk('i didnt understand')

while True:
    run_sage()