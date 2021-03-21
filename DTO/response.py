from os import stat
from flask import make_response

class Response:

    def make_res(self, err, data):
        status = 200
        if err:
            status = 500
            
        return make_response({"error": err, "Employees": data}, status)