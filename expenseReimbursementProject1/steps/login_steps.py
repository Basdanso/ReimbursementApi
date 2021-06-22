import time

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'I navigate to the Employee Home Page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:5000/home')



@when(u'I click on Login')
def step_impl(context):
    context.employee_home_page.login().click()
    time.sleep(2)


@then(u'I should be on Employee Login Page')
def step_impl(context):

    text = context.driver.title
    time.sleep(2)
    print(text)
    assert text =='Login'


@when(u'I enter email')
def step_impl(context):
    context.login_home_page.email().send_keys('abcd@gmail.com')
    time.sleep(2)

@when(u'I enter password')
def step_impl(context):
    context.login_home_page.password().send_keys('password')
    time.sleep(2)

@when(u'I click on submit')
def step_impl(context):
    context.login_home_page.submit().click()

@when(u'I submit email as Employee')
def step_impl(context):
    context.login_home_page.email().send_keys('abcd@gmail.com')
    time.sleep(2)

@when(u'I submit password as Employee')
def step_impl(context):
    context.login_home_page.password().send_keys('password')
    time.sleep(2)

@when(u'I submit email1 as Employee')
def step_impl(context):
    context.login_home_page.email().send_keys('abcd@gmail1.com')
    time.sleep(2)


















