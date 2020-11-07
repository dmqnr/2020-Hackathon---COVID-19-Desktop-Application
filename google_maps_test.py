from PIL import Image
from io import BytesIO
import requests
import googlemaps 

api_key = 'AIzaSyCypcr5ZZ3MenFKCpH0UJPW3QldpoGO9ys'
url = "https://maps.googleapis.com/maps/api/staticmap?"
center = "China"
zoom = 10

r = requests.get(url + "center=" + center + "&zoom =14&size=400x400&key=" + api_key)

im = Image.open(BytesIO(r.content))
im.show()
        
