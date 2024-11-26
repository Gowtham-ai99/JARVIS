from Automation.Open_WEB import openweb
from Automation.OpenApp import Open_App
from Automation.Play_Music_spotify import play_music_on_spotify
from Automation.Play_Music_YT import play_music_on_YT
from TTS_B import speak
import pyautogui
import time
from Automation.tab_automation import perform_browser_action
from Automation.scroll_system import perform_scroll_action
def close():
    pyautogui.hotkey('alt','f4')

def close_tabs():
    pyautogui.hotkey('ctrl', 'w')
def search(text):
    pyautogui.press('/')
    time.sleep(0.3)
    pyautogui.write(text)
    pyautogui.write (" ")
    time.sleep(0.3)
    pyautogui.press('enter')
def open_Brain(text):
   
    text = text.lower()
    if "website" in text or "website named" in text:
        text = text.replace("website", "").replace("open", "").replace("named", "").strip()
        openweb(text)
        return "Opening website..."
    else:
        text = text.replace("app", "").replace("open", "").replace("named", "").strip()
        Open_App(text)
        return "Opening app..."
    

def automation_Brain(text):
    if "new tab" in text:
        pyautogui.hotkey('ctrl', 't')
        speak("New tab opened Sir")
        return "Opening new tab..."
    elif text.startswith("open"):
        open_Brain(text)
    elif text.startswith ("search" or "search for"):
        text = text.replace("search for", "").replace("search", "").strip()
        search(text)
 
    elif "play" in text or "song" in text:
        if "spotify" in text:
            play_music_on_spotify(text)
        elif "youtube" in text:
            play_music_on_YT(text)
        else:
            play_music_on_YT(text)
    else:
        perform_browser_action(text)
        perform_scroll_action(text)
        

   # elif "close" in text :
       # close()
       # speak("successfully closed application  Sir")
        #return "Closing..."        
