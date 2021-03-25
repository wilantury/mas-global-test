import urllib.request as requests
import json

"""Data layer: retrieve data from API"""


class DataApi:
    # Request data of employees from a given API
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
    """if there is a valid employee id, then return
       the employee which match with the given id.
       if not, then return all employees.
    """
    id = int(id)
    if id == 0:
        return None, response
    for employee in response:
        if employee['id'] == id:
            return None, [employee]
    return None, []
