import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from winotify import Notification, audio

def Alert(text):
    icon_path= r"C:\Users\User\Documents\Python\.venv\Jarvis\DATA\logo.png"

    toast= Notification(
    app_id="J.A.R.V.I.S",
    title="🟢",
    msg=text,
    duration="long",
    icon=icon_path,
)

    toast.set_audio(audio.Default,loop= False)

    toast.add_actions(label= "Click me", launch="https://www.google.com")
    toast.add_actions(label= "Dismiss", launch="https://www.google.com")

    toast.show()

