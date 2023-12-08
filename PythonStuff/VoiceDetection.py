#!/usr/bin/env python3

import speech_recognition as sr  # Import the speech recognition library

# Capture audio input from the microphone                                                                             
while True:  # Start an infinite loop
    r = sr.Recognizer()  # Create a recognizer object
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Kindly voice out your command!")  # Prompt the user to speak
        audio = r.listen(source)  # Listen for audio input

    try:
        print("Interpreted as: " + r.recognize_google(audio))  # Print the recognized speech
    except sr.UnknownValueError:
        print("Apologies, the audio wasn't clear enough.")  # Handle unrecognized speech
    except sr.RequestError as e:
        print("There was an issue retrieving results. Error: {0}".format(e))  # Handle request errors

    if input("Press q to quit, any other key to continue: ").lower() == 'q':  # Ask the user if they want to quit
        break  # Break the loop if the user inputs 'q'
