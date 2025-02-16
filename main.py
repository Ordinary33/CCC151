import sys
import platform
import csv
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem



from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.load_students_from_csv()
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

        self.show()

    def add_student(self):
        id = self.ui.lineEdit_4.text()
        first_name = self.ui.lineEdit_5.text()
        last_name = self.ui.lineEdit_6.text()
        yearlvl = self.ui.comboBox.currentText()
        gender = self.ui.comboBox_2.currentText()
        programcode = self.ui.comboBox_3.currentText()

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
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        
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


def display():
    print("Hello")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
