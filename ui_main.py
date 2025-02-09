from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(1200,900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)

        

        #Sidebar
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 111, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #View Student Button
        self.ViewStudent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ViewStudent.setObjectName("ViewStudent")
        # self.ViewStudent.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ViewStudent.setMaximumSize(111,40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ViewStudent.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.ViewStudent, 0)

        #View College Button
        self.ViewCollege = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ViewCollege.setObjectName("ViewCollege")
        self.ViewCollege.setMaximumSize(111,30)
        self.ViewCollege.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.ViewCollege, 0)

        #View Program Button
        self.ViewProgram = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ViewProgram.setObjectName("ViewProgram")
        self.ViewProgram.setMaximumSize(111,30)
        self.ViewProgram.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.ViewProgram, 0)

         #Add Student Button
        self.AddStudent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AddStudent.setObjectName("AddStudent")
        self.AddStudent.setMaximumSize(111,30)
        self.AddStudent.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.AddStudent, 0)

        #Add College Button
        self.AddCollege = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AddCollege.setObjectName("AddCollege")
        self.AddCollege.setMaximumSize(111,30)
        self.AddCollege.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.AddCollege, 0)
        
        #Add Program Button
        self.AddProgram = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AddProgram.setObjectName("AddProgram")
        self.AddProgram.setMaximumSize(111,30)
        self.AddProgram.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.AddProgram, 0)

        #Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 0, 768, 119))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #Label
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 100, 921, 531))
        self.stackedWidget.setObjectName("stackedWidget")
        self.VStud = QtWidgets.QWidget()

        #Student Table
        self.VStud.setObjectName("VStud")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.VStud)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 60, 881, 401))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
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
        self.Studsearch = QtWidgets.QLineEdit(self.VStud)
        self.Studsearch.setGeometry(QtCore.QRect(190, 0, 351, 21))
        self.Studsearch.setObjectName("Studsearch")

        self.label_4 = QtWidgets.QLabel(self.VStud)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.VStud)
        self.label_5.setGeometry(QtCore.QRect(10, -10, 81, 41))
        self.label_5.setObjectName("label_5")

        self.drop_sort_2 = QtWidgets.QComboBox(self.VStud)
        self.drop_sort_2.setGeometry(QtCore.QRect(80, 0, 91, 22))
        self.drop_sort_2.setObjectName("drop_sort_2")

        self.drop_search_2 = QtWidgets.QComboBox(self.VStud)
        self.drop_search_2.setGeometry(QtCore.QRect(80, 30, 91, 22))
        self.drop_search_2.setObjectName("drop_search_2")

        self.SearchBtn_2 = QtWidgets.QPushButton(self.VStud)
        self.SearchBtn_2.setGeometry(QtCore.QRect(590, 0, 93, 28))
        self.SearchBtn_2.setObjectName("SearchBtn_2")

        self.Removebtn_2 = QtWidgets.QPushButton(self.VStud)
        self.Removebtn_2.setGeometry(QtCore.QRect(10, 470, 93, 28))
        self.Removebtn_2.setObjectName("Removebtn_2")

        self.stackedWidget.addWidget(self.VStud)
        self.VColl = QtWidgets.QWidget()
        self.VColl.setObjectName("VColl")
        self.label_2 = QtWidgets.QLabel(self.VColl)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 41))
        self.label_2.setObjectName("label_2")

        self.drop_search = QtWidgets.QComboBox(self.VColl)
        self.drop_search.setGeometry(QtCore.QRect(120, 20, 91, 22))
        self.drop_search.setObjectName("drop_search")

        self.label_3 = QtWidgets.QLabel(self.VColl)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 81, 41))
        self.label_3.setObjectName("label_3")

        self.drop_sort = QtWidgets.QComboBox(self.VColl)
        self.drop_sort.setGeometry(QtCore.QRect(120, 50, 91, 22))
        self.drop_sort.setObjectName("drop_sort")

        self.lineEdit = QtWidgets.QLineEdit(self.VColl)
        self.lineEdit.setGeometry(QtCore.QRect(240, 20, 351, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.SearchBtn = QtWidgets.QPushButton(self.VColl)
        self.SearchBtn.setGeometry(QtCore.QRect(610, 20, 93, 28))
        self.SearchBtn.setObjectName("SearchBtn")
         
        self.tableWidget = QtWidgets.QTableWidget(self.VColl)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 881, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.Removebtn = QtWidgets.QPushButton(self.VColl)
        self.Removebtn.setGeometry(QtCore.QRect(20, 490, 93, 28))
        self.Removebtn.setObjectName("Removebtn")

        self.stackedWidget.addWidget(self.VColl)
        self.VProg = QtWidgets.QWidget()
        self.VProg.setObjectName("VProg")

        self.tableWidget_3 = QtWidgets.QTableWidget(self.VProg)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 60, 881, 401))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.VProg)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 0, 351, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_6 = QtWidgets.QLabel(self.VProg)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 81, 41))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.VProg)
        self.label_7.setGeometry(QtCore.QRect(30, -10, 81, 41))
        self.label_7.setObjectName("label_7")

        self.drop_sort_3 = QtWidgets.QComboBox(self.VProg)
        self.drop_sort_3.setGeometry(QtCore.QRect(100, 0, 91, 22))
        self.drop_sort_3.setObjectName("drop_sort_3")

        self.drop_search_3 = QtWidgets.QComboBox(self.VProg)
        self.drop_search_3.setGeometry(QtCore.QRect(100, 30, 91, 22))
        self.drop_search_3.setObjectName("drop_search_3")

        self.SearchBtn_3 = QtWidgets.QPushButton(self.VProg)
        self.SearchBtn_3.setGeometry(QtCore.QRect(600, 0, 93, 28))
        self.SearchBtn_3.setObjectName("SearchBtn_3")
        self.Removebtn_3 = QtWidgets.QPushButton(self.VProg)
        self.Removebtn_3.setGeometry(QtCore.QRect(20, 470, 93, 28))
        self.Removebtn_3.setObjectName("Removebtn_3")

        self.stackedWidget.addWidget(self.VProg)
        self.Astud = QtWidgets.QWidget()
        self.Astud.setObjectName("Astud")

        self.label_8 = QtWidgets.QLabel(self.Astud)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.Astud)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 30, 131, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_9 = QtWidgets.QLabel(self.Astud)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.Astud)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.Astud)
        self.label_11.setGeometry(QtCore.QRect(20, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.Astud)
        self.label_12.setGeometry(QtCore.QRect(20, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.Astud)
        self.label_13.setGeometry(QtCore.QRect(20, 220, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.Astud)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 70, 131, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.Astud)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 110, 131, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.comboBox = QtWidgets.QComboBox(self.Astud)
        self.comboBox.setGeometry(QtCore.QRect(180, 150, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.Astud)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 190, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_3 = QtWidgets.QComboBox(self.Astud)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 230, 91, 22))
        self.comboBox_3.setObjectName("comboBox_3")

        self.pushButton = QtWidgets.QPushButton(self.Astud)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.Astud)
        self.AColl = QtWidgets.QWidget()
        self.AColl.setObjectName("AColl")

        self.label_14 = QtWidgets.QLabel(self.AColl)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(self.AColl)
        self.label_15.setGeometry(QtCore.QRect(20, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.AColl)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 40, 131, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.AColl)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 80, 231, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.pushButton_2 = QtWidgets.QPushButton(self.AColl)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.stackedWidget.addWidget(self.AColl)
        self.Aprog = QtWidgets.QWidget()
        self.Aprog.setObjectName("Aprog")
        self.label_16 = QtWidgets.QLabel(self.Aprog)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(self.Aprog)
        self.label_17.setGeometry(QtCore.QRect(30, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.Aprog)
        self.label_18.setGeometry(QtCore.QRect(30, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")

        self.lineEdit_9 = QtWidgets.QLineEdit(self.Aprog)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 20, 131, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.lineEdit_10 = QtWidgets.QLineEdit(self.Aprog)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 60, 131, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.comboBox_4 = QtWidgets.QComboBox(self.Aprog)
        self.comboBox_4.setGeometry(QtCore.QRect(170, 100, 101, 22))
        self.comboBox_4.setObjectName("comboBox_4")

        self.pushButton_3 = QtWidgets.QPushButton(self.Aprog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 93, 28))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ViewStudent.setText(_translate("MainWindow", "View Students"))
        self.ViewCollege.setText(_translate("MainWindow", "View Colleges"))
        self.ViewProgram.setText(_translate("MainWindow", "View Programs"))
        self.AddStudent.setText(_translate("MainWindow", "Add Student"))
        self.AddCollege.setText(_translate("MainWindow", "Add College"))
        self.AddProgram.setText(_translate("MainWindow", "Add Program"))
        self.label.setText(_translate("MainWindow", "Student Information System"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID #"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Year Level"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Program Code"))
        self.label_4.setText(_translate("MainWindow", "Sort by:"))
        self.label_5.setText(_translate("MainWindow", "Search by:"))
        self.SearchBtn_2.setText(_translate("MainWindow", "Search"))
        self.Removebtn_2.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Search by:"))
        self.label_3.setText(_translate("MainWindow", "Sort by:"))
        self.SearchBtn.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.Removebtn.setText(_translate("MainWindow", "Delete"))
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
        self.label_8.setText(_translate("MainWindow", "ID #:"))
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
        self.pushButton_3.setText(_translate("MainWindow", "Add Student"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
