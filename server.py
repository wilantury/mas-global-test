from flask import Flask, request
from Data import data
from Logic import salary
from dotenv import load_dotenv
import os
from DTO.response import Response

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("DEBUG")
api_data = os.getenv("API")

res = Response()
salary_calc = salary.SalaryCal()

@app.route('/api')
def employees():
    id = request.args.get('id') or 0
    
    _data = data.DataApi(api_data)
    err, _data = _data.get_data()
    total_annual = salary_calc.calculate(_data[0], _data[0].get('contractTypeName'))
    _data[0]["annual salary"]=total_annual
    return res.make_res(err=err, data=_data)

if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(port=port)