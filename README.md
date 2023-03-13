# Audiobook Maker using Python
This program uses the pyttsx3 library to convert text files into audio files that can be played back as an audiobook.

### Requirements
* Python 3
* pyttsx3 library

### How to Use
* Clone the repository.
* Install the pyttsx3 library using pip install pyttsx3.
* Run the program by executing python audiobook.py in the terminal.
* Enter the file path of the text file you want to convert into an audiobook when prompted.
* If the file exists, the program will read the contents and convert them into audio, which will be played back.
* If the file does not exist, an error message will be displayed.

### Program Explanation
* The program starts by importing the necessary libraries, os and pyttsx3.
* Then, the text-to-speech engine is set up using pyttsx3.init().
* The user is prompted to enter the file path of the text file they want to convert into an audiobook.
* If the file exists, the program reads the contents of the file using the open() method, converts it into audio using the text-to-speech engine, and plays it back using engine.runAndWait().
* If the file does not exist, an error message is displayed.
