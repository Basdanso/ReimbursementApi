class ReimbursementChartInfo:

    def __init__(self, status: str, amount: int):
        self.amount = amount
        self.status = status

    def __str__(self):
        return f"id=  amount= {self.amount}, status= {self.status} "

    def as_json_dict(self):
        return {
            "amount": self.amount,
            "status": self.status
        }
