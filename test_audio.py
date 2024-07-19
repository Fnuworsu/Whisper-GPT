import pyttsx3


engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id, voice.name)
    
engine.setProperty('voice', voices[1].id)

text = "Hello, this is a test."
engine.say(text)
engine.runAndWait()
