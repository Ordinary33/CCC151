from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import QRegularExpression, QPropertyAnimation, Qt, QPoint, QEasingCurve
import math
import csv
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)  
        self.MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1050,640)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 150, MainWindow.height() - 50))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")


        #Sideframe
        self.sideframe = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.sideframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideframe.setStyleSheet("background-color: #A2D5AB;")
        self.sideframe.setObjectName("sideframe")
        self.sideframe.setFixedWidth(50)
        self.sideframe.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)

        #Sidebar
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        #Toggle Button
        self.Toggle = QtWidgets.QPushButton(self.sideframe)
        self.Toggle.setObjectName("Toggle")
        self.Toggle.setFixedSize(50, 50)
        self.Toggle.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        menu_icon = QtGui.QIcon(r"icon\menu.svg")
        self.Toggle.setIcon(menu_icon)
        self.Toggle.setIconSize(QtCore.QSize(32, 32))
        
        #View Button
        self.View = QtWidgets.QPushButton(self.sideframe)
        self.View.setObjectName("View")
        self.View.setFixedSize(50, 50)
        self.View.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        view_icon = QtGui.QIcon(r"icon\View.svg")
        self.View.setIcon(view_icon)
        self.View.setIconSize(QtCore.QSize(32, 32))
        

        #Add Button
        self.Add = QtWidgets.QPushButton(self.sideframe)
        self.Add.setObjectName("Add")
        self.Add.setFixedSize(50, 50)
        self.Add.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        add_icon = QtGui.QIcon(r"icon\Add.svg")
        self.Add.setIcon(add_icon)
        self.Add.setIconSize(QtCore.QSize(32, 32))
        
        #View Student Button
        self.ViewStudent = QtWidgets.QPushButton(self.sideframe)
        self.ViewStudent.setObjectName("ViewStudent")
        self.ViewStudent.setFixedSize(50, 50)
        self.ViewStudent.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        stud_icon = QtGui.QIcon(r"icon\Student.svg")
        self.ViewStudent.setIcon(stud_icon)
        self.ViewStudent.setIconSize(QtCore.QSize(25, 25))

        #View College Button
        self.ViewCollege = QtWidgets.QPushButton(self.sideframe)
        self.ViewCollege.setObjectName("ViewCollege")
        self.ViewCollege.setFixedSize(50, 50)
        self.ViewCollege.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        coll_icon = QtGui.QIcon(r"icon\College.svg")
        self.ViewCollege.setIcon(coll_icon)
        self.ViewCollege.setIconSize(QtCore.QSize(25, 25))

        #View Program Button
        self.ViewProgram = QtWidgets.QPushButton(self.sideframe)
        self.ViewProgram.setObjectName("ViewProgram")
        self.ViewProgram.setFixedSize(50, 50)
        self.ViewProgram.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        prog_icon = QtGui.QIcon(r"icon\Program.svg")
        self.ViewProgram.setIcon(prog_icon)
        self.ViewProgram.setIconSize(QtCore.QSize(25, 25))

        #Add Student Button
        self.AddStudent = QtWidgets.QPushButton(self.sideframe)
        self.AddStudent.setObjectName("AddStudent")
        self.AddStudent.setFixedSize(50, 50)
        self.AddStudent.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.AddStudent.setIcon(stud_icon)
        self.AddStudent.setIconSize(QtCore.QSize(25, 25))

        #Add College Button
        self.AddCollege = QtWidgets.QPushButton(self.sideframe)
        self.AddCollege.setObjectName("AddCollege")
        self.AddCollege.setFixedSize(50, 50)
        self.AddCollege.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.AddCollege.setIcon(coll_icon)
        self.AddCollege.setIconSize(QtCore.QSize(25, 25))
        
        #Add Program Button
        self.AddProgram = QtWidgets.QPushButton(self.sideframe)
        self.AddProgram.setObjectName("AddProgram")
        self.AddProgram.setFixedSize(50, 50)
        self.AddProgram.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.AddProgram.setIcon(prog_icon)
        self.AddProgram.setIconSize(QtCore.QSize(25, 25))

        self.verticalLayout.addWidget(self.Toggle, 0)
        self.verticalLayout.addWidget(self.View, 0)
        self.verticalLayout.addWidget(self.ViewStudent, 0)
        self.verticalLayout.addWidget(self.ViewProgram, 0)
        self.verticalLayout.addWidget(self.ViewCollege, 0)
        self.verticalLayout.addWidget(self.Add, 0)
        self.verticalLayout.addWidget(self.AddStudent, 0)
        self.verticalLayout.addWidget(self.AddProgram, 0)
        self.verticalLayout.addWidget(self.AddCollege, 0)
        self.verticalLayout.addWidget(self.sideframe)

        self.Toggle.enterEvent = self.extendSideMenu
        self.Toggle.leaveEvent = self.collapseSideMenu
        self.View.enterEvent = self.extendSideMenu
        self.View.leaveEvent = self.collapseSideMenu
        self.Add.enterEvent = self.extendSideMenu
        self.Add.leaveEvent = self.collapseSideMenu
        self.ViewStudent.enterEvent = self.extendSideMenu
        self.ViewStudent.leaveEvent = self.collapseSideMenu
        self.ViewProgram.enterEvent = self.extendSideMenu
        self.ViewProgram.leaveEvent = self.collapseSideMenu
        self.ViewCollege.enterEvent = self.extendSideMenu
        self.ViewCollege.leaveEvent = self.collapseSideMenu
        self.AddStudent.enterEvent = self.extendSideMenu
        self.AddStudent.leaveEvent = self.collapseSideMenu
        self.AddProgram.enterEvent = self.extendSideMenu
        self.AddProgram.leaveEvent = self.collapseSideMenu
        self.AddCollege.enterEvent = self.extendSideMenu
        self.AddCollege.leaveEvent = self.collapseSideMenu

        #add student feedback
        self.feedback = QtWidgets.QLabel(self.MainWindow)
        self.feedback.setAlignment(Qt.AlignCenter)
        self.feedback.setStyleSheet("max-width: 120px; max-height: 80px; color:white; background-color: #39AEA9; border-radius:12px; font-weight: bold")
        self.feedback.raise_()
        self.feedback.hide()


        #Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(0, 0, MainWindow.width(), 50)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: #39AEA9;")
        self.frame.setObjectName("frame")

        #Label
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 100, 900, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.VStud = QtWidgets.QWidget()
        
        

        #Student Table
        self.VStud.setObjectName("VStud")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.VStud)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 60, 881, 401))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        #Student Page Search bar
        self.Studsearch = QtWidgets.QLineEdit(self.VStud)
        self.Studsearch.setGeometry(QtCore.QRect(190, 0, 351, 21))
        self.Studsearch.setObjectName("Studsearch")

        #ViewStudent Sort by 
        self.label_4 = QtWidgets.QLabel(self.VStud)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.label_4.setObjectName("label_4")

        #ViewStudent Search by 
        self.label_5 = QtWidgets.QLabel(self.VStud)
        self.label_5.setGeometry(QtCore.QRect(10, -10, 81, 41))
        self.label_5.setObjectName("label_5")

        #ViewStudent search drop
        self.drop_search_2 = QtWidgets.QComboBox(self.VStud)
        self.drop_search_2.setGeometry(QtCore.QRect(80, 0, 91, 22))
        self.drop_search_2.setObjectName("drop_search_2")
        self.drop_search_2.addItems(["ID #", "First Name", "Last Name", "Year Level", "Gender", "Program Code"])

        #ViewStudent sort drop
        self.drop_sort_2 = QtWidgets.QComboBox(self.VStud)
        self.drop_sort_2.setGeometry(QtCore.QRect(80, 30, 91, 22))
        self.drop_sort_2.setObjectName("drop_sort_2")
        self.drop_sort_2.addItems(["ID #", "First Name", "Last Name", "Year Level", "Gender", "Program Code"])


        #ViewStudent search button
        self.SearchBtn_2 = QtWidgets.QPushButton(self.VStud)
        self.SearchBtn_2.setGeometry(QtCore.QRect(560, 0, 85, 25))
        self.SearchBtn_2.setObjectName("SearchBtn_2")

        #ViewStudent delete button
        self.Removebtn_2 = QtWidgets.QPushButton(self.VStud)
        self.Removebtn_2.setGeometry(QtCore.QRect(123, 470, 93, 28))
        self.Removebtn_2.setObjectName("Removebtn_2")

        #ViewStudent edit button
        self.Editbtn = QtWidgets.QPushButton(self.VStud)
        self.Editbtn.setGeometry(QtCore.QRect(10, 470, 93, 28))
        self.Editbtn.setObjectName("Editbtn")
        self.Editbtn.clicked.connect(self.open_edit_dialog)
        self.stackedWidget.addWidget(self.VStud)

        #ViewCollege
        self.VColl = QtWidgets.QWidget()
        self.VColl.setObjectName("VColl")

        #ViewCollege Search by
        self.label_2 = QtWidgets.QLabel(self.VColl)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 81, 41))
        self.label_2.setObjectName("label_2")

        #Viewcollege Sort drop
        self.drop_sort = QtWidgets.QComboBox(self.VColl)
        self.drop_sort.setGeometry(QtCore.QRect(80, 30, 91, 22))
        self.drop_sort.setObjectName("drop_search")
        self.drop_sort.addItems(["Code", "Name"])

        #Viewcollege sort by
        self.label_3 = QtWidgets.QLabel(self.VColl)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.label_3.setObjectName("label_3")

        #Viewcollege search  drop
        self.drop_search = QtWidgets.QComboBox(self.VColl)
        self.drop_search.setGeometry(QtCore.QRect(80, 0, 91, 22))
        self.drop_search.setObjectName("drop_sort")
        self.drop_search.addItems(["Code", "Name"])

        #Viewcollege search bar
        self.lineEdit = QtWidgets.QLineEdit(self.VColl)
        self.lineEdit.setGeometry(QtCore.QRect(190, 0, 351, 21))
        self.lineEdit.setObjectName("lineEdit")

        #Viewcollege search button
        self.SearchBtn = QtWidgets.QPushButton(self.VColl)
        self.SearchBtn.setGeometry(QtCore.QRect(560, 0, 85, 25))
        self.SearchBtn.setObjectName("SearchBtn")
        
        #Colleges Table
        self.tableWidget = QtWidgets.QTableWidget(self.VColl)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 881, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        #Viewcollege delete button
        self.Removebtn = QtWidgets.QPushButton(self.VColl)
        self.Removebtn.setGeometry(QtCore.QRect(123, 470, 93, 28))
        self.Removebtn.setObjectName("Removebtn")

        #ViewCollege edit button
        self.Editbtn2 = QtWidgets.QPushButton(self.VColl)
        self.Editbtn2.setGeometry(QtCore.QRect(10, 470, 93, 28))
        self.Editbtn2.setObjectName("Editbtn2")
        self.Editbtn2.clicked.connect(self.open_edit_college_dialog)

        self.stackedWidget.addWidget(self.VColl) 
        self.VProg = QtWidgets.QWidget()
        self.VProg.setObjectName("VProg")

        #Programs Table
        self.tableWidget_3 = QtWidgets.QTableWidget(self.VProg)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 60, 881, 401))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        

        #ViewPrograms search bar
        self.lineEdit_3 = QtWidgets.QLineEdit(self.VProg)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 0, 351, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        #ViewPrograms sort by
        self.label_6 = QtWidgets.QLabel(self.VProg)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.label_6.setObjectName("label_6")

        #ViewPrograms search by
        self.label_7 = QtWidgets.QLabel(self.VProg)
        self.label_7.setGeometry(QtCore.QRect(10, -10, 81, 41))
        self.label_7.setObjectName("label_7")

        #Viewprograms search drop
        self.drop_search_3 = QtWidgets.QComboBox(self.VProg)
        self.drop_search_3.setGeometry(QtCore.QRect(80, 0, 91, 22))
        self.drop_search_3.setObjectName("drop_sort_3")
        self.drop_search_3.addItems(["Code", "Name", "College Code"])

        #Viewprograms sort drop
        self.drop_sort_3 = QtWidgets.QComboBox(self.VProg)
        self.drop_sort_3.setGeometry(QtCore.QRect(80, 30, 91, 22))
        self.drop_sort_3.setObjectName("drop_search_3")
        self.drop_sort_3.addItems(["Code", "Name", "College Code"])

        #Viewprograms search button
        self.SearchBtn_3 = QtWidgets.QPushButton(self.VProg)
        self.SearchBtn_3.setGeometry(QtCore.QRect(560, 0, 85, 25))
        self.SearchBtn_3.setObjectName("SearchBtn_3")

        #Viewprograms delete button
        self.Removebtn_3 = QtWidgets.QPushButton(self.VProg)
        self.Removebtn_3.setGeometry(QtCore.QRect(123, 470, 93, 28))
        self.Removebtn_3.setObjectName("Removebtn_3")

        #Viewprograms edit button
        self.Editbtn3 = QtWidgets.QPushButton(self.VProg)
        self.Editbtn3.setGeometry(QtCore.QRect(10, 470, 93, 28))
        self.Editbtn3.setObjectName("Editbtn3")
        self.Editbtn3.clicked.connect(self.open_edit_program_dialog)

        self.stackedWidget.addWidget(self.VProg)
        self.Astud = QtWidgets.QWidget()
        self.Astud.setObjectName("Astud")

        # id no. 
        self.label_8 = QtWidgets.QLabel(self.Astud)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        #id search bar
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Astud)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 30, 131, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        #regex validator YYYY-NNNN format
        regex = QRegularExpression(r"^\d{4}-\d{4}$")
        validator = QRegularExpressionValidator(regex, self.lineEdit_4)
        self.lineEdit_4.setValidator(validator)

        #first name 
        self.label_9 = QtWidgets.QLabel(self.Astud)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        #last name
        self.label_10 = QtWidgets.QLabel(self.Astud)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        #year level
        self.label_11 = QtWidgets.QLabel(self.Astud)
        self.label_11.setGeometry(QtCore.QRect(20, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        #gender
        self.label_12 = QtWidgets.QLabel(self.Astud)
        self.label_12.setGeometry(QtCore.QRect(20, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        #program code
        self.label_13 = QtWidgets.QLabel(self.Astud)
        self.label_13.setGeometry(QtCore.QRect(20, 220, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")


        #first name search
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Astud)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 70, 131, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")

        #last name search
        self.lineEdit_6 = QtWidgets.QLineEdit(self.Astud)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 110, 131, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")

        #first name and last name regex validator (letters and spaces)
        name_validator = QRegularExpressionValidator(QRegularExpression("^[A-Za-z ]+$"))
        self.lineEdit_5.setValidator(name_validator)
        self.lineEdit_6.setValidator(name_validator)


        #year level drop
        self.comboBox = QtWidgets.QComboBox(self.Astud)
        self.comboBox.setGeometry(QtCore.QRect(180, 150, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["1", "2", "3", "4"])

        #gender drop
        self.comboBox_2 = QtWidgets.QComboBox(self.Astud)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 190, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Male", "Female", "Other"])

        #program code drop
        self.comboBox_3 = QtWidgets.QComboBox(self.Astud)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 230, 91, 22))
        self.comboBox_3.setObjectName("comboBox_3")


        #Add student button
        self.pushButton = QtWidgets.QPushButton(self.Astud)
        self.pushButton.setGeometry(QtCore.QRect(15, 270, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.stackedWidget.addWidget(self.Astud)
        self.AColl = QtWidgets.QWidget()
        self.AColl.setObjectName("AColl")

        #code coll
        self.label_14 = QtWidgets.QLabel(self.AColl)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        #name coll
        self.label_15 = QtWidgets.QLabel(self.AColl)
        self.label_15.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        #code search bar coll
        self.lineEdit_7 = QtWidgets.QLineEdit(self.AColl)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 30, 131, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")

        

        #name search bar coll
        self.lineEdit_8 = QtWidgets.QLineEdit(self.AColl)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 70, 131, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.lineEdit_7.setValidator(name_validator)
        self.lineEdit_8.setValidator(name_validator)

        #add college button
        self.pushButton_2 = QtWidgets.QPushButton(self.AColl)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 120, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.stackedWidget.addWidget(self.AColl)
        self.Aprog = QtWidgets.QWidget()
        self.Aprog.setObjectName("Aprog")

        #code prog
        self.label_16 = QtWidgets.QLabel(self.Aprog)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        #name prog
        self.label_17 = QtWidgets.QLabel(self.Aprog)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        #college code prog
        self.label_18 = QtWidgets.QLabel(self.Aprog)
        self.label_18.setGeometry(QtCore.QRect(20, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")

        #code search bar prog
        self.lineEdit_9 = QtWidgets.QLineEdit(self.Aprog)
        self.lineEdit_9.setGeometry(QtCore.QRect(180, 30, 131, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")

        #name search bar prog
        self.lineEdit_10 = QtWidgets.QLineEdit(self.Aprog)
        self.lineEdit_10.setGeometry(QtCore.QRect(180, 70, 131, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.lineEdit_9.setValidator(name_validator)
        self.lineEdit_10.setValidator(name_validator)
        
        #college code drop prog
        self.comboBox_4 = QtWidgets.QComboBox(self.Aprog)
        self.comboBox_4.setGeometry(QtCore.QRect(180, 110, 131, 21))
        self.comboBox_4.setObjectName("comboBox_4")

        #add program button
        self.pushButton_3 = QtWidgets.QPushButton(self.Aprog)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 150, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.stackedWidget.addWidget(self.Aprog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Information System"))
        self.Toggle.setText(_translate("MainWindow", "Menu"))
        self.View.setText(_translate("MainWindow", "View"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.ViewStudent.setText(_translate("MainWindow", "View Students"))
        self.ViewCollege.setText(_translate("MainWindow", "View Colleges"))
        self.ViewProgram.setText(_translate("MainWindow", "View Programs"))
        self.AddStudent.setText(_translate("MainWindow", "Add Student"))
        self.AddCollege.setText(_translate("MainWindow", "Add College"))
        self.AddProgram.setText(_translate("MainWindow", "Add Program"))
        self.label.setText(_translate("MainWindow", "SSIS"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID #"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Main Window", "Last Name"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Year Level"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Program Code"))
        self.label_4.setText(_translate("MainWindow", "Sort by:"))
        self.label_5.setText(_translate("MainWindow", "Search by:"))
        self.SearchBtn_2.setText(_translate("MainWindow", "Search"))
        self.Removebtn_2.setText(_translate("MainWindow", "Delete"))
        self.Editbtn.setText(_translate("MainWindow", "Edit"))
        self.label_2.setText(_translate("MainWindow", "Search by:"))
        self.label_3.setText(_translate("MainWindow", "Sort by:"))
        self.SearchBtn.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.Removebtn.setText(_translate("MainWindow", "Delete"))
        self.Editbtn2.setText(_translate("MainWindow", "Edit"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "College Code"))
        self.label_6.setText(_translate("MainWindow", "Sort by:"))
        self.label_7.setText(_translate("MainWindow", "Search by:"))
        self.SearchBtn_3.setText(_translate("MainWindow", "Search"))
        self.Removebtn_3.setText(_translate("MainWindow", "Delete"))
        self.Editbtn3.setText(_translate("MainWindow", "Edit"))
        self.label_8.setText(_translate("MainWindow", "ID # (YYYY-NNNN):"))
        self.label_9.setText(_translate("MainWindow", "First Name:"))
        self.label_10.setText(_translate("MainWindow", "Last Name:"))
        self.label_11.setText(_translate("MainWindow", "Year Level:"))
        self.label_12.setText(_translate("MainWindow", "Gender:"))
        self.label_13.setText(_translate("MainWindow", "Program Code:"))
        self.pushButton.setText(_translate("MainWindow", "Add Student"))
        self.label_14.setText(_translate("MainWindow", "Code:"))
        self.label_15.setText(_translate("MainWindow", "Name:"))
        self.pushButton_2.setText(_translate("MainWindow", "Add College"))
        self.label_16.setText(_translate("MainWindow", "Code:"))
        self.label_17.setText(_translate("MainWindow", "Name:"))
        self.label_18.setText(_translate("MainWindow", "College Code:"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Program"))
        

    def open_edit_dialog(self):

        selected_row = self.tableWidget_2.currentRow()
        if selected_row == -1:
            return
        
        student_id_item = self.tableWidget_2.item(selected_row, 0)
        if not student_id_item:
            return
        
        student_id = student_id_item.text()

        dialog = QtWidgets.QDialog(self.MainWindow)  
        dialog.setWindowTitle("Edit Student")
        dialog.setFixedSize(300, 300)
        dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Close Button
        close_btn = QtWidgets.QPushButton(dialog)
        close_btn.setGeometry(270, 5, 24, 24)
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
        
        #edit id no
        self.edit_id = QtWidgets.QLabel(dialog)
        self.edit_id.setGeometry(QtCore.QRect(10, 20, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_id.setFont(font)
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setText("ID #:")
        self.edit_id.setStyleSheet("color: white; font-weight:bold;")

        #edit id search
        self.edit_search = QtWidgets.QLineEdit(dialog)
        self.edit_search.setGeometry(QtCore.QRect(130, 20, 100, 20))
        self.edit_search.setObjectName("edit_search")
        self.edit_search.setText(student_id)
        self.edit_search.setReadOnly(True)

        #edit first name
        self.edit_fn = QtWidgets.QLabel(dialog)
        self.edit_fn.setGeometry(QtCore.QRect(10, 50, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_fn.setFont(font)
        self.edit_fn.setObjectName("edit_fn")
        self.edit_fn.setText("First Name:")
        self.edit_fn.setStyleSheet("color: white; font-weight:bold;")

        #edit last name
        self.edit_ln = QtWidgets.QLabel(dialog)
        self.edit_ln.setGeometry(QtCore.QRect(10, 80, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_ln.setFont(font)
        self.edit_ln.setObjectName("edit_ln")
        self.edit_ln.setText("Last Name:")
        self.edit_ln.setStyleSheet("color: white; font-weight:bold;")

        #edit year lvl
        self.edit_yr = QtWidgets.QLabel(dialog)
        self.edit_yr.setGeometry(QtCore.QRect(10, 110, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_yr.setFont(font)
        self.edit_yr.setObjectName("edit_yr")
        self.edit_yr.setText("Year Level:")
        self.edit_yr.setStyleSheet("color: white; font-weight:bold;")

        #edit gender
        self.edit_gen = QtWidgets.QLabel(dialog)
        self.edit_gen.setGeometry(QtCore.QRect(10, 140, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_gen.setFont(font)
        self.edit_gen.setObjectName("edit_gen")
        self.edit_gen.setText("Gender:")
        self.edit_gen.setStyleSheet("color: white; font-weight:bold;")

        #edit program code
        self.edit_prog = QtWidgets.QLabel(dialog)
        self.edit_prog.setGeometry(QtCore.QRect(10, 170, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_prog.setFont(font)
        self.edit_prog.setObjectName("edit_prog")
        self.edit_prog.setText("Program Code:")
        self.edit_prog.setStyleSheet("color: white; font-weight:bold;")

        #edit first name search
        self.edit_fnse = QtWidgets.QLineEdit(dialog)
        self.edit_fnse.setGeometry(QtCore.QRect(130, 50, 131, 21))
        self.edit_fnse.setObjectName("edit_fnse")
        self.edit_fnse.setText(self.tableWidget_2.item(selected_row, 1).text())

        #edit last name search
        self.edit_lnse = QtWidgets.QLineEdit(dialog)
        self.edit_lnse.setGeometry(QtCore.QRect(130, 80, 131, 21))
        self.edit_lnse.setObjectName("edit_lnse")
        self.edit_lnse.setText(self.tableWidget_2.item(selected_row, 2).text())

        #edit first name and last name regex validator
        name_validator = QRegularExpressionValidator(QRegularExpression("^[A-Za-z ]+$"))
        self.edit_fnse.setValidator(name_validator)
        self.edit_lnse.setValidator(name_validator)

        #edit year level drop
        self.edit_yrcom = QtWidgets.QComboBox(dialog)
        self.edit_yrcom.setGeometry(QtCore.QRect(130, 110, 73, 22))
        self.edit_yrcom.setObjectName("edit_yrcom")
        self.edit_yrcom.addItems(["1", "2", "3", "4"])
        self.edit_yrcom.setCurrentText(self.tableWidget_2.item(selected_row, 3).text())

        #edit gender drop
        self.edit_gencom = QtWidgets.QComboBox(dialog)
        self.edit_gencom.setGeometry(QtCore.QRect(130, 140, 91, 22))
        self.edit_gencom.setObjectName("edit_gencom")
        self.edit_gencom.addItems(["Male", "Female", "Other"])
        self.edit_gencom.setCurrentText(self.tableWidget_2.item(selected_row, 4).text())

        #edit program code drop
        self.edit_pccom = QtWidgets.QComboBox(dialog)
        self.edit_pccom.setGeometry(QtCore.QRect(130, 170, 91, 22))
        self.edit_pccom.setObjectName("edit_pccom")
        self.edit_pccom.clear()
        self.edit_pccom.addItem("None")
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  
            program_codes = [row[0] for row in reader if row]  
        self.edit_pccom.addItems(program_codes)
        self.edit_pccom.setCurrentText(self.tableWidget_2.item(selected_row, 5).text())
        

        #edit save button
        self.Savebtn1 = QtWidgets.QPushButton(dialog)
        self.Savebtn1.setGeometry(QtCore.QRect(10, 200, 93, 28))
        self.Savebtn1.setObjectName("Savebtn1")
        self.Savebtn1.setText("Save")
        self.Savebtn1.clicked.connect(lambda: self.save_edited_student(dialog, student_id))
        
        dialog.exec_()


    def save_edited_student(self, dialog, student_id):
        new_first_name = self.edit_fnse.text()
        new_last_name = self.edit_lnse.text()
        new_year_level = self.edit_yrcom.currentText()
        new_gender = self.edit_gencom.currentText()
        new_program_code = self.edit_pccom.currentText()

        if not new_first_name or not new_last_name:
            QMessageBox.warning(dialog, "Input Error", "All Fields must be filled!")
            return
        
        updated_rows = []
        with open("csv/students.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row and row[0] == student_id:
                row[1] = new_first_name
                row[2] = new_last_name
                row[3] = new_year_level
                row[4] = new_gender
                row[5] = new_program_code
            updated_rows.append(row)

        with open("csv/students.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        self.tableWidget_2.setRowCount(0)  
        self.refresh_student_table() 
        self.feedback_anim("Student Edited") 

        dialog.accept()

    def refresh_student_table(self):
        self.tableWidget_2.setRowCount(0)
        with open("csv/students.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row_data in reader:
                row = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row)
                for col, item in enumerate(row_data):
                    self.tableWidget_2.setItem(row, col, QtWidgets.QTableWidgetItem(item)) 
    def open_edit_program_dialog(self):
        selected_row = self.tableWidget_3.currentRow()
        if selected_row == -1:
            return

        program_code_item = self.tableWidget_3.item(selected_row, 0)
        if not program_code_item:
            return
    
        program_code = program_code_item.text()
        program_name = self.tableWidget_3.item(selected_row, 1).text()
        college_code = self.tableWidget_3.item(selected_row, 2).text()

        dialog = QtWidgets.QDialog(self.MainWindow)
        dialog.setWindowTitle("Edit Program")
        dialog.setFixedSize(300, 200)
        dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Close Button
        close_btn = QtWidgets.QPushButton(dialog)
        close_btn.setGeometry(270, 5, 24, 24)
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

        self.edit_c = QtWidgets.QLabel(dialog)
        self.edit_c.setGeometry(QtCore.QRect(10, 20, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_c.setFont(font)
        self.edit_c.setObjectName("edit_c")
        self.edit_c.setText("Code:")

        #edit name
        self.edit_n = QtWidgets.QLabel(dialog)
        self.edit_n.setGeometry(QtCore.QRect(10, 50, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_n.setFont(font)
        self.edit_n.setObjectName("edit_n")
        self.edit_n.setText("Name:")

        #edit cc
        self.edit_cc = QtWidgets.QLabel(dialog)
        self.edit_cc.setGeometry(QtCore.QRect(10, 80, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_cc.setFont(font)
        self.edit_cc.setObjectName("edit_cc")
        self.edit_cc.setText("College Code:")

        name_validator = QRegularExpressionValidator(QRegularExpression("^[A-Za-z ]+$"))
    
        #edit code search
        self.edit_code = QtWidgets.QLineEdit(dialog)
        self.edit_code.setGeometry(QtCore.QRect(130, 20, 100, 20))
        self.edit_code.setText(program_code)
        self.edit_code.setValidator(name_validator)

        #edit name search
        self.edit_name = QtWidgets.QLineEdit(dialog)
        self.edit_name.setGeometry(QtCore.QRect(130, 50, 131, 21))
        self.edit_name.setText(program_name)
        self.edit_name.setValidator(name_validator)
    
        #edit cc drop
        self.edit_college_code = QtWidgets.QComboBox(dialog)
        self.edit_college_code.setGeometry(QtCore.QRect(130, 80, 150, 22))
        self.edit_college_code.clear()
        self.edit_college_code.addItem("None")
    
        with open("csv/colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            college_codes = [row[0] for row in reader if row]
    
        self.edit_college_code.addItems(college_codes)
        self.edit_college_code.setCurrentText(college_code)
    
        # Save Button
        self.save_button = QtWidgets.QPushButton("Save", dialog)
        self.save_button.setGeometry(QtCore.QRect(10, 140, 93, 28))
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(lambda: self.save_edited_program(dialog, program_code))
    
        dialog.exec_()

    def save_edited_program(self, dialog, program_code):
        new_program_code = self.edit_code.text()
        new_name = self.edit_name.text()
        new_college_code = self.edit_college_code.currentText()
    
        if not new_name or not new_college_code:
            QMessageBox.warning(dialog, "Input Error", "All Fields must be filled!")
            return
    
        updated_rows = []
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)
    
        for row in rows:
            if row and row[0] == program_code:
                row[0] = new_program_code
                row[1] = new_name
                row[2] = new_college_code
            updated_rows.append(row)
    
        with open("csv/programs.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        updated_students = []
        with open("csv/students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row and row[5] == program_code:  
                row[5] = new_program_code  
            updated_students.append(row)

        with open("csv/students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_students)
    
        self.refresh_program_table()
        self.refresh_student_table()
        self.feedback_anim("Program Edited")
        dialog.accept()

    def refresh_program_table(self):
        self.tableWidget_3.setRowCount(0)
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row_data in reader:
                row = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row)
                for col, item in enumerate(row_data):
                    self.tableWidget_3.setItem(row, col, QtWidgets.QTableWidgetItem(item))


    def open_edit_college_dialog(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            return

        college_code_item = self.tableWidget.item(selected_row, 0)
        if not college_code_item:
            return

        college_code = college_code_item.text()
        college_name = self.tableWidget.item(selected_row, 1).text()

        dialog = QtWidgets.QDialog(self.MainWindow)
        dialog.setWindowTitle("Edit College")
        dialog.setFixedSize(300, 300)
        dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Close Button
        close_btn = QtWidgets.QPushButton(dialog)
        close_btn.setGeometry(270, 5, 24, 24)
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

        #edit code
        self.label_code = QtWidgets.QLabel("Code:", dialog)
        self.label_code.setGeometry(QtCore.QRect(10, 30, 50, 20))
        self.label_code.setFont(QtGui.QFont("Arial", 10))

        #edit name
        self.label_name = QtWidgets.QLabel("Name:", dialog)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.label_name.setFont(QtGui.QFont("Arial", 10))

        name_validator = QRegularExpressionValidator(QRegularExpression("^[A-Za-z ]+$"))

        #edit code search
        self.edit_code = QtWidgets.QLineEdit(dialog)
        self.edit_code.setGeometry(QtCore.QRect(130, 30, 100, 20))
        self.edit_code.setText(college_code)
        self.edit_code.setValidator(name_validator)

        #edit name search
        self.edit_name = QtWidgets.QLineEdit(dialog)
        self.edit_name.setGeometry(QtCore.QRect(130, 60, 150, 20))
        self.edit_name.setText(college_name)
        self.edit_name.setValidator(name_validator)


        self.save_button2 = QtWidgets.QPushButton("Save", dialog)
        self.save_button2.setGeometry(QtCore.QRect(10, 110, 93, 28))
        self.save_button2.setObjectName("save_button2")
        self.save_button2.clicked.connect(lambda: self.save_edited_college(dialog, college_code))

        dialog.exec_()

    def save_edited_college(self, dialog, college_code):
        new_college_code = self.edit_code.text()
        new_college_name = self.edit_name.text()

        if not new_college_code or not new_college_name:
            QtWidgets.QMessageBox.warning(dialog, "Input Error", "All Fields must be filled!")
            return

        updated_rows = []
        with open("csv/colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row and row[0] == college_code:
                row[0] = new_college_code
                row[1] = new_college_name
            updated_rows.append(row)

        with open("csv/colleges.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        updated_programs = []
        with open("csv/programs.csv", "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row and row[2] == college_code:  
                row[2] = new_college_code  
            updated_programs.append(row)

        with open("csv/programs.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_programs)

        self.refresh_college_table()
        self.refresh_program_table()
        self.feedback_anim("College Edited")
        dialog.accept()

    def refresh_college_table(self):
        self.tableWidget.setRowCount(0)
        with open("csv/colleges.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row_data in reader:
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                for col, item in enumerate(row_data):
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(item))


    def extendSideMenu(self, event):
        self.verticalLayoutWidget.setMaximumWidth(150)
        self.sideframe.setMaximumWidth(150)

        self.animation = QPropertyAnimation(self.sideframe, b"maximumWidth")
        self.animation2 = QPropertyAnimation(self.Toggle, b"maximumWidth")
        self.animation3 = QPropertyAnimation(self.View, b"maximumWidth")
        self.animation4 = QPropertyAnimation(self.Add, b"maximumWidth")
        self.animation5 = QPropertyAnimation(self.ViewStudent, b"maximumWidth")
        self.animation6 = QPropertyAnimation(self.ViewProgram, b"maximumWidth")
        self.animation7 = QPropertyAnimation(self.ViewCollege, b"maximumWidth")
        self.animation8 = QPropertyAnimation(self.AddStudent, b"maximumWidth")
        self.animation9 = QPropertyAnimation(self.AddProgram, b"maximumWidth")
        self.animation10 = QPropertyAnimation(self.AddCollege, b"maximumWidth")

        self.animation.setDuration(200)
        self.animation2.setDuration(200)
        self.animation3.setDuration(200)
        self.animation4.setDuration(200)
        self.animation5.setDuration(200)
        self.animation6.setDuration(200)
        self.animation7.setDuration(200)
        self.animation8.setDuration(200)
        self.animation9.setDuration(200)
        self.animation10.setDuration(200)

        self.animation.setStartValue(50)
        self.animation2.setStartValue(50)
        self.animation3.setStartValue(50)
        self.animation4.setStartValue(50)
        self.animation5.setStartValue(50)
        self.animation6.setStartValue(50)
        self.animation7.setStartValue(50)
        self.animation8.setStartValue(50)
        self.animation9.setStartValue(50)
        self.animation10.setStartValue(50)
        
        self.animation.setEndValue(120)
        self.animation2.setEndValue(120)
        self.animation3.setEndValue(120)
        self.animation4.setEndValue(120)
        self.animation5.setEndValue(120)
        self.animation6.setEndValue(120)
        self.animation7.setEndValue(120)
        self.animation8.setEndValue(120)
        self.animation9.setEndValue(120)
        self.animation10.setEndValue(120)

        self.Toggle.setStyleSheet("color: #557B83;")
        self.View.setStyleSheet("color: #557B83;")
        self.Add.setStyleSheet("color: #557B83;")
        self.ViewStudent.setStyleSheet("color: #557B83;")          
        self.ViewProgram.setStyleSheet("color: #557B83;")          
        self.ViewCollege.setStyleSheet("color: #557B83;")
        self.AddStudent.setStyleSheet("color: #557B83;")          
        self.AddProgram.setStyleSheet("color: #557B83;")          
        self.AddCollege.setStyleSheet("color: #557B83;")           
            
        self.animation.start()
        self.animation2.start()
        self.animation3.start()
        self.animation4.start()
        self.animation5.start()
        self.animation6.start()
        self.animation7.start()
        self.animation8.start()
        self.animation9.start()
        self.animation10.start()


    def collapseSideMenu(self, event):

        self.animation = QPropertyAnimation(self.sideframe, b"maximumWidth")
        self.animation2 = QPropertyAnimation(self.Toggle, b"maximumWidth")
        self.animation3 = QPropertyAnimation(self.View, b"maximumWidth")
        self.animation4 = QPropertyAnimation(self.Add, b"maximumWidth")
        self.animation5 = QPropertyAnimation(self.ViewStudent, b"maximumWidth")
        self.animation6 = QPropertyAnimation(self.ViewProgram, b"maximumWidth")
        self.animation7 = QPropertyAnimation(self.ViewCollege, b"maximumWidth")
        self.animation8 = QPropertyAnimation(self.AddStudent, b"maximumWidth")
        self.animation9 = QPropertyAnimation(self.AddProgram, b"maximumWidth")
        self.animation10 = QPropertyAnimation(self.AddCollege, b"maximumWidth")


        self.animation.setDuration(200)
        self.animation2.setDuration(200)
        self.animation3.setDuration(200)
        self.animation4.setDuration(200)
        self.animation5.setDuration(200)
        self.animation6.setDuration(200)
        self.animation7.setDuration(200)
        self.animation8.setDuration(200)
        self.animation9.setDuration(200)
        self.animation10.setDuration(200)

        self.animation.setStartValue(120)
        self.animation2.setStartValue(120)
        self.animation3.setStartValue(120)
        self.animation4.setStartValue(120)
        self.animation5.setStartValue(120)
        self.animation6.setStartValue(120)
        self.animation7.setStartValue(120)
        self.animation8.setStartValue(120)
        self.animation9.setStartValue(120)
        self.animation10.setStartValue(120)

        self.animation.setEndValue(50)
        self.animation2.setEndValue(50)
        self.animation3.setEndValue(50)
        self.animation4.setEndValue(50)
        self.animation5.setEndValue(50)
        self.animation6.setEndValue(50)
        self.animation7.setEndValue(50)
        self.animation8.setEndValue(50)
        self.animation9.setEndValue(50)
        self.animation10.setEndValue(50)

        self.Toggle.setStyleSheet("color: #A2D5AB;")
        self.View.setStyleSheet("color: #A2D5AB;")
        self.Add.setStyleSheet("color: #A2D5AB;")
        self.ViewStudent.setStyleSheet("color: #A2D5AB;")
        self.ViewProgram.setStyleSheet("color: #A2D5AB;")
        self.ViewCollege.setStyleSheet("color: #A2D5AB;")
        self.AddStudent.setStyleSheet("color: #A2D5AB;")
        self.AddProgram.setStyleSheet("color: #A2D5AB;")
        self.AddCollege.setStyleSheet("color: #A2D5AB;")

        self.animation.start()
        self.animation2.start()
        self.animation3.start()
        self.animation4.start()
        self.animation5.start()
        self.animation6.start()
        self.animation7.start()
        self.animation8.start()
        self.animation9.start()
        self.animation10.start()

    
    def feedback_anim(self, message):

        self.feedback.setText(message)
        self.feedback.show()
        self.anim = QPropertyAnimation(self.feedback, b"pos")
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        X = math.floor(self.MainWindow.width() / 2) - 50
        startY = 0 - self.MainWindow.height()
        endY = 60
        self.feedback.move(X, startY)

        self.anim.setStartValue(QPoint(X, startY))
        self.anim.setEndValue(QPoint(X, endY))
        self.anim.setDuration(400)

        threading.Timer(2, lambda: self.feedback.hide()).start()
        self.anim.start()    

    
    