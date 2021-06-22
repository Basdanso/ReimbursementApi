from abc import abstractmethod, ABC
from typing import List

from entities.employees import Employee


class EmployeeDAO(ABC):


    @abstractmethod
    def create_account_by_emp_id(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_account_by_id(self, emp_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_accounts(self) -> List[Employee]:
        pass

    @abstractmethod
    def update_account(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def delete_account_by_id(self, emp_id: int) -> bool:
        pass

    @abstractmethod
    def update_account_balance_by_emp_id(self, balance: int, emp_id: int):
        pass

    @abstractmethod
    def delete__account_by_user_id(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def delete_account_by_user_id_and_emp_id(self, user_id: int, emp_id: int) -> bool:
        pass

    @abstractmethod
    def update_account_by_user_id_and_emp_id(self, employee: Employee, user_id: int, emp_id: int) -> Employee:
        pass

    @abstractmethod
    def get_account_by_user_id_and_emp_id(self, user_id: int, emp_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_account_by_user_id(self, user_id: int) -> [Employee]:
        pass

