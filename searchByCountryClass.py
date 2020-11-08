import json
import requests
from PyQt5 import QtCore, QtGui, QtWidgets


def searchByCountry(country):
    querystring = {"country" : country}
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
        'x-rapidapi-key': "22d3a1185emsh3d18a46b7b639c5p131883jsncc7c7abd2aa6",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    data = response.json()
    popul = data["response"][0]["population"]
    active = data["response"][0]["cases"]["active"]
    newCases = data["response"][0]["cases"]["new"]
    critical = data["response"][0]["cases"]["critical"]
    recovered = data["response"][0]["cases"]["recovered"] 
    totalCases = data["response"][0]["cases"]["total"] 
    newDeaths = data["response"][0]["deaths"]["new"]
    totalDeaths = data["response"][0]["deaths"]["total"]
    totalTests = data["response"][0]["tests"]["total"]
    date = data["response"][0]["day"]
    return popul, active, newCases, critical, recovered, totalCases, newDeaths, totalDeaths, totalTests, date