import json
import requests
from PyQt5 import QtCore, QtGui, QtWidgets


def getCountries():
    url = "https://covid-193.p.rapidapi.com/countries"
    headers = {
        'x-rapidapi-key': "22d3a1185emsh3d18a46b7b639c5p131883jsncc7c7abd2aa6",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    country = response.json()
    return country["response"]