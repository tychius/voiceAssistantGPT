import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define Logger class to redirect stdout to a log file


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("log.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


# Redirect stdout to log file using Logger class
sys.stdout = Logger()
