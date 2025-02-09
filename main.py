import sys
import platform
import csv
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


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

        #Delete Student button
        self.ui.Removebtn_2.clicked.connect(self.add_student)

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
            for row in reader:
                if row:
                    row_position = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(row_position)
                    for col, data in enumerate(row):
                        self.ui.tableWidget_2.setItem(row_position, col, QTableWidgetItem(data))
        

    def delete_student(self):
        selected_row = self.ui.tableWidget_2.currentRow()

        student_id = self.ui.tableWidget_2.item(selected_row, 0).text()
        self.ui.tableWidget_2.removeRow(selected_row)
        students = []

        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != student_id:
                    students.append(row)

        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)
            
def display():
    print("Hello")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
