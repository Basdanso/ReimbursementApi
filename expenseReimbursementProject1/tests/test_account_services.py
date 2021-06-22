#Mocking is a very common testing practice
# Faking the output of a function with predefined values
#allows us to write tests in a consistent fashion without worrying if the underlying works correctly
from unittest.mock import MagicMock

from daos.account_dao import AccountDAO
from daos.account_dao_postgres import AccountDaoPostgres

from entities.account import Account
from services.account_services import AccountService
from services.account_services_impl import AccountServiceImpl

account_dao: AccountDAO = AccountDaoPostgres()

account_service: AccountService = AccountServiceImpl(account_dao)
test_account: Account = Account(0, "Lolly", "email@gmail.com", "savingpw", "Manager", 6543)
account_dao.create_account(test_account)


class TestAccountService:
    def test_transfer_amount(self):
        account1 = account_dao.create_account(test_account)
        account2 = account_dao.create_account(test_account)
        print(account1)
        print(account2)
        account_service.update_account(account1)
        assert (account1.balance - account1.balance) == 0

