from src.Logic import salary
from src.tests.mocks import employee
from src.DTO.employeeSerializer import EmployeeSerializer 

salary_calc = salary.SalaryCal()
employee_serializer = EmployeeSerializer()

def test_calc_hourly_salary():
    assert salary_calc.calculate(
        employee.employee_hourly_contract, "HourlySalaryEmployee") == 14400000


def test_calc_monthly_salary():
    assert salary_calc.calculate(
        employee.employee_monthly_contract, "MonthlySalaryEmployee") == 600000

def test_dto_employee():
    assert employee_serializer.serialize(
        employee.employee_hourly_contract,
        14400000, "HourlySalaryEmployee") == employee.employee_serialize
