#pip install pywhatkit
import pywhatkit as pw
from TTS_B import speak

def play_music_on_YT(Song_Name):
    Song_Name_1 =Song_Name.replace("open","open").replace("song","").replace("play","").replace("on youtube","").replace("youtube","").replace(" ","").strip()
    pw.playonyt(Song_Name_1)
    speak(f"playing {Song_Name_1} on youtube Sir")
