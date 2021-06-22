class Account:

    def __init__(self, id: int, name: str, email: str, password: str,
                 account_type: str, open_bal: int):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        # employee / manager
        self.accountType = account_type
        self.balance = open_bal

    def __str__(self):
        return f" id= {self.id}, name= {self.name}, email= {self.email}, password= {self.password}" \
               f"accountType: {self.accountType}, balance: {self.balance}"

    def as_json_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "accountType": self.accountType,
            "balance": self.balance
        }