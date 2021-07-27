import keyboard, sys
import sys, pyperclip  # read and get text from clipboard
from nltk.tokenize import sent_tokenize

import pyttsx3  # voice setup

#
# # VOICE SETUP
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # making list of voices
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)  # speak the given input
    engine.runAndWait()


if len(sys.argv) > 1:  # if file of text is more than a file it means it will return more than 1
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
for sentence in sent_tokenize(address):
    print(sentence)
    speak(sentence)
