# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from searchByCountryClass import searchByCountry
from getCountriesClass import getCountries
from google_maps_test import displayMap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 1179)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.countryList = QtWidgets.QComboBox(self.centralwidget)
        self.countryList.setGeometry(QtCore.QRect(300, 220, 141, 22))
        self.countryList.setObjectName("countryList")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 220, 181, 16))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 330, 81, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 330, 71, 20))
        self.label_3.setObjectName("label_3")
        
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(520, 220, 75, 23))
        self.search.setObjectName("search")
        
        self.population = QtWidgets.QLineEdit(self.centralwidget)
        self.population.setGeometry(QtCore.QRect(200, 330, 113, 20))
        self.population.setObjectName("population")
        
        self.newCases = QtWidgets.QLineEdit(self.centralwidget)
        self.newCases.setGeometry(QtCore.QRect(470, 330, 113, 20))
        self.newCases.setObjectName("newCases")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 400, 81, 16))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 400, 91, 16))
        self.label_5.setObjectName("label_5")
        
        self.activeCases = QtWidgets.QLineEdit(self.centralwidget)
        self.activeCases.setGeometry(QtCore.QRect(200, 400, 113, 20))
        self.activeCases.setObjectName("activeCases")
        
        self.criticalCases = QtWidgets.QLineEdit(self.centralwidget)
        self.criticalCases.setGeometry(QtCore.QRect(470, 400, 113, 20))
        self.criticalCases.setObjectName("criticalCases")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 470, 71, 16))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 530, 151, 21))
        self.label_7.setObjectName("label_7")
        
        self.newDeaths = QtWidgets.QLineEdit(self.centralwidget)
        self.newDeaths.setGeometry(QtCore.QRect(200, 470, 113, 20))
        self.newDeaths.setObjectName("newDeaths")
        
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(340, 530, 113, 20))
        self.total.setObjectName("total")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 330, 111, 16))
        self.label_8.setObjectName("label_8")
        
        self.recovered = QtWidgets.QLineEdit(self.centralwidget)
        self.recovered.setGeometry(QtCore.QRect(730, 330, 113, 20))
        self.recovered.setObjectName("recovered")
        
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(660, 220, 75, 23))
        self.exit.setObjectName("exit")
        
        self.warning_label = QtWidgets.QLabel(self.centralwidget)
        self.warning_label.setGeometry(QtCore.QRect(130, 590, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.warning_label.setFont(font)
        self.warning_label.setText("")
        self.warning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_label.setObjectName("warning_label")
        
        self.mapImage = QtWidgets.QLabel(self.centralwidget)
        self.mapImage.setGeometry(QtCore.QRect(270, 680, 400, 400))
        self.mapImage.setText("")
        self.mapImage.setObjectName("mapImage")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(370, 470, 91, 16))
        self.label_10.setObjectName("label_10")
        
        self.totalDeaths = QtWidgets.QLineEdit(self.centralwidget)
        self.totalDeaths.setGeometry(QtCore.QRect(470, 470, 113, 20))
        self.totalDeaths.setObjectName("totalDeaths")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 400, 91, 16))
        self.label_9.setObjectName("label_9")
        
        self.totalTests = QtWidgets.QLineEdit(self.centralwidget)
        self.totalTests.setGeometry(QtCore.QRect(730, 400, 113, 20))
        self.totalTests.setObjectName("totalTests")
        
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(420, 20, 171, 171))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(120, 280, 531, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVID-19 Travel Advisory"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Please select a country:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Population:"))
        self.label_3.setText(_translate("MainWindow", "New Cases:"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Active Cases:"))
        self.label_5.setText(_translate("MainWindow", "Critical Cases:"))
        self.label_6.setText(_translate("MainWindow", "New Deaths:"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Total Cases:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Recovered Cases:"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.label_10.setText(_translate("MainWindow", "Total Deaths:"))
        self.label_9.setText(_translate("MainWindow", "Total Tests:"))
        self.dateLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\"/></p></body></html>"))


    def initUI(self, MainWindow):
        for country in getCountries():
            if country != "CAR" or country != "Cura&ccedil;ao" or country != "Diamond-Princess-":
                self.countryList.addItem(country)
        self.search.clicked.connect(self.searchOnClick)
        self.exit.clicked.connect(self.exitOnClick)
        
    def searchOnClick(self, MainWindow):
        popul, active, newCases, critical, recovered, totalCases, newDeaths, totalDeaths, totalTests, date = searchByCountry(str(self.countryList.currentText()))
        self.population.setText(str(popul))
        self.newCases.setText(str(newCases))
        self.activeCases.setText(str(active))
        self.criticalCases.setText(str(critical))
        self.recovered.setText(str(recovered))
        self.total.setText(str(totalCases))
        self.newDeaths.setText(str(newDeaths))
        self.totalDeaths.setText(str(totalDeaths))
        self.totalTests.setText(str(totalTests))
        self.dateLabel.setText("Below is the data on " + str(date))
        
        qp = displayMap(str(self.countryList.currentText()))
        self.mapImage.setPixmap(qp)
        self.mapImage.resize(qp.width(), qp.height())
        
        if popul > 300000:
            if  int(newCases) >= 500:
                self.warning_label.setText("The CDC considers this country a Level 3 High Risk\nMake sure to consult all local and state regulations before traveling")
                self.warning_label.setStyleSheet("background-color: red")
            elif int(newCases) < 500 and int(newCases) > 250:
                self.warning_label.setText("The CDC considers this country a Level 2 Moderate Risk\nMake sure to consult all local and state regulations before traveling")
                self.warning_label.setStyleSheet("background-color: orange")
            elif int(newCases) <= 250:
                self.warning_label.setText("The CDC considers this country a Level 1 Low Risk\nMake sure to consult all local and state regulations before traveling")
                self.warning_label.setStyleSheet("background-color: lightgreen")

        if popul < 300000:
            if  int(newCases) > 10:
                 self.warning_label.setText("The CDC considers this country a Level 3 High Risk\nMake sure to consult all local and state regulations before traveling")
                 self.warning_label.setStyleSheet("background-color: red")
            elif int(newCases) <= 10 and int(newCases) >= 7:
                 self.warning_label.setText("The CDC considers this country a Level 2 Moderate Risk\nMake sure to consult all local and state regulations before traveling")
                 self.warning_label.setStyleSheet("background-color: orange")
            elif int(newCases) <= 6:
                 self.warning_label.setText("The CDC considers this country a Level 1 Low Risk\nMake sure to consult all local and state regulations before traveling")
                 self.warning_label.setStyleSheet("background-color: lightgreen")
                 

    def exitOnClick(self, MainWindow):
        sys.exit()
