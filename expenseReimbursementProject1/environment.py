from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from behave.runner import Context
from selenium import webdriver

from poms.employee_home_page import EmployeeHomePage
from poms.login_home_page import LoginHomePage
from poms.manager_home_page import ManagerHomePage
from poms.reimbursement_home_page import ReimbursementHomePage


def before_all(context: Context):
    context.driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\seleneum\\chromedriver_win32\\chromedriver.exe')

    context.employee_home_page = EmployeeHomePage(context.driver)
    context.login_home_page = LoginHomePage(context.driver)
    context.reimbursement_home_page = ReimbursementHomePage(context.driver)
    context.manager_home_page = ManagerHomePage(context.driver)



def after_all(context: Context):
    context.driver.quit()







# def before_all(context: Context):
#   # Idelly you attach the web driver
#   context.driver: WebDriver = webdriver.Chrome('C:\\Users\user\\Desktop\\chromedriver\\chromedriver_win32\\chromedriver.exe')
#   context.employeeHomePage = EmployeeHomePage(context.driver)  # by creating a POM our code is leaner and easier to
#   print("I run before any scenario")


# def after_all(context):
#    print("I run after all scenarios")
#   context.driver.quit()
