class MyReimbursement:

    def __init__(self, id: int, email: str, transferAmount: int, reason: str, status: str = "Waiting"):
        self.id = id
        self.email = email
        self.transferAmount = transferAmount
        self.reason = reason
        self.status = status


    def __str__(self):
        return f"id= {self.id}, email= {self.email}, transferAmount= {self.transferAmount}, reason = {self.reason}, status= {self.status} "

    def as_json_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "transferAmount": self.transferAmount,
            "reason": self.reason,
            "status": self.status
        }
