from abc import abstractmethod, ABC

from entities.account import Account
from entities.my_reimbursements import MyReimbursement


class AccountDAO(ABC):

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def find_account(self, email):
        pass

    @abstractmethod
    def create_reimbursement(self, myReimbursement) -> MyReimbursement:
        pass

    @abstractmethod
    def get_all_reimbursements(self, status: str, email: str) -> [MyReimbursement]:
        pass

    @abstractmethod
    def get_reimbursement(self, id):
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: MyReimbursement):
        pass

    @abstractmethod
    def update_account(self, acc: Account):
        pass

    @abstractmethod
    def get_report_reimbursement(self) -> dict:
        pass