#pip install SpeechRecognition
#pip install mtranslate
#pip insall colorama
#pip install pyaudio
#pip install setuptools


import os
import speech_recognition as sr
from mtranslate import translate
import threading
from colorama import Fore, Style, init
import pyaudio

init(autoreset=True)

def print_loop():
    #while True:
        print(Fore.GREEN + "Listening....", end="", flush=True)
        print(Style.RESET_ALL, end="", flush=True)

def Translate(text):
    english_text = translate(text, 'en-US')
    return english_text

def Speech_To_Text():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 40000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.dynamic_energy_threshold = False
    recognizer.pause_threshold = 0.7
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "Listening.....", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                os.system('cls')
                print  ( "\r",Fore.GREEN + "Recognizing....", end="", flush=True)
                Recognized_text = recognizer.recognize_google(audio).lower()  # Requires Google Cloud API setup
                if Recognized_text:
                    translated_text = Translate(Recognized_text)
                    print("\r" + Fore.BLUE + "\n Gowtham: " + translated_text)
                    return translated_text
                else:
                    return ""
            except sr.UnknownValueError:  # Fixed typo here
                print(Fore.RED + "\rI am unable to recognize what you said. Please try again.")
            finally:
                print("\r", end="", flush=True)

            # Clear screen after recognizing and translating
            os.system("cls" if os.name == "nt" else "clear")

# Start the threads outside the Speech_To_Text function
stt_thread = threading.Thread(target=Speech_To_Text)
print_thread = threading.Thread(target=print_loop)

# Start threads
stt_thread.start()
print_thread.start()

# Wait for threads to complete
stt_thread.join()
print_thread.join()
