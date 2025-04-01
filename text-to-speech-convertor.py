import pyttsx3

engine = pyttsx3.init()
print("Hello, this is a text to speech conversion program. It converts text into speech using Python.")
text = input("Enter the text you want to convert to speech: ")
engine.say(text)
engine.runAndWait()