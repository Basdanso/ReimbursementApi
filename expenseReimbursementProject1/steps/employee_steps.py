import time

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'I navigate to the Create Reimbursements Page')
def step_impl(context):
    context.driver.get(
        'file:///C:/Users/user/PycharmProjects/expenseReimbursementProject1/views/templates/createReim.html')
    time.sleep(3)
    text = context.driver.title
    print(text)
    assert text == 'Create'


@when(u'I submit an email')
def step_impl(context):
    context.reimbursement_home_page.email().send_keys('email@gmail.com')
    time.sleep(2)


@when(u'I submit amount')
def step_impl(context):
    context.reimbursement_home_page.amount().send_keys(100)
    time.sleep(2)

@when(u'I submit reason')
def step_impl(context):
    context.reimbursement_home_page.reason().send_keys('travel')
    time.sleep(2)


@when(u'I enter on submit')
def step_impl(context):
    context.reimbursement_home_page.submit().click()
    time.sleep(2)
