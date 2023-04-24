import os
import sys
import logging
from dotenv import load_dotenv


# Define Logger class to redirect stdout and stderr to a log file
class Logger(object):
    def __init__(self, log_file="log.txt"):
        self.terminal_stdout = sys.stdout
        self.terminal_stderr = sys.stderr
        self.log = open(log_file, "a")
        
        # Configure logging
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)

    def write(self, message):
        self.terminal_stdout.write(message)
        self.log.write(message)

    def flush(self):
        pass

    def write_error(self, message):
        self.terminal_stderr.write(message)
        self.log.write(message)

    def flush_error(self):
        pass

# Redirect stdout and stderr to log file using Logger class
log_file = "myAssistant.log"
sys.stdout = Logger(log_file)
sys.stderr = sys.stdout

# Load environment variables from .env file
load_dotenv()
