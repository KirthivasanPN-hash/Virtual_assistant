import pyttsx3
friend = pyttsx3.init()
speech = input("type here:")
friend.say(speech)
friend.runAndWait()