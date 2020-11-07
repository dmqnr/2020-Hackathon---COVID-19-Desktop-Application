import json
import requests
from PyQt5 import QtCore, QtGui, QtWidgets


def searchByCountry(self, MainWindow):
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
    self.deaths.setText(str(newDeaths))