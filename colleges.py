import csv
from PyQt5.QtWidgets import  QTableWidgetItem, QMessageBox
def update_stud(self, deleted_student_id):
        rows = []
        with open('students.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            rows.append(header)  

            for row in reader:
                if row and row[0] != deleted_student_id:
                    rows.append(row)

        with open('students.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def add_college(self):
        code = self.ui.lineEdit_7.text()
        college_name = self.ui.lineEdit_8.text()
        
        if not code or not college_name:
            QMessageBox.warning(self, "Input Error", "All Fields must be filled!")
            return
        
        if not self.is_collcode_unique(code):
            QMessageBox.warning(self, "Duplicate Code", "College Code already exists!")
            return

        with open("colleges.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([code, college_name])

        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(code))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(college_name))


        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.update_college_combbox()

def is_collcode_unique(self, college_code):
        with open("colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row and row[0] == college_code:  
                    return False
        return True
            
def load_colleges_from_csv(self):
        with open("colleges.csv", "r", newline="") as file:
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
        
        with open("colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            column_index = None

            if college_filter in header:
                column_index = header.index(college_filter)
            
            if not search_coll:
                self.load_colleges_from_csv()
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

def delete_college(self):
        selected_row = self.ui.tableWidget.currentRow()

        if selected_row == -1:
            return
        college_code_item = self.ui.tableWidget.item(selected_row, 0)
        if college_code_item:
            college_code = college_code_item.text()
            self.ui.tableWidget.removeRow(selected_row)
            self.update_coll(college_code)
            self.coll_delete(college_code)
    
def coll_delete(self, deleted_college_code):
        for row in range(self.ui.tableWidget_3.rowCount()):
           program_college_item = self.ui.tableWidget_3.item(row, 2)  

           if program_college_item and program_college_item.text() == deleted_college_code:
                program_college_item.setText("None")  

        self.update_prog_delete() 

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

        with open('programs.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            
def update_coll(self, student_id):
        rows = []
        with open('colleges.csv', mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        rows = [row for row in rows if row[0] != student_id]

        with open('colleges.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def update_college_combbox(self):
        self.ui.comboBox_4.clear()
        for row in range(self.ui.tableWidget.rowCount()):  
            college_code = self.ui.tableWidget.item(row, 0).text()
            self.ui.comboBox_4.addItem(college_code)
            
