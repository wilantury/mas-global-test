# Flask
from flask import Flask, request
import os

# Libraries
from flask_cors import CORS
from dotenv import load_dotenv

# local
from Data import data
from Logic import salary
from DTO import response, employeeSerializer

load_dotenv()

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": os.getenv("URL_CLIENT")}})

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("DEBUG")
api_data = os.getenv("API")

# instance of Classes
res = response.Response()
salary_calc = salary.SalaryCal()


def employee_serialize(dto, employee):
    # return a employee with annual salary
    total_annual = salary_calc.calculate(
        employee, employee.get('contractTypeName'))
    return dto.serialize(
        employee, total_annual, employee.get('contractTypeName'))


@app.route('/api')
def employees():
    id = request.args.get('id') or '0'

    dto_employee = employeeSerializer.EmployeeSerializer()

    _data = data.DataApi(api_data)
    err, _data = _data.get_data_id(id)
    print(_data)

    if err:
        return res.make_res(err="Internal server error", admin_err=err,
                            data=_data)
    try:
        dto_data = [employee_serialize(dto_employee, employee) for employee in _data]
        return res.make_res(data=dto_data)
    except Exception as e:
        return res.make_res(
            err="Internal server error", admin_err=str(e), data=[])


if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(port=port)
