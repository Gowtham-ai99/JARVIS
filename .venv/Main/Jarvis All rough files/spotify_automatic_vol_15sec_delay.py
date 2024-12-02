import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# Function to adjust Spotify volume
def set_spotify_volume(level):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == "spotify.exe":
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(level, None)
            return

# Function to check if any other app is actively playing audio
def is_audio_playing_except_spotify(threshold=0.01):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() != "spotify.exe":
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            audio_session = session.SimpleAudioVolume
            if session.State == 1 and volume.GetMasterVolume() > threshold:
                return True
    return False

# Monitor and adjust Spotify volume dynamically
def monitor_audio_and_control_spotify():
    spotify_volume_reduced = False  # Tracks Spotify's volume state

    try:
        while True:
            audio_playing = is_audio_playing_except_spotify()

            if audio_playing and not spotify_volume_reduced:
                # Lower Spotify's volume
                set_spotify_volume(0.1)
                print("Other audio detected. Lowering Spotify volume.")
                spotify_volume_reduced = True

            elif not audio_playing and spotify_volume_reduced:
                # Restore Spotify's volume
                set_spotify_volume(1.0)
                print("No other audio detected. Restoring Spotify volume.")
                spotify_volume_reduced = False

            time.sleep(0.1)  # Check every 200ms for faster response

    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_audio_and_control_spotify()
