#======================================================================================================
# Turning Chat-GPT into a smart voice assistant
# based on speech recognition and text-to-speech synthesis.
# The voice assistant can answer questions and give feedback.
# Author: Hao, Zhao 2023-01-21
#======================================================================================================

# Import the OpenAI library
import openai
openai.api_key = "Inset Your OpenAI API key"

# Import the speech recognition library
import speech_recognition as sr
# Set up the recognizer
r = sr.Recognizer()

# Import the text to speech synthesis library
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 120)            # setting up new voice rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female

# Record the audio
engine.say(" Do you have any questions to ask Chat GPT?")
engine.runAndWait()
print('---------------------Please speak now, recording start-----------------------')
with sr.Microphone() as source:
    audio = r.listen(source)
print('---------------------Recording finished---------------------------------------')

# Convert the audio to text
prompt = r.recognize_google(audio)
print(prompt)

# check if the reply contains 'yes'
while 'YES' in prompt.upper() or 'QUESTION' in prompt.upper():

    # Record the audio
    engine.say(" Please ask your question and get help from Chat GPT?")
    engine.runAndWait()
    print('---------------------Please speak now, recording start-----------------------')
    with sr.Microphone() as source:
        audio = r.listen(source)
    print('---------------------Recording finished---------------------------------------')

    # Convert the audio to text
    prompt = r.recognize_google(audio)

    # Generate text
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the generated text
    message = completions.choices[0].text
    print(message)

    # generate the feedback
    engine.say(message)
    engine.runAndWait()
    # engine.stop()

    # Record the audio
    engine.say(" Do you have any other questions to ask Chat GPT?")
    engine.runAndWait()
    print('---------------------Please speak now, recording start-----------------------')
    with sr.Microphone() as source:
        audio = r.listen(source)
    print('---------------------Recording finished---------------------------------------')

    # Convert the audio to text
    prompt = r.recognize_google(audio)
    print(prompt)

