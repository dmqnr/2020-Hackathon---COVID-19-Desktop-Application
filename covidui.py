# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from searchByCountryClass import searchByCountry
from getCountriesClass import getCountries

"""def getCountries():
    url = "https://covid-193.p.rapidapi.com/countries"
    headers = {
        'x-rapidapi-key': "22d3a1185emsh3d18a46b7b639c5p131883jsncc7c7abd2aa6",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    country = response.json()
    return country["response"]"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.countryList = QtWidgets.QComboBox(self.centralwidget)
        self.countryList.setGeometry(QtCore.QRect(258, 30, 131, 22))
        self.countryList.setObjectName("countryList")
        for country in getCountries():
            self.countryList.addItem(country)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 100, 71, 20))
        self.label_3.setObjectName("label_3")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(490, 30, 75, 23))
        self.search.setObjectName("search")
        self.search.clicked.connect(self.searchOnClick)
        self.population = QtWidgets.QLineEdit(self.centralwidget)
        self.population.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.population.setObjectName("population")
        self.newCases = QtWidgets.QLineEdit(self.centralwidget)
        self.newCases.setGeometry(QtCore.QRect(410, 100, 113, 20))
        self.newCases.setObjectName("newCases")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 170, 91, 16))
        self.label_5.setObjectName("label_5")
        self.activeCases = QtWidgets.QLineEdit(self.centralwidget)
        self.activeCases.setGeometry(QtCore.QRect(170, 170, 113, 20))
        self.activeCases.setObjectName("activeCases")
        self.criticalCases = QtWidgets.QLineEdit(self.centralwidget)
        self.criticalCases.setGeometry(QtCore.QRect(440, 170, 113, 20))
        self.criticalCases.setObjectName("criticalCases")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 240, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 330, 151, 16))
        self.label_7.setObjectName("label_7")
        self.deaths = QtWidgets.QLineEdit(self.centralwidget)
        self.deaths.setGeometry(QtCore.QRect(170, 240, 113, 20))
        self.deaths.setObjectName("deaths")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(310, 330, 113, 20))
        self.total.setObjectName("total")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 240, 111, 16))
        self.label_8.setObjectName("label_8")
        self.recovered = QtWidgets.QLineEdit(self.centralwidget)
        self.recovered.setGeometry(QtCore.QRect(440, 240, 113, 20))
        self.recovered.setObjectName("recovered")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(630, 30, 75, 23))
        self.warning_label = QtWidgets.QLabel(self.centralwidget)
        self.warning_label.setGeometry(QtCore.QRect(100, 390, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.warning_label.setFont(font)
        self.warning_label.setText("")
        self.warning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_label.setObjectName("warning_label")
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please select a country:"))
        self.label_2.setText(_translate("MainWindow", "Population:"))
        self.label_3.setText(_translate("MainWindow", "New Cases:"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Active Cases:"))
        self.label_5.setText(_translate("MainWindow", "Critical Cases:"))
        self.label_6.setText(_translate("MainWindow", "Deaths:"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Total Cases:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Recovered Cases:"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        
    def searchOnClick(self, MainWindow):
        popul, active, newCases, critical, recovered, totalCases, newDeaths, totalDeaths = searchByCountry(str(self.countryList.currentText()))
        self.population.setText(str(popul))
        self.newCases.setText(str(newCases))
        self.activeCases.setText(str(active))
        self.criticalCases.setText(str(critical))
        self.recovered.setText(str(recovered))
        self.total.setText(str(totalCases))
        self.deaths.setText(str(newDeaths))
        
        if  totalCases >= 100000:
            self.warning_label.setText("We do not recommend traveling here.")
        elif totalCases < 100000 and totalCases >= 10000:
            self.warning_label.setText("Travel here at your own discretion.")
        elif totalCases < 10000:
            self.warning_label.setText("Be cautious traveling here.")
        

    """def searchByCountry(self, MainWindow):
        country = str(self.countryList.currentText())
        print(country)
        querystring = {"country" : country}
        url = "https://covid-193.p.rapidapi.com/statistics"
        headers = {
            'x-rapidapi-key': "22d3a1185emsh3d18a46b7b639c5p131883jsncc7c7abd2aa6",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        popul = data["response"][0]["population"]
        active = data["response"][0]["cases"]["active"]
        new = data["response"][0]["cases"]["new"]
        critical = data["response"][0]["cases"]["critical"]
        recovered = data["response"][0]["cases"]["recovered"] 
        total = data["response"][0]["cases"]["total"] 
        newDeaths = data["response"][0]["deaths"]["new"]
        totalDeaths = data["response"][0]["deaths"]["total"]
        self.population.setText(str(popul))
        self.newCases.setText(str(new))
        self.activeCases.setText(str(active))
        self.criticalCases.setText(str(critical))
        self.recovered.setText(str(recovered))
        self.total.setText(str(total))
        self.deaths.setText(str(newDeaths))"""
    
    
"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""

