
class Employee:

    counter = 0

    def __init__(self, emp_id, name, emp_role, balance):

        self.emp_id = emp_id
        self.name = name
        self.emp_role = emp_role
        self.balance = balance
        Employee.counter += 1

    def __str__(self) ->str:
        return f"EmpId{self.emp_id}, EmpName{self.name}, Role{self.emp_role}, Balance{self.balance}"


    def as_json_dict(self):
        return {
            "EmployeeId": self.emp_id,
            "EmployeeName": self.name,
            "Role": self.emp_role,
            "Balance": self.balance,
        }
