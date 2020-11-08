import json
import requests
from PyQt5 import QtCore, QtGui, QtWidgets

def checkNone(data):
    if data is None:
        data = "0"
    return data

def searchByCountry(country):
    querystring = {"country" : country}
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
        'x-rapidapi-key': "22d3a1185emsh3d18a46b7b639c5p131883jsncc7c7abd2aa6",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    popul = data["response"][0]["population"]
    popul = checkNone(popul)
    
    active = data["response"][0]["cases"]["active"]
    active = checkNone(active)
    
    newCases = data["response"][0]["cases"]["new"]
    newCases = checkNone(newCases)
    
    critical = data["response"][0]["cases"]["critical"]
    critical = checkNone(critical)
    
    recovered = data["response"][0]["cases"]["recovered"] 
    recovered = checkNone(recovered)
    
    totalCases = data["response"][0]["cases"]["total"] 
    totalCases = checkNone(totalCases)
    
    newDeaths = data["response"][0]["deaths"]["new"]
    newDeaths = checkNone(newDeaths)
    
    totalDeaths = data["response"][0]["deaths"]["total"]
    totalDeaths = checkNone(totalDeaths)
    
    totalTests = data["response"][0]["tests"]["total"]
    totalTests = checkNone(totalTests)
    
    date = data["response"][0]["day"]
    date = checkNone(date)

    return popul, active, newCases, critical, recovered, totalCases, newDeaths, totalDeaths, totalTests, date
