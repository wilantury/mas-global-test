import urllib.request as requests
import json

"""Data layer: retrieve data from API"""
class DataApi:
    def __init__(self, API):
        self.API = API
    
    def get_data_id(self, id):
        try:
            response = requests.urlopen(self.API)
            response = response.read()
            response = json.loads(response.decode('utf-8'))
            return _retrieve_employee_id(response, id)

        except Exception as e:
            return str(e), []


def _retrieve_employee_id(response, id):
    id = int(id)
    if id == 0:
        return None, response
    for employee in response:
        if employee['id'] == id:
            return None, [employee]
    return None, []
