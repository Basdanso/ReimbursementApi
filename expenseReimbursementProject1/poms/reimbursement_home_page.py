from selenium.webdriver.chrome.webdriver import WebDriver

# Page Object Model
# A class that will contain the important elements on a web page
from selenium.webdriver.remote.webelement import WebElement


class ReimbursementHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def email(self):
        element: WebElement = self.driver.find_element_by_id("email")  # get element by id
        return element

    def amount(self):
        element: WebElement = self.driver.find_element_by_id("amount")  # get element by id
        return element

    def reason(self):
        element: WebElement = self.driver.find_element_by_id("reason")  # get element by id
        return element

    def submit(self):
        element: WebElement = self.driver.find_element_by_id("submit")  # get element by id
        return element
