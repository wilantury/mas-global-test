class SalaryCal:
    """Calc the salary of employees.
       their salary depend of a contract type:
       - Hourly salary
       - Monthly salary
    """
    def calculate(self, employee, contract_type_name):
        salary_calculator = self._get_salary(contract_type_name)
        return salary_calculator(employee)

    def _get_salary(self, contract_type):
        if contract_type == "HourlySalaryEmployee":
            return lambda employee: employee['hourlySalary'] * 12 * 120
        elif contract_type == "MonthlySalaryEmployee":
            return lambda employee: employee['monthlySalary'] * 12
        else:
            raise ValueError(contract_type)
