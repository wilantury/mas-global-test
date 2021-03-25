
class EmployeeSerializer:
    """Return a employee with the annual salary, which it depends
       of the contract type.
    """
    def serialize(self, employee, annualSalary, contract_type):
        serializer = self._get_serializer(contract_type)
        return serializer(annualSalary, employee)

    def _get_serializer(self, contract_type):
        if contract_type == 'HourlySalaryEmployee':
            return self._serialize_to_hourly_contract
        elif contract_type == 'MonthlySalaryEmployee':
            return self._serialize_to_monthly_contract
        else:
            raise ValueError(contract_type)

    def _serialize_to_hourly_contract(self, annualSalary, employee):
        # employee with hourly contract
        payload = {
            "id": employee['id'],
            "name": employee['name'],
            "contractTypeName": employee['contractTypeName'],
            "roleId": employee['roleId'],
            "roleName": employee['roleName'],
            "roleDescription": employee['roleDescription'],
            "baseSalary": employee['hourlySalary'],
            "annualSalary": annualSalary
        }
        return payload

    def _serialize_to_monthly_contract(self, annualSalary, employee):
        # employee with monthly contract
        payload = {
            "id": employee['id'],
            "name": employee['name'],
            "contractTypeName": employee['contractTypeName'],
            "roleId": employee['roleId'],
            "roleName": employee['roleName'],
            "roleDescription": employee['roleDescription'],
            "baseSalary": employee['monthlySalary'],
            "annualSalary": annualSalary
        }
        return payload
