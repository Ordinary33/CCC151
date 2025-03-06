import sys
import csv
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame
from PyQt5 import QtCore, QtGui
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

        # Minimize Button
        self.min_btn = QPushButton(self.ui.frame)
        self.min_btn.setGeometry(self.width() - 80, 10, 30, 30)
        self.min_btn.setStyleSheet("background: none; color: white; border: none; font-size: 16px;")
        self.min_btn.setIcon(QtGui.QIcon("icon/Minimize.svg"))
        self.min_btn.setIconSize(QtCore.QSize(24, 24))
        self.min_btn.clicked.connect(self.showMinimized)

        # Close Button
        self.close_btn = QPushButton(self.ui.frame)
        self.close_btn.setGeometry(self.width() - 40, 10, 30, 30)
        self.close_btn.setStyleSheet("background: none; color: white; border: none; font-size: 16px;")
        self.close_btn.setIcon(QtGui.QIcon("icon/Close.svg"))
        self.close_btn.setIconSize(QtCore.QSize(24, 24))
        self.close_btn.clicked.connect(self.close)

        # Window Dragging
        self.oldPos = None

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
        self.ui.Removebtn_2.clicked.connect(lambda: confirm_del(self))

        #Add College button
        self.ui.pushButton_2.clicked.connect(lambda: add_college(self))
        
        #Search College button
        self.ui.SearchBtn.clicked.connect(lambda: search_college(self))

        #Sort College
        self.ui.drop_sort.currentIndexChanged.connect(lambda: sort_college(self))

        #Delete College
        self.ui.Removebtn.clicked.connect(lambda: confirm_delc(self))

        #Add Program button
        self.ui.pushButton_3.clicked.connect(lambda: add_program(self))

        #Search Program button
        self.ui.SearchBtn_3.clicked.connect(lambda: search_program(self))

        #Sort Program
        self.ui.drop_sort_3.currentIndexChanged.connect(lambda: sort_program(self))

        #Delete Program
        self.ui.Removebtn_3.clicked.connect(lambda: confirm_delp(self))

        self.show()


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = event.globalPos() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None

        
        
def display():
    print("Hello")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # with open("styles.qss", "r") as file:
    #     app.setStyleSheet(file.read())
    sys.exit(app.exec_())
