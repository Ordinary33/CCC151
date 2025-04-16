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
    student_id = self.ui.lineEdit_4.text()
    first_name = self.ui.lineEdit_5.text()
    last_name = self.ui.lineEdit_6.text()
    yearlvl = self.ui.comboBox.currentText()
    gender = self.ui.comboBox_2.currentText()
    program_code = self.ui.comboBox_3.currentText()

    id_valid = QRegularExpression(r"^\d{4}-\d{4}$")
    name_pattern = QRegularExpression(r"^[A-Za-z][A-Za-z\s]*$")

    if not id_valid.match(student_id).hasMatch():
        QMessageBox.warning(self, "Input Error", "Invalid ID format! Must be YYYY-NNNN.")
        return

    if not name_pattern.match(first_name).hasMatch() or not name_pattern.match(last_name).hasMatch():
        QMessageBox.warning(self, "Input Error", "First and Last Name must contain at least one letter/must not start with space!")
        return

    if not is_id_unique(self, student_id):
        QMessageBox.warning(self, "Duplicate ID", "ID already exists!")
        return

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()

        query = """INSERT INTO students (student_id, first_name, last_name, year_level, gender, program_code)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (student_id, first_name, last_name, yearlvl, gender, program_code))
        connection.commit()

        # Add student data to the table
        row_position = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(row_position)
        self.ui.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(student_id))
        self.ui.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(first_name))
        self.ui.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(last_name))
        self.ui.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(yearlvl))
        self.ui.tableWidget_2.setItem(row_position, 4, QTableWidgetItem(gender))
        self.ui.tableWidget_2.setItem(row_position, 5, QTableWidgetItem(program_code))

        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.comboBox_3.setCurrentIndex(0)
        sfeedback_anim(self, "Student Added")

    except mysql.connector.Error as e:
        QMessageBox.critical(self, "Database Error", f"Failed to add student: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    
def is_id_unique(self, student_id):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students WHERE student_id = %s", (student_id,))
        result = cursor.fetchone()
        return result[0] == 0

    except mysql.connector.Error as e:
        traceback.print_exc()
        QMessageBox.critical(self, "Database Error", f"Failed to check student ID: {e}")
        return False

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    
def load_students(self):
    self.ui.tableWidget_2.setRowCount(0)
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT student_id, first_name, last_name, year_level, gender, program_code FROM students")
        for row in cursor.fetchall():
            row_position = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(row_position)
            for col, data in enumerate(row):
                self.ui.tableWidget_2.setItem(row_position, col, QTableWidgetItem(str(data)))

    except mysql.connector.Error as e:
        traceback.print_exc()
        QMessageBox.critical(self, "Database Error", f"Failed to load students: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

        

def search_student(self):
    search_stud = self.ui.Studsearch.text().strip().lower()
    student_filter = self.ui.drop_search_2.currentText()
    self.ui.tableWidget_2.setRowCount(0)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()

        if student_filter == "ID #":
            filter_column = "student_id"
        elif student_filter == "First Name":
            filter_column = "first_name"
        elif student_filter == "Last Name":
            filter_column = "last_name"
        elif student_filter == "Year Level":
            filter_column = "year_level"
        elif student_filter == "Gender":
            filter_column = "gender"
        elif student_filter == "Program Code":
            filter_column = "program_code"
        else:
            filter_column = None

        if not search_stud:
            query = "SELECT student_id, first_name, last_name, year_level, gender, program_code FROM students"
        else:
            if filter_column:
                query = f"SELECT student_id, first_name, last_name, year_level, gender, program_code FROM students WHERE {filter_column} LIKE %s"
                search_stud = f"%{search_stud}%"
            else:
                query = "SELECT student_id, first_name, last_name, year_level, gender, program_code FROM students"

        cursor.execute(query, (search_stud,) if search_stud else ())
        results = cursor.fetchall()

        for row_data in results:
            row_position = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(row_position)
            for col, cell in enumerate(row_data):
                self.ui.tableWidget_2.setItem(row_position, col, QTableWidgetItem(str(cell)))

    except Error as e:
        QMessageBox.critical(self, "Database Error", f"Failed to search students: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()



def sort_student(self):
        selected_column_name = self.ui.drop_sort_2.currentText()
        header_label = [self.ui.tableWidget_2.horizontalHeaderItem(i).text() for i in range (self.ui.tableWidget_2.columnCount())]

        if selected_column_name in header_label:
            column_index = header_label.index(selected_column_name)
            self.ui.tableWidget_2.sortItems(column_index)

def delete_student(self, dialog):
    selected_row = self.ui.tableWidget_2.currentRow()

    if selected_row == -1:
        return

    student_id_item = self.ui.tableWidget_2.item(selected_row, 0)
    if student_id_item:
        student_id = student_id_item.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="student_information_system"
            )
            cursor = connection.cursor()

            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            connection.commit()

            self.ui.tableWidget_2.removeRow(selected_row)
            update_student_combobox(self)
            sfeedback_anim(self, "Student Deleted")

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to delete student: {e}")

        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

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
