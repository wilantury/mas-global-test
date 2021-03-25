from flask import make_response


class Response:
    """Build a response to send to client"""
    def make_res(self, data, err=None, admin_err=None):
        status = 200
        if err:
            print("Error:", admin_err)
            status = 500

        return make_response({"error": err, "Employees": data}, status)
