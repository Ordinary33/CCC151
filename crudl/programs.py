import csv
from PyQt5.QtWidgets import  QTableWidgetItem, QMessageBox
from crudl.students import *
from crudl.colleges import *

def add_program(self):
        code = self.ui.lineEdit_9.text()
        program_name = self.ui.lineEdit_10.text()
        college_code = self.ui.comboBox_4.currentText()
        
        if not code or not program_name or not college_code:
            QMessageBox.warning(self, "Input Error", "All Fields must be filled!")
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

def is_progcode_unique(self, program_code):
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row and row[0].lower() == program_code:  
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

def delete_program(self):
        selected_row = self.ui.tableWidget_3.currentRow()

        if selected_row == -1:
            return
        program_code_item = self.ui.tableWidget_3.item(selected_row, 0)
        if program_code_item:
            program_code = program_code_item.text()
            self.ui.tableWidget_3.removeRow(selected_row)
            update_prog(self, program_code)
            prog_delete(self, program_code)

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

   

    