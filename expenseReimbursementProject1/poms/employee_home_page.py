from selenium.webdriver.chrome.webdriver import WebDriver

# Page Object Model
# A class that will contain the important elements on a web page
from selenium.webdriver.remote.webelement import WebElement


class EmployeeHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver  # Dependency injection of a driver into the web page

    # Selectors are the different ways to get elements in selenium
    def home(self):
        element: WebElement = self.driver.find_element_by_id("home")  # get element by id
        return element

    def login(self):
        element: WebElement = self.driver.find_element_by_id("login")  # get element by id
        return element

    def register(self):
        element: WebElement = self.driver.find_element_by_id("register-form")  # get element by id
        return element

    def reimbursements(self):
        element: WebElement = self.driver.find_element_by_id("reimbursement")  # get element by id
        return element

    def createReim(self):
        element: WebElement = self.driver.find_element_by_id("create")  # get element by id
        return element

    def logout(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element



