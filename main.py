import sys
import csv
from PyQt5.QtWidgets import QMainWindow, QApplication
from crudl.students import *
from crudl.programs import *
from crudl.colleges import *

from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        with open("styles.qss", "r") as file:
            self.setStyleSheet(file.read())

        load_students_from_csv(self)
        load_colleges_from_csv(self)
        load_programs_from_csv(self)
        update_college_combbox(self)
        update_program_combbox(self)

        #Toggle Button
        # self.ui.Toggle.clicked.connect()
        # View Student Page
        self.ui.ViewStudent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

         # View College Page
        self.ui.ViewCollege.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # View Programs Page
        self.ui.ViewProgram.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        
        # Add Student Page
        self.ui.AddStudent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
       
        # Add College Page
        self.ui.AddCollege.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        
        # Add Programs Page
        self.ui.AddProgram.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))

        #Add Student button
        self.ui.pushButton.clicked.connect(lambda: add_student(self))

        #Search Student button
        self.ui.SearchBtn_2.clicked.connect(lambda:search_student(self))

        #Sort Student
        self.ui.drop_sort_2.currentIndexChanged.connect(lambda: sort_student(self))

        #Delete Student
        self.ui.Removebtn_2.clicked.connect(lambda: delete_student(self))

        #Add College button
        self.ui.pushButton_2.clicked.connect(lambda: add_college(self))
        
        #Search College button
        self.ui.SearchBtn.clicked.connect(lambda: search_college(self))

        #Sort College
        self.ui.drop_sort.currentIndexChanged.connect(lambda: sort_college(self))

        #Delete College
        self.ui.Removebtn.clicked.connect(lambda: delete_college(self))

        #Add Program button
        self.ui.pushButton_3.clicked.connect(lambda: add_program(self))

        #Search Program button
        self.ui.SearchBtn_3.clicked.connect(lambda: search_program(self))

        #Sort Program
        self.ui.drop_sort_3.currentIndexChanged.connect(lambda: sort_program(self))

        #Delete Program
        self.ui.Removebtn_3.clicked.connect(lambda: delete_program(self))
        
        self.show()

def display():
    print("Hello")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
