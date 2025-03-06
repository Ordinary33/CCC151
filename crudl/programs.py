import csv
import math
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem, QMessageBox
from PyQt5.QtCore import  QPropertyAnimation, QPoint, QEasingCurve, QRegularExpression, Qt
from crudl.students import *
from crudl.colleges import *

def add_program(self):
        code = self.ui.lineEdit_9.text()
        program_name = self.ui.lineEdit_10.text()
        college_code = self.ui.comboBox_4.currentText()
        name_pattern = QRegularExpression(r"^[A-Za-z][A-Za-z\s]*$")

        if not name_pattern.match(code).hasMatch() or not name_pattern.match(program_name).hasMatch():
              QMessageBox.warning(self, "Input Error", "Code and Program Name must contain at least one letter/must not start with space!")
              return
        
        if not is_progcode_unique(self, code):
            QMessageBox.warning(self, "Duplicate Code", "Program code already exists!")
            return
        
        with open("csv/programs.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([code, program_name, college_code])

        row_position = self.ui.tableWidget_3.rowCount()
        self.ui.tableWidget_3.insertRow(row_position)
        self.ui.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(code))
        self.ui.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(program_name))
        self.ui.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(college_code))


        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.comboBox_4.setCurrentIndex(0)
        update_program_combbox(self)
        pfeedback_anim(self, "Program Added")

def is_progcode_unique(self, program_code):
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row and row[0] == program_code:  
                    return False
        return True
    
def load_programs_from_csv(self):
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if row:
                    row_position = self.ui.tableWidget_3.rowCount()
                    self.ui.tableWidget_3.insertRow(row_position)
                    for col, data in enumerate(row):
                        self.ui.tableWidget_3.setItem(row_position, col, QTableWidgetItem(data))

def update_program_combbox(self):
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItem("None")
        for row in range(self.ui.tableWidget_3.rowCount()):  
            program_code = self.ui.tableWidget_3.item(row, 0).text()
            self.ui.comboBox_3.addItem(program_code)

def search_program(self):
        search_prog = self.ui.lineEdit_3.text().strip().lower()
        program_filter = self.ui.drop_search_3.currentText()
        self.ui.tableWidget_3.setRowCount(0)
        
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            column_index = None

            if program_filter in header:
                column_index = header.index(program_filter)
            
            if not search_prog:
                load_programs_from_csv(self)
                return
            
            for row_data in reader:
                if column_index is not None:
                    if search_prog in row_data[column_index].lower():
                        row_position = self.ui.tableWidget_3.rowCount()
                        self.ui.tableWidget_3.insertRow(row_position)
                        for col, cell in enumerate(row_data):
                            self.ui.tableWidget_3.setItem(row_position, col, QTableWidgetItem(cell))

def sort_program(self):
        selected_column_name = self.ui.drop_sort_3.currentText()
        header_label = [self.ui.tableWidget_3.horizontalHeaderItem(i).text() for i in range (self.ui.tableWidget_3.columnCount())]

        if selected_column_name in header_label:
            column_index = header_label.index(selected_column_name)
            self.ui.tableWidget_3.sortItems(column_index)

def delete_program(self, dialog):
        selected_row = self.ui.tableWidget_3.currentRow()

        if selected_row == -1:
            return
        program_code_item = self.ui.tableWidget_3.item(selected_row, 0)
        if program_code_item:
            program_code = program_code_item.text()
            self.ui.tableWidget_3.removeRow(selected_row)
            update_prog(self, program_code)
            prog_delete(self, program_code)
            pfeedback_anim(self, "Program Deleted")

        dialog.close()

def prog_delete(self, program_code):
        for row in range(self.ui.tableWidget_2.rowCount()):
            student_program_item = self.ui.tableWidget_2.item(row, 5)

            if student_program_item and student_program_item.text() == program_code:
                student_program_item.setText("None")

        update_student_delete(self, program_code)

def update_prog(self, program_code):
        rows = []
        with open('csv/programs.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if rows:
            header = rows[0]
            filtered_rows = [header] + [row for row in rows[1:] if row[0] != program_code]

        else:
            filtered_rows = []

        with open('csv/programs.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filtered_rows)

def update_student_delete(self, deleted_program_code):
        with open('csv/students.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if rows:
            header = rows[0]
            for row in rows[1:]:
                if len(row) > 5 and row[5] == deleted_program_code:
                    row[5] = "None"

        with open('csv/students.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)


def pfeedback_anim(self, message):

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

def confirm_delp(self):
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

        self.condel = QtWidgets.QLabel("Are you sure you want to delete this program?", dialog)
        self.condel.setGeometry(QtCore.QRect(10, 30, 400, 20))
        self.condel.setFont(QtGui.QFont("Arial", 10))
        self.condel.setStyleSheet("color: white; font-weight:bold;")
        self.condel.setAlignment(Qt.AlignCenter)
        self.yesbut = QtWidgets.QPushButton("YES", dialog)
        self.yesbut.setGeometry(QtCore.QRect(160, 60, 93, 28))
        self.yesbut.setObjectName("yesbut")
        self.yesbut.setFont(QtGui.QFont("Arial", 10))
        self.yesbut.setStyleSheet("color: white; font-weight:bold;")
        self.yesbut.clicked.connect(lambda: delete_program(self, dialog))

        dialog.exec()