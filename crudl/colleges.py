import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidgetItem, QMessageBox
from PyQt5.QtCore import  QPropertyAnimation, QPoint, QEasingCurve, QRegularExpression, Qt
from crudl.programs import *
from crudl.students import *
def update_stud(self, deleted_student_id):
        rows = []
        with open('csv/students.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            rows.append(header)  

            for row in reader:
                if row and row[0] != deleted_student_id:
                    rows.append(row)

        with open('csv/students.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

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

        with open("csv/colleges.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([code, college_name])

        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(code))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(college_name))


        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        update_college_combbox(self)
        cfeedback_anim(self, "College Added")

def is_collcode_unique(self, college_code):
        with open("csv/colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row and row[0] == college_code:  
                    return False
        return True
            
def load_colleges_from_csv(self):
        with open("csv/colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if row:
                    row_position = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row_position)
                    for col, data in enumerate(row):
                        self.ui.tableWidget.setItem(row_position, col, QTableWidgetItem(data))
    
def search_college(self):
        search_coll = self.ui.lineEdit.text().strip().lower()
        college_filter = self.ui.drop_search.currentText()
        self.ui.tableWidget.setRowCount(0)
        
        with open("csv/colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            column_index = None

            if college_filter in header:
                column_index = header.index(college_filter)
            
            if not search_coll:
                load_colleges_from_csv(self)
                return
            
            for row_data in reader:
                if column_index is not None:
                    if search_coll in row_data[column_index].lower():
                        row_position = self.ui.tableWidget.rowCount()
                        self.ui.tableWidget.insertRow(row_position)
                        for col, cell in enumerate(row_data):
                            self.ui.tableWidget.setItem(row_position, col, QTableWidgetItem(cell))

def sort_college(self):
        selected_column_name = self.ui.drop_sort.currentText()
        header_label = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range (self.ui.tableWidget.columnCount())]

        if selected_column_name in header_label:
            column_index = header_label.index(selected_column_name)
            self.ui.tableWidget.sortItems(column_index)

def delete_college(self, dialog):
        selected_row = self.ui.tableWidget.currentRow()

        if selected_row == -1:
            return
        college_code_item = self.ui.tableWidget.item(selected_row, 0)
        if college_code_item:
            college_code = college_code_item.text()
            self.ui.tableWidget.removeRow(selected_row)
            update_coll(self, college_code)
            coll_delete(self, college_code)
            cfeedback_anim(self, "College Deleted")

        dialog.close()
    
def coll_delete(self, deleted_college_code):
        for row in range(self.ui.tableWidget_3.rowCount()):
           program_college_item = self.ui.tableWidget_3.item(row, 2)  

           if program_college_item and program_college_item.text() == deleted_college_code:
                program_college_item.setText("None")  

        update_prog_delete(self) 

def update_prog_delete(self):
        rows = []
        if self.ui.tableWidget_3.rowCount() > 0:
            header = [self.ui.tableWidget_3.horizontalHeaderItem(col).text() for col in range(self.ui.tableWidget_3.columnCount())]
            rows.append(header)

        for row in range(self.ui.tableWidget_3.rowCount()):
            program_data = []
            for col in range(self.ui.tableWidget_3.columnCount()):
                item = self.ui.tableWidget_3.item(row, col)
                program_data.append(item.text() if item else "None")  
            rows.append(program_data)

        with open('csv/programs.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            
def update_coll(self, student_id):
        rows = []
        with open('csv/colleges.csv', mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        rows = [row for row in rows if row[0] != student_id]

        with open('csv/colleges.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def update_college_combbox(self):
        self.ui.comboBox_4.clear()
        self.ui.comboBox_4.addItem("None")
        for row in range(self.ui.tableWidget.rowCount()):  
            college_code = self.ui.tableWidget.item(row, 0).text()
            self.ui.comboBox_4.addItem(college_code)
            
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