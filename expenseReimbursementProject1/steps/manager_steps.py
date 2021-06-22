import time

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'I navigate to the Manager Home Page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:5000/home')


@when(u'I  Login In')
def step_impl(context):
    context.employee_home_page.login().click()
    time.sleep(2)


@then(u'I should be on Manager Login Page')
def step_impl(context):
    text = context.driver.title
    print(text)
    assert text == 'Login'


@when(u'I submit email')
def step_impl(context):
    context.login_home_page.email().send_keys('admin@gmail.com')
    time.sleep(2)


@when(u'I submit password')
def step_impl(context):
    context.login_home_page.password().send_keys('password')
    time.sleep(2)


@when(u'I click on enter')
def step_impl(context):
    context.login_home_page.submit().click()
    time.sleep(5)


@when(u'I submit email1')
def step_impl(context):
    context.login_home_page.email().send_keys('admin@gmail1.com')
    time.sleep(2)


@when('I click on Statistics')
def step_impl(context):
    context.manager_home_page.statistics().click()
    time.sleep(5)


@then(u'I should be on Statistics Page')
def step_impl(context):
    text = context.driver.title
    print(text)
    assert text == 'Statistics'


@when(u'I click on Display')
def step_impl(context):
    context.manager_home_page.display().click()
    time.sleep(5)


@then(u'I should be on Reimbursements Page')
def step_impl(context):
    text = context.driver.title
    print(text)
    assert text == 'Reimbursements'
