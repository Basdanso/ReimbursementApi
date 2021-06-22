from abc import ABC, abstractmethod

from entities.account import Account
from entities.my_reimbursements import MyReimbursement


class AccountService(ABC):
    @abstractmethod
    def create_account(self, account: Account):
        pass

    def find_account(self, email):
        pass

    def create_reimbursement(self, myReimbursement: MyReimbursement):
        pass

    def get_all_reimbursements(self, status: str, email: str) -> [MyReimbursement]:
        pass

    def get_reimbursement(self, id):
        pass

    def update_reimbursement(self, reimbursement: MyReimbursement):
        pass

    def update_account(self, acc : Account):
        pass

    def get_report_reimbursement(self) -> dict:
        pass