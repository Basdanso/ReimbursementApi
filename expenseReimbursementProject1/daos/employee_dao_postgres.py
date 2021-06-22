from abc import ABC
from typing import List
from connection_utils import connection
from daos.employee_daao import EmployeeDAO
from entities.employees import Employee
from exceptions.not_found_exception import ResourceNotFoundError


class EmployeeDaoPostgres(EmployeeDAO, ABC):

    def create_account_by_emp_id(self, employee: Employee) -> Employee:
        try:
            sql = """ insert into employees(name, emp_role, balance)
              values (%s, %s, %s) returning emp_id """
            cursor = connection.cursor()
            cursor.execute(sql, [employee.emp_id, employee.name, employee.emp_role])
            connection.commit()
            employee.emp_id = cursor.fetchone()[0]
        except Exception as e:
            print(e)
        return employee

    def get_account_by_id(self, emp_id: int) -> Employee:

        sql = """select * from employees where emp_id = %s """
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        account = Employee(*record)
        return account

    def get_all_account_by_user_id(self, user_id: int) -> [Employee]:
        sql = """select * from employees where user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        records = cursor.fetchall()
        employees = [Employee(*record) for record in records]
        if len(employees) == 0:
            raise ResourceNotFoundError
        return employees

    def get_accounts_by_user_id_and_range(self, user_id: int, lower: int, grater: int) -> [Employee]:
        sql = """select * from employees where user_id = %s and balance between %s and %s """
        cursor = connection.cursor()
        cursor.execute(sql, [user_id, lower, grater])
        # cursor.execute(sql, [lower, grater])
        records = cursor.fetchall()
        employees = [Employee(*record) for record in records]
        if len(employees) == 0:
            raise ResourceNotFoundError
        return employees

    def get_account_by_user_id_and_employee_id(self, user_id: int, emp_id: int) -> Employee:
        sql = """select * from employees where user_id= %s and emp_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id, emp_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        employee = Employee(*record)
        return employee

    def update_account_by_user_id_and_emp_id(self, employee: Employee, user_id: int, emp_id: int) -> Employee:
        sql = """update employees set name = %s, balance = %s where emp_id = %s and user_id = %s returning 
        emp_id, user_id ; """
        cursor = connection.cursor()
        cursor.execute(sql, [employee.balance, emp_id, user_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        employee.emp_id = record[0]
        employee.user_id = record[1]
        return employee

    def get_all_accounts(self) -> List[Employee]:
        sql = """select * from employees"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employee_list = []
        for record in records:
            employee_list.append(Employee(*record))
        return employee_list

    def delete_account_by_user_id_and_emp_id(self, user_id: int, emp_id: int) -> bool:
        sql = """delete from employees where user_id = %s and emp_id = %s returning emp_id ;"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id, emp_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        return True

    def delete__account_by_user_id(self, user_id: int) -> bool:
        sql = """delete from employee where user_id = %s ;"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        return True

    def update_account(self, employee: Employee) -> Employee:
        sql = """update employee set name = %s, emp_role = %s, balance = %s where emp_id = %s AND user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (
            employee.emp_id, employee.name, employee.emp_role, employee.balance
        ))
        connection.commit()
        return employee

    def delete_account_by_id(self, emp_id: int) -> bool:
        sql = """delete from employees where emp_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        connection.commit()
        return True

    def update_account_balance_by_emp_id(self, balance: int, emp_id: int):
        sql = """update employees set balance = %s where emp_id = %s returning emp_id;"""
        cursor = connection.cursor()
        cursor.execute(sql, [balance, emp_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        return True
