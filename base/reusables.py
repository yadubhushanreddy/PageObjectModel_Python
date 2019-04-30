from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from utilities import custom_logger as cl
import logging


class Reusable:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partial":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        else:
            print("Locator type "+locator_type+" not supported")

    def get_title(self):
        return self.driver.title

    def get_element(self, locator, locator_type="id"):
        locator_type = locator_type.lower()
        element = self.driver.find_element(self.get_by_type(locator_type), locator)
        return element

    def click_element(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        element.click()
        print("Clicked on element with locator {0} and locator type {1}".
              format(locator, locator_type))
        self.log.info("Clicked on element with locator {0} and locator type {1}".
                      format(locator, locator_type))

    def send_data(self, test_data, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        element.send_keys(test_data)
        print("Sent data to element with locator {0} and locator type {1}".
              format(locator, locator_type))
        self.log.info("Sent data to element with locator {0} and locator type {1}".
                      format(locator, locator_type))

    def mouse_hover(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        action_chn = ActionChains(self.driver)
        action_chn.move_to_element(element).perform()
        print("Mouse hovered on element with locator {0} and locator type {1}"
              .format(locator, locator_type))
        self.log.info("Mouse hovered on element with locator {0} and locator type {1}"
                      .format(locator, locator_type))

    def element_display(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        element.is_displayed()
        print("Element with locator {0} and locator type {1} was displayed"
              .format(locator, locator_type))
        self.log.info("Element with locator {0} and locator type {1} was displayed"
                      .format(locator, locator_type))

    def wait_for_element(self, locator, locator_type="id",
                         timeout=20, poll_frequency=0.5):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, timeout=timeout,
                             poll_frequency=poll_frequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((by_type, locator)))
        return element

    def wait_for_title(self, expected_title,
                       timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(self.driver, timeout=timeout,
                             poll_frequency=poll_frequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.title_contains(expected_title))
        return element










