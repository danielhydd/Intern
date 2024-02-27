from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QLabel, QPushButton, QDialog, QMessageBox, QLineEdit
from PyQt5 import uic, QtCore
import sys
dateSelectedText = "Date"
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("cal.ui", self)

        # Define our widgets
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "label")
        self.pushButton = self.findChild(QPushButton, "pushButton")

        # Connect the calendar to the function
        self.calendar.selectionChanged.connect(self.grab_date)

        # Connect pushButton to open new window
        self.pushButton.clicked.connect(self.open_new_window)

        # Show The App
        self.show()

    def grab_date(self):
        dateSelected = self.calendar.selectedDate()
        global dateSelectedText
        dateSelectedText = str(dateSelected.toString())
        self.label.setText(str(dateSelected.toString()))

    def open_new_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()


class SecondWindow(QMainWindow):  # Corrected to inherit from QDialog
    def __init__(self):
        super(SecondWindow, self).__init__()
        uic.loadUi("second_window.ui", self)  # Load the UI file for the second window
        self.setWindowTitle("Events") 
        
        self.date_label = QLabel("Events", self)
        global dateSelected
        
        self.date_label.setText(dateSelectedText)
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the center
        font = self.date_label.font()
        font.setPointSize(20)  # Set font size to 20
        font.setBold(True)  # Make text bold
        self.date_label.setFont(font)
        self.date_label.setGeometry(0, 20, self.width(), 50)  #
        
        # Event Name textbox
        self.event_name_label = QLabel("Event Name:", self)
        self.event_name_label.setGeometry(50, 100, 100, 30)
        self.event_name_edit = QLineEdit(self)
        self.event_name_edit.setGeometry(170, 100, 200, 30)

        # Description textbox
        self.description_label = QLabel("Description:", self)
        self.description_label.setGeometry(50, 150, 100, 30)
        self.description_edit = QLineEdit(self)
        self.description_edit.setGeometry(170, 150, 200, 30)

        # Participant Number textbox
        self.participant_label = QLabel("Participant Number:", self)
        self.participant_label.setGeometry(50, 200, 120, 30)
        self.participant_edit = QLineEdit(self)
        self.participant_edit.setGeometry(170, 200, 200, 30)

        # Button to add event
        self.add_event_button = QPushButton("Add Event", self)
        self.add_event_button.setGeometry(50, 250, 200, 50)
        self.add_event_button.clicked.connect(self.show_popup)

    def show_popup(self):
        event_name = self.event_name_edit.text()
        description = self.description_edit.text()
        participant_number = self.participant_edit.text()
        popup_message = f"Event Name: {event_name}\nDescription: {description}\nParticipant Number: {participant_number}"
        QMessageBox.information(self, "Add Event", popup_message)
            


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
