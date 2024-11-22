import pyautogui 
import time
from TTS_B import speak
import webbrowser


def play_music_on_spotify(song_name):
    
    song_name1 = song_name.lower().replace('open', '').replace('play', '').replace('spotify', '').replace('on', '').strip()
    # Open Spotify and search for the song
    speak(f"playing {song_name1} on Spotify sir")
    webbrowser.open("https://open.spotify.com/search/" + song_name)
    time.sleep(6)  
    pyautogui.click(815,465)# Wait for the search results to load

