import os
import pyttsx3

# Set up text-to-speech engine
engine = pyttsx3.init()

# Get file path from user input
file_path = input("Enter file path: ")

# Check if file exists
if os.path.exists(file_path):
    # Open file and read contents
    with open(file_path, "r") as f:
        contents = f.read()
    
    # Speak contents using text-to-speech engine
    engine.say(contents)
    engine.runAndWait()
    
else:
    print("File does not exist.")
