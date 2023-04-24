from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QSizePolicy
from PyQt5.QtCore import Qt

class CustomLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setWordWrap(True)
        self.setFixedWidth(400)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.setStyleSheet("font-weight: bold; font-size: 10pt;")

class AssistantUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title, flags, and background transparency
        self.setWindowTitle("Personal Assistant")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set up layout for UI
        layout = QVBoxLayout()

        # Add labels for listening status, user input, and assistant response
        self.listening_label = CustomLabel("Listening...")
        self.listening_label.setStyleSheet(
            "color: white; font: 8pt 'Segoe UI'; background-color: rgba(0,0,0,150); padding: 10px; border-radius: 10px;")
        self.listening_label.setText("<b>Listening...</b>")
        layout.addWidget(self.listening_label)

        self.user_said_label = CustomLabel("You said:")
        self.user_said_label.setStyleSheet(
            "color: white; font: 8pt 'Segoe UI'; background-color: rgba(0,0,0,150); padding: 10px; border-radius: 10px;")
        self.user_said_label.setSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.user_said_label.setText("<b>You Said:</b>")
        layout.addWidget(self.user_said_label)

        self.assistant_response_label = CustomLabel("Assistant:")
        self.assistant_response_label.setStyleSheet(
            "color: white; font: 8pt 'Segoe UI'; background-color: rgba(0,0,0,150); padding: 10px; border-radius: 10px;")
        self.assistant_response_label.setSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.assistant_response_label.setText("<b>Assistant:</b>")
        layout.addWidget(self.assistant_response_label)

        # Align layout to top of UI window
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)
