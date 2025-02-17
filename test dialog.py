from PyQt5 import QtWidgets

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)  # This is the actual QWidget
        self.MainWindow.setCentralWidget(self.centralwidget)

        # Example Edit button setup
        self.Editbtn = QtWidgets.QPushButton("Edit", self.centralwidget)
        self.Editbtn.clicked.connect(self.open_edit_dialog)
        
    def open_edit_dialog(self):
        # Use self.MainWindow (the actual QMainWindow) as the parent for the dialog
        dialog = QtWidgets.QDialog(self.MainWindow)  # Pass the actual QMainWindow, not Ui_MainWindow
        dialog.setWindowTitle("Edit Student Information")
        
        # Add layout and widgets to the dialog
        layout = QtWidgets.QVBoxLayout(dialog)
        label = QtWidgets.QLabel("Enter new student information:")
        layout.addWidget(label)

        input_field = QtWidgets.QLineEdit()
        layout.addWidget(input_field)

        save_button = QtWidgets.QPushButton("Save")
        layout.addWidget(save_button)

        # Show the dialog
        dialog.exec_()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Pass the QMainWindow instance to setupUi

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
