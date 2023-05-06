# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Project_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 900))
        
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        MainWindow.setFont(font)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.field_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.field_dropdown.setGeometry(QtCore.QRect(400, 60, 160, 20))
        self.field_dropdown.setObjectName("field_dropdown")
        
        self.field_dropdown.addItem("")
        self.field_dropdown.addItem("Callsign")
        self.field_dropdown.addItem("Aircraft Type")
        self.field_dropdown.addItem("Origin")
        self.field_dropdown.addItem("Destination")
        self.field_dropdown.addItem("Registration")
        self.field_dropdown.setCurrentIndex(0)
        
        self.field_label = QtWidgets.QLabel(self.centralwidget)
        self.field_label.setGeometry(QtCore.QRect(80, 60, 300, 20))
        self.field_label.setObjectName("field_label")
        
        self.query_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.query_entry.setGeometry(QtCore.QRect(400, 100, 160, 20))
        self.query_entry.setObjectName("query_entry")
        
        self.query_label = QtWidgets.QLabel(self.centralwidget)
        self.query_label.setGeometry(QtCore.QRect(270, 100, 100, 20))
        self.query_label.setObjectName("query_label")
        
        self.results_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_1.setGeometry(QtCore.QRect(100, 610, 1080, 20))
        self.results_label_1.setText("")
        self.results_label_1.setObjectName("results_label_1")
        
        self.whole_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.whole_checkBox.setGeometry(QtCore.QRect(380, 120, 180, 20))
        self.whole_checkBox.setObjectName("whole_checkBox")
        
        self.location_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.location_checkBox.setGeometry(QtCore.QRect(180, 150, 180, 20))
        self.location_checkBox.setObjectName("location_checkBox")
        
        self.location_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.location_dropdown.setGeometry(QtCore.QRect(380, 150, 180, 20))
        self.location_dropdown.setObjectName("location_dropdown")
        
        self.location_dropdown.addItem("")
        self.location_dropdown.addItem("Nebraska")
        self.location_dropdown.addItem("North America")
        self.location_dropdown.addItem("Europe")
        self.location_dropdown.addItem("Asia")
        self.location_dropdown.setCurrentIndex(0)
        
        self.submit_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(330, 200, 90, 40))
        self.submit_button.setObjectName("submit_button")
        
        self.flight_info_label = QtWidgets.QLabel(self.centralwidget)
        self.flight_info_label.setGeometry(QtCore.QRect(600, 60, 91, 20))
        self.flight_info_label.setObjectName("flight_info_label")
        
        self.flights_label = QtWidgets.QLabel(self.centralwidget)
        self.flights_label.setGeometry(QtCore.QRect(20, 580, 60, 20))
        self.flights_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flights_label.setObjectName("flights_label")
        
        self.flight_button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_1.setGeometry(QtCore.QRect(10, 610, 80, 20))
        self.flight_button_1.setObjectName("flight_button_1")
        
        self.flight_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_2.setGeometry(QtCore.QRect(10, 640, 80, 20))
        self.flight_button_2.setObjectName("flight_button_2")
        
        self.flight_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_3.setGeometry(QtCore.QRect(10, 670, 80, 20))
        self.flight_button_3.setObjectName("flight_button_3")
        
        self.flight_button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_4.setGeometry(QtCore.QRect(10, 700, 80, 20))
        self.flight_button_4.setObjectName("flight_button_4")
        
        self.flight_button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_5.setGeometry(QtCore.QRect(10, 730, 80, 20))
        self.flight_button_5.setObjectName("flight_button_5")
        
        self.flight_button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_6.setGeometry(QtCore.QRect(10, 760, 80, 20))
        self.flight_button_6.setObjectName("flight_button_6")
        
        self.flight_button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_7.setGeometry(QtCore.QRect(10, 790, 80, 20))
        self.flight_button_7.setObjectName("flight_button_7")
        
        self.flight_button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.flight_button_8.setGeometry(QtCore.QRect(10, 820, 80, 20))
        self.flight_button_8.setObjectName("flight_button_8")
        
        self.results_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_2.setGeometry(QtCore.QRect(100, 640, 1080, 20))
        self.results_label_2.setText("")
        self.results_label_2.setObjectName("results_label_2")
        
        self.results_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_3.setGeometry(QtCore.QRect(100, 670, 1080, 20))
        self.results_label_3.setText("")
        self.results_label_3.setObjectName("results_label_3")
        
        self.results_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_4.setGeometry(QtCore.QRect(100, 700, 1080, 20))
        self.results_label_4.setText("")
        self.results_label_4.setObjectName("results_label_4")
        
        self.results_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_5.setGeometry(QtCore.QRect(100, 730, 1080, 20))
        self.results_label_5.setText("")
        self.results_label_5.setObjectName("results_label_5")
        
        self.results_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_6.setGeometry(QtCore.QRect(100, 760, 1080, 20))
        self.results_label_6.setText("")
        self.results_label_6.setObjectName("results_label_6")
        
        self.results_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_7.setGeometry(QtCore.QRect(100, 790, 1080, 20))
        self.results_label_7.setText("")
        self.results_label_7.setObjectName("results_label_7")
        
        self.results_label_8 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_8.setGeometry(QtCore.QRect(100, 820, 1080, 20))
        self.results_label_8.setText("")
        self.results_label_8.setObjectName("results_label_8")
        
        self.flight_data_label = QtWidgets.QLabel(self.centralwidget)
        self.flight_data_label.setGeometry(QtCore.QRect(600, 100, 580, 460))
        self.flight_data_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.flight_data_label.setWordWrap(True)
        self.flight_data_label.setObjectName("flight_data_label")
        
        self.results_label_0 = QtWidgets.QLabel(self.centralwidget)
        self.results_label_0.setGeometry(QtCore.QRect(100, 580, 1080, 20))
        self.results_label_0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.results_label_0.setObjectName("results_label_0")
        
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(50, 275, 500, 275))
        self.image_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.image_label.setObjectName("image_label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlightRadar24 Tool"))
        self.field_label.setText(_translate("MainWindow", "Which field would you like to query?"))
        self.query_label.setText(_translate("MainWindow", "Enter query:"))
        self.whole_checkBox.setText(_translate("MainWindow", "Match whole query?"))
        self.location_checkBox.setText(_translate("MainWindow", "Limit Results By Location?"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.flight_info_label.setText(_translate("MainWindow", "Flight Info"))
        self.flights_label.setText(_translate("MainWindow", "Flights"))
        self.flight_button_1.setText(_translate("MainWindow", "Flight 1"))
        self.flight_button_2.setText(_translate("MainWindow", "Flight 2"))
        self.flight_button_3.setText(_translate("MainWindow", "Flight 3"))
        self.flight_button_4.setText(_translate("MainWindow", "Flight 4"))
        self.flight_button_5.setText(_translate("MainWindow", "Flight 5"))
        self.flight_button_6.setText(_translate("MainWindow", "Flight 6"))
        self.flight_button_7.setText(_translate("MainWindow", "Flight 7"))
        self.flight_button_8.setText(_translate("MainWindow", "Flight 8"))
        self.flight_data_label.setText(_translate("MainWindow", "Submit a query and select a flight to view more infomation!"))
        self.results_label_0.setText(_translate("MainWindow", "Callsign  |  Airline  |  Origin  |  Dest  |  Reg       |  Type    |  Lat   |  Long   |  Alt    |  Hdg  |  Spd  |"))
