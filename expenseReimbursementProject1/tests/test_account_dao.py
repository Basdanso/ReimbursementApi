from daos.account_dao import AccountDAO
from daos.account_dao_postgres import AccountDaoPostgres
from entities.account import Account
from exceptions.not_found_exception import ResourceNotFoundError
from unittest import TestCase
from unittest.mock import MagicMock

account_dao: AccountDAO = AccountDaoPostgres()

test_account = Account(1, "email@gmail.com", "Jamas", "Current", "New York", 4321)


####
def test_get_reimbursement():
    account = account_dao.get_reimbursement(test_account.id)


def test_update_account():
    pass


def test_find_account():
    result = account_dao.find_account(test_account.email)


def test_get_all_accounts():
    account1 = Account(0, "Bas", "email@gmail.com", "passw1", "Employee", 4321)
    account2 = Account(0, "Adam", "aa@gmail.com", "passw2", "Manager", 7112)
    account_dao.create_account(account1)
    account_dao.create_account(account2)
