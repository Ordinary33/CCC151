import csv
import mysql.connector
from mysql.connector import Error
import traceback
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem, QMessageBox
from PyQt5.QtCore import  QPropertyAnimation, QPoint, QEasingCurve, QRegularExpression, Qt
from crudl.programs import *
from crudl.students import *

def add_college(self):
    code = self.ui.lineEdit_7.text()
    college_name = self.ui.lineEdit_8.text()
    name_pattern = QRegularExpression(r"^[A-Za-z][A-Za-z\s]*$")

    if not name_pattern.match(code).hasMatch() or not name_pattern.match(college_name).hasMatch():
        QMessageBox.warning(self, "Input Error", "Code and College Name must contain at least one letter/must not start with space!")
        return

    if not code or not college_name:
        QMessageBox.warning(self, "Input Error", "All Fields must be filled!")
        return

    if not is_collcode_unique(self, code):
        QMessageBox.warning(self, "Duplicate Code", "College Code already exists!")
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
            "INSERT INTO colleges (college_code, college_name) VALUES (%s, %s)",
            (code, college_name)
        )
        connection.commit()
        print("inserted successfully")

        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(code))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(college_name))

        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        update_college_combbox(self)
        cfeedback_anim(self, "College Added")

    except mysql.connector.Error as e:
        print("MySQL error:", e)
        QMessageBox.critical(self, "Database Error", f"Failed to add college: {e}")
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def is_collcode_unique(self, code):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM colleges WHERE college_code = %s", (code,))
        result = cursor.fetchone()
        
        if result[0] > 0:
            return False  
        return True  

    except Error as e:
        print(f"Error checking college code uniqueness: {e}")
        return False  
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
  

def load_colleges(self):
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()

        # Execute a query to fetch all colleges
        cursor.execute("SELECT college_code, college_name FROM colleges")
        rows = cursor.fetchall()

        # Clear the table before inserting new data
        self.ui.tableWidget.setRowCount(0)

        # Insert rows into the table widget
        for row in rows:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(row[0]))  # college_code
            self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(row[1]))  # college_name

    except Error as e:
        QMessageBox.critical(self, "Database Error", f"Failed to load colleges: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    

def search_college(self):
    search_coll = self.ui.lineEdit.text().strip().lower()
    college_filter = self.ui.drop_search.currentText()
    self.ui.tableWidget.setRowCount(0)
    
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()

        # Define the column to filter based on the dropdown selection
        if college_filter == "Code":
            filter_column = "college_code"
        elif college_filter == "Name":
            filter_column = "college_name"
        else:
            filter_column = None
        
        if not search_coll:  # If no search term, show all colleges
            query = "SELECT college_code, college_name FROM colleges"
        else:
            if filter_column:
                query = f"SELECT college_code, college_name FROM colleges WHERE {filter_column} LIKE %s"
                search_coll = f"%{search_coll}%"  # Add wildcard for partial matching
            else:
                query = "SELECT college_code, college_name FROM colleges"
            
        # Execute the query
        cursor.execute(query, (search_coll,) if search_coll else ())
        results = cursor.fetchall()

        # Populate the table with search results
        for row_data in results:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            for col, cell in enumerate(row_data):
                self.ui.tableWidget.setItem(row_position, col, QTableWidgetItem(str(cell)))

    except Error as e:
        QMessageBox.critical(self, "Database Error", f"Failed to search colleges: {e}")
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def sort_college(self):
        selected_column_name = self.ui.drop_sort.currentText()
        header_label = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range (self.ui.tableWidget.columnCount())]

        if selected_column_name in header_label:
            column_index = header_label.index(selected_column_name)
            self.ui.tableWidget.sortItems(column_index)

def delete_college(self, dialog):
    selected_row = self.ui.tableWidget.currentRow()

    if selected_row == -1:
        return  # No row selected, so exit

    college_code_item = self.ui.tableWidget.item(selected_row, 0)
    if college_code_item:
        college_code = college_code_item.text()

        # Remove the row from the table widget
        self.ui.tableWidget.removeRow(selected_row)

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="student_information_system"
            )
            cursor = connection.cursor()

            # Update programs table: set college_code to NULL for programs linked to the deleted college
            cursor.execute("UPDATE programs SET college_code = NULL WHERE college_code = %s", (college_code,))
            connection.commit()

            # Now, delete the college
            cursor.execute("DELETE FROM colleges WHERE college_code = %s", (college_code,))
            connection.commit()

            # Provide feedback after deletion
            cfeedback_anim(self, "College Deleted")
            load_programs(self)


        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to delete college: {e}")

        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    dialog.close()
    
def update_college_combbox(self):
        self.ui.comboBox_4.clear()
        for row in range(self.ui.tableWidget.rowCount()):  
            college_code = self.ui.tableWidget.item(row, 0).text()
            self.ui.comboBox_4.addItem(college_code)

def college_delete(self, college_code):
    for row in range(self.ui.tableWidget_2.rowCount()):
        student_college_item = self.ui.tableWidget_2.item(row, 4)  # Assuming college code is in column 4
        if student_college_item and student_college_item.text() == college_code:
            student_college_item.setText("None")
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        cursor = connection.cursor()

        # Update programs table: set college_code to 'None' for programs linked to the deleted college
        cursor.execute("UPDATE programs SET college_code = NULL WHERE college_code = %s", (college_code,))

        # Commit changes to the database
        connection.commit()
        
    except Error as e:
        QMessageBox.critical(self, "Database Error", f"Failed to update related records after college deletion: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

            
def cfeedback_anim(self, message):

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

def confirm_delc(self):
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

        self.condel = QtWidgets.QLabel("Are you sure you want to delete this college?", dialog)
        self.condel.setGeometry(QtCore.QRect(10, 30, 400, 20))
        self.condel.setFont(QtGui.QFont("Arial", 10))
        self.condel.setStyleSheet("color: white; font-weight:bold;")
        self.condel.setAlignment(Qt.AlignCenter)
        self.yesbut = QtWidgets.QPushButton("YES", dialog)
        self.yesbut.setGeometry(QtCore.QRect(160, 60, 93, 28))
        self.yesbut.setObjectName("yesbut")
        self.yesbut.setFont(QtGui.QFont("Arial", 10))
        self.yesbut.setStyleSheet("color: white; font-weight:bold;")
        self.yesbut.clicked.connect(lambda: delete_college(self, dialog))

        dialog.exec()