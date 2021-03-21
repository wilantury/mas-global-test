class SalaryCal:

    def calculate(self, employee, contract_type_name):
        salary_calculator = self._get_salary(contract_type_name)
        return salary_calculator(employee)
    
    def _get_salary(self, contract_type):
        if contract_type == "HourlySalaryEmployee":
            return self._salary_calc_hourly_employee
        elif contract_type == "MonthlySalaryEmployee":
            return self._salary_calc_monthly_employee
        else:
            raise ValueError(contract_type)
    
    def _salary_calc_hourly_employee(self, employee):
        return employee['hourlySalary'] * 12 * 120
    
    def _salary_calc_monthly_employee(self, employee):
        return employee['monthlySalary'] * 12

