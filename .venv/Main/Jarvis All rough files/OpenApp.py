import pyautogui as gui
import subprocess
import time

def Open_App(text):
    try:
        subprocess.run(text)
    except Exception as e:
        gui.press("win")
        time.sleep(0.1)
        gui.write(text)
        time.sleep(0.1)
        gui.press("enter")
