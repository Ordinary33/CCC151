import csv
from PyQt5.QtWidgets import  QTableWidgetItem, QMessageBox
from crudl.colleges import *
from crudl.programs import *

def add_student(self):
        id = self.ui.lineEdit_4.text()
        first_name = self.ui.lineEdit_5.text()
        last_name = self.ui.lineEdit_6.text()
        yearlvl = self.ui.comboBox.currentText()
        gender = self.ui.comboBox_2.currentText()
        programcode = self.ui.comboBox_3.currentText()

        if not first_name or not last_name:
            QMessageBox.warning(self, "Input Error", "All fields must be filled!")
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

def delete_student(self):
        selected_row = self.ui.tableWidget_2.currentRow()

        if selected_row != -1:
            student_id_item = self.ui.tableWidget_2.item(selected_row, 0)
            if student_id_item:
                student_id = student_id_item.text()

                self.ui.tableWidget_2.removeRow(selected_row)
                update_stud(self, student_id)