from daos.account_dao import AccountDAO
from entities.account import Account
from connection_utils import connection
from entities.my_reimbursements import MyReimbursement


class AccountDaoPostgres(AccountDAO):

    def create_account(self, account: Account) -> Account:
        try:
            sql = """ insert into account(name, email, password, account_type, balance)
              values (%s, %s, %s, %s, %s) returning id """
            cursor = connection.cursor()
            cursor.execute(sql, [account.name, account.email, account.password, account.accountType, account.balance])
            connection.commit()
            account.id = cursor.fetchone()[0]
            return account
        except Exception as e:
            print(e)
            return None

    def find_account(self, email):
        try:
            sql = """select * from account where email = %s """
            cursor = connection.cursor()
            cursor.execute(sql, [email])
            connection.commit()
            record = cursor.fetchone()
            account = Account(*record)
            return account
        except Exception as e:
            print(e)
        return None

    def find_account_by_id(self, id):
        try:
            sql = """select * from account where id = %s """
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            connection.commit()
            record = cursor.fetchone()
            account = Account(*record)
            return account
        except Exception as e:
            print(e)
        return None

    def create_reimbursement(self, myReimbursement) -> MyReimbursement:
        try:
            sql = """ insert into my_reimbursement(email, transfer_amount, reason, status)
              values (%s, %s, %s, %s) returning id """
            cursor = connection.cursor()
            cursor.execute(sql, [myReimbursement.email, myReimbursement.transferAmount, myReimbursement.reason,
                                 myReimbursement.status])
            connection.commit()
            myReimbursement.id = cursor.fetchone()[0]
            return myReimbursement
        except Exception as e:
            print(e)
        return None

    def get_all_reimbursements(self, status: str, email: str) -> [MyReimbursement]:
        if len(email) == 0:
            # return all for managers
            try:
                sql = """select * from my_reimbursement where status = %s """
                cursor = connection.cursor()
                cursor.execute(sql, [status])
                connection.commit()
                record = cursor.fetchall()
                myReimbursementList = []
                for t in record:
                    myReimbursement = MyReimbursement(*t)
                    myReimbursementList.append(myReimbursement)
                return myReimbursementList
            except Exception as e:
                print(e)
            return None

        # for employee
        try:
            sql = """select * from my_reimbursement where status = %s and email = %s"""
            cursor = connection.cursor()
            cursor.execute(sql, [status, email])
            connection.commit()
            record = cursor.fetchall()
            myReimbursementList = []
            for t in record:
                myReimbursement = MyReimbursement(*t)
                myReimbursementList.append(myReimbursement)
            return myReimbursementList
        except Exception as e:
            print(e)
        return None

    def get_reimbursement(self, id: str) -> MyReimbursement:
        try:
            sql = """select * from my_reimbursement where id = %s """
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            connection.commit()
            record = cursor.fetchone()
            myReimbursement = MyReimbursement(*record)
            return myReimbursement
        except Exception as e:
            print(e)
        return None

    def update_reimbursement(self, reimbursement: MyReimbursement):
        try:
            sql = """update my_reimbursement set status = %s where id = %s """
            cursor = connection.cursor()
            cursor.execute(sql, [reimbursement.status, reimbursement.id])
            connection.commit()
            # record = cursor.fetchone()
            # myReimbursement = MyReimbursement(*record)
            return reimbursement
        except Exception as e:
            print(e)
        return None

    def update_account(self, acc: Account):
        try:
            sql = """update account set balance = %s where id = %s """
            cursor = connection.cursor()
            cursor.execute(sql, [acc.balance, acc.id])
            connection.commit()
            return acc
        except Exception as e:
            print(e)
        return None

    def get_report_reimbursement(self) -> dict:
        try:
            sql = """select min(transfer_amount), max(transfer_amount),round(avg(transfer_amount)), 
            sum(transfer_amount) from my_reimbursement; """
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            record = cursor.fetchone()
            report = {'min': record[0], 'max': record[1], 'average': int(record[2]), 'sum': record[3]}
            return report
        except Exception as e:
            print(e)
        return None

    def delete_account(self, account_id):
        try:
            sql = """delete from account where id = %s """
            cursor = connection.cursor()
            cursor.execute(sql, [account_id])
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
