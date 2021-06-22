from selenium.webdriver.chrome.webdriver import WebDriver

# Page Object Model
# A class that will contain the important elements on a web page
from selenium.webdriver.remote.webelement import WebElement


class LoginHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver  # Dependency injection of a driver into the web page

    def email(self):
        element: WebElement = self.driver.find_element_by_id("email")  # get element by id
        return element

    def password(self):
        element: WebElement = self.driver.find_element_by_id("password")  # get element by id
        return element


    def submit(self):
        element: WebElement = self.driver.find_element_by_id("submit")  # get element by id
        return element

