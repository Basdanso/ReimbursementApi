from entities.employees import Employee


class ReimbursementAccount(Employee):

    def __init__(self, account_id: int, name: str, emp_role, balance=0, emp_id=0, user_id=0):
        super().__init__(emp_id, name, emp_role, balance)

        self.account_id = account_id
        self.name = name
        self.emp_role = emp_role
        self.balance = balance
        self.emp_id = emp_id
        self.user_id = user_id

    def __str__(self):
        return f" id= {self.account_id}, name= {self.name}, emp_role= {self.emp_role}, balance= {self.balance}, " \
               f"emp_id: {self.emp_id}, user_id: {self.user_id},"

    def as_json_dict(self):
        return {
            "accountId": self.account_id,
            "Name": self.name,
            "EmpRole": self.emp_role,
            "Balance": self.balance,
            "EmployeeId": self.emp_id,
            "UserId": self.user_id,
        }


account = Account(0, 'Basiru','Manager', 2000, 1, 1)
print(account)
#print(Account.counter)