import urllib.request as requests
import json

"""Data layer: retrieve data from API"""
class DataApi:
    def __init__(self, API):
        self.API = API
    
    def get_data(self):
        try:
            response = requests.urlopen(self.API)
            response = response.read()
            return None, json.loads(response.decode('utf-8'))
        except Exception as e:
            return e, {}

