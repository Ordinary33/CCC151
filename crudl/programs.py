import csv
import math
import threading
import mysql.connector
from mysql.connector import Error
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

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO programs (program_code, program_name, college_code) VALUES (%s, %s, %s)",
            (code, program_name, college_code)
        )
        connection.commit()

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

    except mysql.connector.Error as e:
        traceback.print_exc()
        QMessageBox.critical(self, "Database Error", f"Failed to add program: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def is_progcode_unique(self, program_code):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM programs WHERE program_code = %s", (program_code,))
        result = cursor.fetchone()
        return result[0] == 0

    except mysql.connector.Error as e:
        traceback.print_exc()
        QMessageBox.critical(self, "Database Error", f"Failed to check program code: {e}")
        return False

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    
def load_programs(self):
    self.ui.tableWidget_3.setRowCount(0)
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT program_code, program_name, college_code FROM programs")
        for row in cursor.fetchall():
            row_position = self.ui.tableWidget_3.rowCount()
            self.ui.tableWidget_3.insertRow(row_position)
            for col, data in enumerate(row):
                self.ui.tableWidget_3.setItem(row_position, col, QTableWidgetItem(str(data)))

    except mysql.connector.Error as e:
        traceback.print_exc()
        QMessageBox.critical(self, "Database Error", f"Failed to load programs: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def update_program_combbox(self):
        self.ui.comboBox_3.clear()
        for row in range(self.ui.tableWidget_3.rowCount()):  
            program_code = self.ui.tableWidget_3.item(row, 0).text()
            self.ui.comboBox_3.addItem(program_code)

def search_program(self):
    search_prog = self.ui.lineEdit_3.text().strip().lower()
    program_filter = self.ui.drop_search_3.currentText()
    self.ui.tableWidget_3.setRowCount(0)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()

        if program_filter == "Code":
            filter_column = "program_code"
        elif program_filter == "Name":
            filter_column = "program_name"
        elif program_filter == "College Code":
            filter_column = "college_code"
        else:
            filter_column = None

        if not search_prog:
            query = "SELECT program_code, program_name, college_code FROM programs"
        else:
            if filter_column:
                query = f"SELECT program_code, program_name, college_code FROM programs WHERE {filter_column} LIKE %s"
                search_prog = f"%{search_prog}%"
            else:
                query = "SELECT program_code, program_name, college_code FROM programs"

        cursor.execute(query, (search_prog,) if search_prog else ())
        results = cursor.fetchall()

        for row_data in results:
            row_position = self.ui.tableWidget_3.rowCount()
            self.ui.tableWidget_3.insertRow(row_position)
            for col, cell in enumerate(row_data):
                self.ui.tableWidget_3.setItem(row_position, col, QTableWidgetItem(str(cell)))

    except Error as e:
        QMessageBox.critical(self, "Database Error", f"Failed to search programs: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def sort_program(self):
        selected_column_name = self.ui.drop_sort_3.currentText()
        header_label = [self.ui.tableWidget_3.horizontalHeaderItem(i).text() for i in range (self.ui.tableWidget_3.columnCount())]

        if selected_column_name in header_label:
            column_index = header_label.index(selected_column_name)
            self.ui.tableWidget_3.sortItems(column_index)

def delete_program(self, dialog):
    from crudl.students import load_students
    selected_row = self.ui.tableWidget_3.currentRow()

    if selected_row == -1:
        return

    program_code_item = self.ui.tableWidget_3.item(selected_row, 0)
    if program_code_item:
        program_code = program_code_item.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="student_information_system"
            )
            cursor = connection.cursor()

            
            cursor.execute("UPDATE students SET program_code = NULL WHERE program_code = %s", (program_code,))
            connection.commit()

            
            cursor.execute("DELETE FROM programs WHERE program_code = %s", (program_code,))
            connection.commit()

            
            self.ui.tableWidget_3.removeRow(selected_row)

            
            update_program_combbox(self)

            pfeedback_anim(self, "Program Deleted")
            load_students(self)

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to delete program: {e}")

        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    dialog.close()


def prog_delete(self, program_code):
    for row in range(self.ui.tableWidget_2.rowCount()):
        student_program_item = self.ui.tableWidget_2.item(row, 5)
        if student_program_item and student_program_item.text() == program_code:
            student_program_item.setText("None")

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()

        
    except Error as e:
        QMessageBox.critical(self, "Database Error", f"Failed to update students after program deletion: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


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