import gradio as gr
import config
import pyttsx3
from openai import OpenAI
client = OpenAI(api_key=config.OPEN_API_KEY)
messages=[
            {"role": "system", "content": "You are a helpful data structures and algorithms coach."},
        ]

def transcribe(audio):
    global messages
    
    audio_file= open(audio, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
    )
    #print(transcription)

    messages.append({"role": "user", "content": transcription.json()})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    system_message=response.choices[0].message.content
    messages.append({"role": "assistant", "content": system_message})
    #print(response.choices[0].message.content)
    engine=pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    text=system_message
    engine.say(text)
    engine.runAndWait()
    
    chat_transcript=""
    for message in messages:
        if message["role"] != "system":
            chat_transcript += message["role"] + ": " + message["content"]+ "\n\n"
    return chat_transcript

ui= gr.Interface(fn=transcribe, inputs=gr.Audio(sources=["microphone"], type="filepath"),outputs=["text"])
ui.launch()