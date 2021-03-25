from flask import Blueprint, request
import os
# local
from Data import data
from Logic import salary
from DTO import response, employeeSerializer

employees_bp =  Blueprint('employee_bp', __name__)

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


@employees_bp.route('/api')
def employees():
    """Route that retrieve data from employees from 
       a given API
    """
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