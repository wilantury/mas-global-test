from flask import Flask, request
from Data import data
from Logic import salary
from dotenv import load_dotenv
from flask_cors import CORS
import os
from DTO import response, employeeSerializer

load_dotenv()

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("DEBUG")
api_data = os.getenv("API")

res = response.Response()
salary_calc = salary.SalaryCal()

@app.route('/api')
def employees():
    id = request.args.get('id') or '0'
    
    dto_employee = employeeSerializer.EmployeeSerializer()

    _data = data.DataApi(api_data)
    err, _data = _data.get_data_id(id)
    if err:
        return res.make_res(err="Internal server error", admin_err = err, data=_data)

    dto_data = []
    try:
        for employee in _data:  
            total_annual = salary_calc.calculate(employee, employee.get('contractTypeName'))
            dto_data.append(dto_employee.serialize(employee, total_annual, employee.get('contractTypeName')))
        return res.make_res(data=dto_data)    
    except Exception as e:
        return res.make_res(err="Internal server error", admin_err = str(e), data=[])   
        

if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(port=port)