# Voice Assistant

A simple voice assistant that uses Google Speech Recognition, GPT, and PyQt5.

## Prerequisites

1. Python 3.6 or higher (only required for running from source)
2. pip (only required for running from source)


## How to Run the Voice Assistant from the Executable

1. Clone or download the repository from GitHub.

2. Set up your OpenAI API key as an environment variable:
   - On Windows:
     1. Press `Win` + `X`, then click on "System".
     2. Click on "Advanced system settings" on the right side.
     3. Click on the "Environment Variables" button near the bottom right.
     4. Click on "New" under "User variables".
     5. Set the variable name to `OPENAI_API_KEY` and the variable value to your OpenAI API key.
     6. Click "OK" to save your changes.
   - On macOS/Linux:
     1. Open your terminal.
     2. Open the `.bash_profile` or `.bashrc` file in a text editor (e.g., `nano ~/.bash_profile` or `nano ~/.bashrc`).
     3. Add the following line, replacing `YOUR_API_KEY` with your actual OpenAI API key:
        ```
        export OPENAI_API_KEY=YOUR_API_KEY
        ```
     4. Save the file and restart your terminal.

3. Run the `main.exe` file by double-clicking it.

## Running the Voice Assistant from Source
## Installation

1. Clone the repository:
git clone https://github.com/tychius/voice_assistant.git

cd voice_assistant


2. Create a virtual environment:
python -m venv venv


3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:
pip install -r requirements.txt


5. Add your OpenAI API key:
Create a file named `.env` in the project's root directory and add the following line, replacing `YOUR_API_KEY` with your actual OpenAI API key:
OPENAI_API_KEY=YOUR_API_KEY


## Usage

1. Ensure your virtual environment is active.

2. Run the main.py script:
python main.py


The voice assistant will start, and a user interface will be displayed. You can interact with the assistant using voice commands.
