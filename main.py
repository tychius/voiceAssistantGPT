import sys
import threading
import openai
import os
from config import Logger
from speech import SpeechAssistant
from gpt import GPTAssistant, response_is_complete
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication
from ui import AssistantUI

# Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Instantiate speech and GPT assistants
speech_assistant = SpeechAssistant()
gpt_assistant = GPTAssistant(api_key)

# Define function to run the voice assistant


def run_assistant():
    # Set maximum number of retries for GPT API call
    max_retries = 3
    while True:
        # Listen for user input and recognize it using speech assistant
        user_input = speech_assistant.listen_and_recognize()
        if user_input:
            # If user says "quit" or "exit", exit the application
            if user_input.lower() in ["quit", "exit"]:
                QApplication.quit()
                break

            # Try to generate a response using GPT API, retrying up to max_retries times if necessary
            retries = 0
            while retries < max_retries:
                response = gpt_assistant.generate_response(user_input)
                if response_is_complete(response):
                    break
                retries += 1

            # If max_retries reached, return an error message
            if retries == max_retries:
                response = "Sorry, I couldn't generate a complete response. Please try again."

            # Speak the response using speech assistant and update UI labels
            speech_assistant.speak(response)
            window.user_said_label.setText(f"You said: {user_input}")
            window.assistant_response_label.setText(f"Assistant: {response}")


# Set attribute for high DPI scaling
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
app = QApplication(sys.argv)

# Create and configure UI window
window = AssistantUI()

primary_screen = QGuiApplication.primaryScreen()
screen_geometry = primary_screen.availableGeometry()
window.setGeometry(screen_geometry.width() - window.sizeHint().width() - 10,
                   30,
                   window.sizeHint().width(),
                   window.sizeHint().height())

# Start assistant in a separate thread and show UI window
threading.Thread(target=run_assistant, daemon=True).start()
window.show()

# Start Qt event loop and exit application when loop exits
sys.exit(app.exec_())
