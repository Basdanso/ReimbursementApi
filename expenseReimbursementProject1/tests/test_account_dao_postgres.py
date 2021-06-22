from unittest import TestCase

from daos.account_dao_postgres import AccountDaoPostgres
from entities.account import Account

account_dao = AccountDaoPostgres()
#account_dao = AccountDaoLocal()

test_account = Account(0, "Bas", "test@gmail.com", "password", "Employee", 2000)


def test_create_account():
    acc = account_dao.create_account(test_account)
    print('test_create_account')
    print(test_account)
    print(acc)
    assert test_account.id != 0


def test_get_account_by_id():
    account = account_dao.find_account_by_id(test_account.id)
    print('test_get_account_by_id')
    print(account)
    print(test_account)
    TestCase().assertDictEqual(account.as_json_dict(), test_account.as_json_dict())


def test_update_account():
    test_account.available = True
    update_account = account_dao.update_account(test_account)
    print('update_account.id')
    print(update_account)
    assert update_account.id == test_account.id


def test_delete_account():
    result = account_dao.delete_account(test_account.id)
    assert result == True


