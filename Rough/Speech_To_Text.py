import speech_recognition as sr
import os

def listen_and_transcribe():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    # Recognize speech using Google's Web Speech API
    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        
        # Get the current working directory
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'input.txt')
        
        # Save the transcribed text to 'input.txt'
        with open(file_path, "w") as file:
            file.write(text)
            print(f"Text saved to {file_path}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Run the function
listen_and_transcribe()
