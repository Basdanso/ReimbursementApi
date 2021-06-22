from lib2to3.pgen2 import driver
from telnetlib import EC

from selenium.webdriver.chrome.webdriver import WebDriver

# Page Object Model
# A class that will contain the important elements on a web page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class ManagerHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver  # Dependency injection of a driver into the web page

    # Selectors are the different ways to get elements in selenium
    def home(self):
        element: WebElement = self.driver.find_element_by_id("home")  # get element by id
        return element

    def statistics(self):
        element: WebElement = self.driver.find_element_by_id("statistics")  # get element by id
        return element

    def display(self):
        element: WebElement = self.driver.find_element_by_id("display")  # get element by id
        return element


    def logout(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element