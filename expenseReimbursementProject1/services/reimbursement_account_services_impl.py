from daos.account_dao import AccountDAO

from entities.account import Account
from entities.my_reimbursements import MyReimbursement
from services.reimbursements_account_services import AccountService


class AccountServiceImpl(AccountService):

    def __init__(self, account_dao: AccountDAO):
        self.account_dao = account_dao

    def create_account(self, account: Account) -> Account:
        return self.account_dao.create_account(account)

    def find_account(self, email):
        return self.account_dao.find_account(email)

    def create_reimbursement(self, myReimbursement: MyReimbursement) -> MyReimbursement:
        return self.account_dao.create_reimbursement(myReimbursement)

    def get_all_reimbursements(self, status: str) -> [MyReimbursement]:
        return self.account_dao.get_all_reimbursements(status)

    def get_reimbursement(self, id):
        return self.account_dao.get_reimbursement(id)

    def update_reimbursement(self, reimbursement: MyReimbursement):
        return self.account_dao.update_reimbursement(reimbursement)