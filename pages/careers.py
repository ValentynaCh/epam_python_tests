from selenium import webdriver
from selenium.webdriver.common.by import By


class Careers:
    language_dropdown_xpath: str = "//button[@class='location-selector__button']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def get_current_locale(self) -> str:
        print("Get new current locale")
        return self.driver.find_element(By.XPATH, self.language_dropdown_xpath).text
