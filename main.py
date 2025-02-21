import sys
import platform
import csv
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem



from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        with open("styles.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.load_students_from_csv()
        self.load_colleges_from_csv()
        self.load_programs_from_csv()
        self.update_college_combbox()
        self.update_program_combbox()
        # View Student Page
        self.ui.ViewStudent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

         # View College Pagec
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
        self.ui.pushButton.clicked.connect(self.add_student)

        #Search Student button
        self.ui.SearchBtn_2.clicked.connect(self.search_student)

        #Sort Student
        self.ui.drop_sort_2.currentIndexChanged.connect(self.sort_student)

        #Delete Student
        self.ui.Removebtn_2.clicked.connect(self.delete_student)

        #Add College button
        self.ui.pushButton_2.clicked.connect(self.add_college)
        
        #Search College button
        self.ui.SearchBtn.clicked.connect(self.search_college)

        #Sort College
        self.ui.drop_sort.currentIndexChanged.connect(self.sort_college)

        #Delete College
        self.ui.Removebtn.clicked.connect(self.delete_college)

        #Add Program button
        self.ui.pushButton_3.clicked.connect(self.add_program)

        #Search Program button
        self.ui.SearchBtn_3.clicked.connect(self.search_program)

        #Sort Program
        self.ui.drop_sort_3.currentIndexChanged.connect(self.sort_program)

        #Delete Program
        self.ui.Removebtn_3.clicked.connect(self.delete_program)

        

        
        self.show()

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
        if not self.is_id_unique(id):
            QMessageBox.warning(self, "Duplicate ID", "ID already exists!")
            return
        with open("students.csv", "a", newline="") as file:
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
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row and row[0] == student_id:  
                    return False
        return True
    
    def load_students_from_csv(self):
        with open("students.csv", "r", newline="") as file:
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
        
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            column_index = None

            if student_filter in header:
                column_index = header.index(student_filter)
            
            if not search_stud:
                self.load_students_from_csv()
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
                self.update_stud(student_id)

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
            

    def add_program(self):
        code = self.ui.lineEdit_9.text()
        program_name = self.ui.lineEdit_10.text()
        college_code = self.ui.comboBox_4.currentText()
        
        if not code or not program_name or not college_code:
            QMessageBox.warning(self, "Input Error", "All Fields must be filled!")
            return
        
        if not self.is_progcode_unique(code):
            QMessageBox.warning(self, "Duplicate Code", "Program code already exists!")
            return
        
        with open("programs.csv", "a", newline="") as file:
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
        self.update_program_combbox()

    def is_progcode_unique(self, program_code):
        with open("programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row and row[0] == program_code:  
                    return False
        return True
    
    def load_programs_from_csv(self):
        with open("programs.csv", "r", newline="") as file:
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
        
        with open("programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            column_index = None

            if program_filter in header:
                column_index = header.index(program_filter)
            
            if not search_prog:
                self.load_programs_from_csv()
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
            self.update_prog(program_code)
            self.prog_delete(program_code)

    def prog_delete(self, program_code):
        for row in range(self.ui.tableWidget_2.rowCount()):
            student_program_item = self.ui.tableWidget_2.item(row, 5)

            if student_program_item and student_program_item.text() == program_code:
                student_program_item.setText("None")

        self.update_student_delete(program_code)

    def update_prog(self, program_code):
        rows = []
        with open('programs.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if rows:
            header = rows[0]
            filtered_rows = [header] + [row for row in rows[1:] if row[0] != program_code]

        else:
            filtered_rows = []

        with open('programs.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filtered_rows)

    def update_student_delete(self, deleted_program_code):
        with open('students.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if rows:
            header = rows[0]
            for row in rows[1:]:
                if len(row) > 5 and row[5] == deleted_program_code:
                    row[5] = "None"

        with open('students.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

   

    
def display():
    print("Hello")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
