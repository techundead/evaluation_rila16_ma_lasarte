import requests

def getTemp():
    r = requests.get("http://localhost:5000/temperature")
    return r.json()

    
