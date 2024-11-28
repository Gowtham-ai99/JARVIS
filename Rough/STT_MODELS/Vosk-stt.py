import os
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# Initialize Vosk Model (Ensure the model path is correct)
MODEL_PATH = r"C:\\Users\\User\\Documents\\Python\\J.A.R.V.I.S\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15" 

# Verify the model directory exists
if not os.path.exists(MODEL_PATH):
    print(f"Model not found at {MODEL_PATH}. Please download it first!")
    exit(1)

# Load the Vosk model
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
recognizer.SetWords(True)

# Audio configuration
sample_rate = 16000
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    """Callback to handle incoming audio data."""
    if status:
        print(f"Audio error: {status}")
    audio_queue.put(bytes(indata))

def save_to_file(text):
    """Save recognized text to input.txt."""
    with open("input.txt", "w") as file:
        file.write(text)
    print("Text saved to input.txt")

def listen_continuously():
    """Listen continuously and process speech."""
    print("Listening for speech... Say 'Jarvis' to save text.")
    with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = eval(result).get("text", "")
                if text:  # If text is not empty
                    if "jarvis" in text.lower():
                        print(f"Keyword detected: {text}")
                        save_to_file(text)
                    else:
                        print(f"Text: {text}")  # Print recognized text

if __name__ == "__main__":
    try:
        listen_continuously()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
