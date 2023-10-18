from selenium import webdriver

from enums.browsers import Browsers
from exceptions.no_browser import NoBrowser


class Drivers:
    BASE_URL = "https://www.epam.com/"

    @staticmethod
    def get_driver(browser_type: str) -> webdriver:
        if browser_type is Browsers.firefox:
            return Drivers.__get_firefox()
        elif browser_type is Browsers.chrome:
            return Drivers.__get_chrome()
        else:
            raise NoBrowser(browser_type)

    @staticmethod
    def __get_firefox() -> webdriver:
        driver: webdriver = webdriver.Firefox()
        # Here you can set up browser options, capabilities etc.
        Drivers.__get_base_browser_options(driver)
        return driver

    @staticmethod
    def __get_chrome() -> webdriver:
        driver: webdriver = webdriver.Chrome()
        # Here you can set up browser options, capabilities etc.
        Drivers.__get_base_browser_options(driver)
        return driver

    @staticmethod
    def __get_base_browser_options(driver: webdriver) -> webdriver:
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(Drivers.BASE_URL)
