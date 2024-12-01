import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify setup
SPOTIFY_CLIENT_ID = '57fe10273793431c9ceddde4052ef4ff'
SPOTIFY_CLIENT_SECRET = 'db6549ba324742479cf6229f6049266d'
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-playback-state"))

# Function to set Spotify volume
def set_spotify_volume(level):
    try:
        spotify.volume(int(level * 100))  # Spotify volume: 0-100 scale
    except Exception as e:
        print(f"Error adjusting Spotify volume: {e}")

# Function to check if another app is playing audio
def is_other_audio_playing(ignore_process="Spotify.exe"):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() != ignore_process:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if volume.GetMasterVolume() > 0:  # Check if volume > 0
                return True
    return False

# Monitor other playback and adjust Spotify volume
def monitor_and_adjust_spotify():
    try:
        while True:
            if is_other_audio_playing():
                set_spotify_volume(0.2)  # Lower Spotify volume (20%)
            else:
                set_spotify_volume(1.0)  # Restore Spotify volume (100%)
            time.sleep(1)  # Check every second
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    monitor_and_adjust_spotify()