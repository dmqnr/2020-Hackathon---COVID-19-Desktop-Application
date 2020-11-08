from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import requests

def displayMap(center):
    api_key = 'AIzaSyCypcr5ZZ3MenFKCpH0UJPW3QldpoGO9ys'
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    zoom = 10
    r = requests.get(url + "center=" + center + "&zoom =14&size=400x400&key=" + api_key)
    image = r.content

    qp = QPixmap()
    qp.loadFromData(image)
    return qp


