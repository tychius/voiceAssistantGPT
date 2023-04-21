import speech_recognition as sr
import pyttsx3

class SpeechAssistant:
    def listen_and_recognize(self):
        # Create speech recognizer and listen for user input
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                # Use Google Speech Recognition API to recognize user input
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except:
                # If speech recognition fails, return None
                print("Sorry, I couldn't understand.")
                return None

    def speak(self, text):
        # Initialize speech synthesis engine and speak text
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # You can adjust the speech rate as needed
        engine.say(text)
        engine.runAndWait()
