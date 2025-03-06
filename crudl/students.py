import csv
import math
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem, QMessageBox
from PyQt5.QtCore import  QPropertyAnimation, QPoint, QEasingCurve, QRegularExpression, Qt
from crudl.colleges import *
from crudl.programs import *
from ui_main import Ui_MainWindow

def add_student(self):
        id = self.ui.lineEdit_4.text()
        first_name = self.ui.lineEdit_5.text()
        last_name = self.ui.lineEdit_6.text()
        yearlvl = self.ui.comboBox.currentText()
        gender = self.ui.comboBox_2.currentText()
        programcode = self.ui.comboBox_3.currentText()

        id_valid = QRegularExpression(r"^\d{4}-\d{4}$")
        name_pattern = QRegularExpression(r"^[A-Za-z][A-Za-z\s]*$")

        if not id_valid.match(id).hasMatch():
             QMessageBox.warning(self, "Input Error", "Invalid ID format! Must be YYYY-NNNN.")
             return
        
        if not name_pattern.match(first_name).hasMatch() or not name_pattern.match(last_name).hasMatch():
            QMessageBox.warning(self, "Input Error", "First and Last Name must contain at least one letter/must not start with space!")
            return

        if not is_id_unique(self, id):
            QMessageBox.warning(self, "Duplicate ID", "ID already exists!")
            return
        with open("csv/students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([id, first_name, last_name, yearlvl, gender, programcode])

        row_position = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(row_position)
        self.ui.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(id))
        self.ui.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(first_name))
        self.ui.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(last_name))
        self.ui.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(yearlvl))
        self.ui.tableWidget_2.setItem(row_position, 4, QTableWidgetItem(gender))
        self.ui.tableWidget_2.setItem(row_position, 5, QTableWidgetItem(programcode))

        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.comboBox_3.setCurrentIndex(0)
        sfeedback_anim(self, "Student Added")
    
def is_id_unique(self, student_id):
        with open("csv/students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row and row[0] == student_id:  
                    return False
        return True
    
def load_students_from_csv(self):
        with open("csv/students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if row:
                    row_position = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(row_position)
                    for col, data in enumerate(row):
                        self.ui.tableWidget_2.setItem(row_position, col, QTableWidgetItem(data))
        
    

def search_student(self):
        search_stud = self.ui.Studsearch.text().strip().lower()
        student_filter = self.ui.drop_search_2.currentText()
        self.ui.tableWidget_2.setRowCount(0)
        
        with open("csv/students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            column_index = None

            if student_filter in header:
                column_index = header.index(student_filter)
            
            if not search_stud:
                load_students_from_csv(self)
                return
            
            for row_data in reader:
                if column_index is not None:
                    if search_stud in row_data[column_index].lower():
                        row_position = self.ui.tableWidget_2.rowCount()
                        self.ui.tableWidget_2.insertRow(row_position)
                        for col, cell in enumerate(row_data):
                            self.ui.tableWidget_2.setItem(row_position, col, QTableWidgetItem(cell))


def sort_student(self):
        selected_column_name = self.ui.drop_sort_2.currentText()
        header_label = [self.ui.tableWidget_2.horizontalHeaderItem(i).text() for i in range (self.ui.tableWidget_2.columnCount())]

        if selected_column_name in header_label:
            column_index = header_label.index(selected_column_name)
            self.ui.tableWidget_2.sortItems(column_index)

def delete_student(self, dialog):
        selected_row = self.ui.tableWidget_2.currentRow()

        if selected_row != -1:
            student_id_item = self.ui.tableWidget_2.item(selected_row, 0)
            if student_id_item:
                student_id = student_id_item.text()

                self.ui.tableWidget_2.removeRow(selected_row)
                update_stud(self, student_id)
                sfeedback_anim(self, "Student Deleted")

        dialog.close()

        

def sfeedback_anim(self, message):

        self.ui.feedback.setText(message)
        self.ui.feedback.show()
        self.anim = QPropertyAnimation(self.ui.feedback, b"pos")
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        X = math.floor(self.width() / 2) - 50
        startY = 0 - self.height()
        endY = 60
        self.ui.feedback.move(X, startY)

        self.anim.setStartValue(QPoint(X, startY))
        self.anim.setEndValue(QPoint(X, endY))
        self.anim.setDuration(400)

        threading.Timer(2, lambda: self.ui.feedback.hide()).start()
        self.anim.start()

def confirm_del(self):
        dialog = QtWidgets.QDialog(self.parent())
        dialog.setStyleSheet(self.styleSheet())
        dialog.setWindowTitle("Edit College")
        dialog.setFixedSize(400, 100)
        dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Close Button
        close_btn = QtWidgets.QPushButton(dialog)
        close_btn.setGeometry(370, 5, 24, 24)
        close_btn.setStyleSheet("background: none; color: white; border: none;")
        close_btn.setIcon(QtGui.QIcon("icon/Close.svg"))
        close_btn.setIconSize(QtCore.QSize(24, 24))
        close_btn.clicked.connect(dialog.close)

        
        dialog.oldPos = None
        def mousePressEvent(event):
            if event.button() == QtCore.Qt.LeftButton:
                dialog.oldPos = event.globalPos()
    
        def mouseMoveEvent(event):
            if dialog.oldPos:
                delta = event.globalPos() - dialog.oldPos
                dialog.move(dialog.x() + delta.x(), dialog.y() + delta.y())
                dialog.oldPos = event.globalPos()

        def mouseReleaseEvent(event):
            dialog.oldPos = None

        dialog.mousePressEvent = mousePressEvent
        dialog.mouseMoveEvent = mouseMoveEvent
        dialog.mouseReleaseEvent = mouseReleaseEvent

        self.condel = QtWidgets.QLabel("Are you sure you want to delete this student?", dialog)
        self.condel.setGeometry(QtCore.QRect(10, 30, 400, 20))
        self.condel.setFont(QtGui.QFont("Arial", 10))
        self.condel.setStyleSheet("color: white; font-weight:bold;")
        self.condel.setAlignment(Qt.AlignCenter)
        self.yesbut = QtWidgets.QPushButton("YES", dialog)
        self.yesbut.setGeometry(QtCore.QRect(160, 60, 93, 28))
        self.yesbut.setObjectName("yesbut")
        self.yesbut.setFont(QtGui.QFont("Arial", 10))
        self.yesbut.setStyleSheet("color: white; font-weight:bold;")
        self.yesbut.clicked.connect(lambda: delete_student(self, dialog))

        dialog.exec()
