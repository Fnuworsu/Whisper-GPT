import pyttsx3


engine = pyttsx3.init()

# Set the speech rate (words per minute)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

# Get and print the available voices
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id, voice.name)

# Set the voice (e.g., change to the second voice in the list)
engine.setProperty('voice', voices[1].id)

text = "Hello, this is a test."
engine.say(text)
engine.runAndWait()
