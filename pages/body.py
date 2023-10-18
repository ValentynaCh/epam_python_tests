from selenium import webdriver
from selenium.webdriver.common.by import By


class Body:
    location_list_xpath = "//div[@class = 'tabs-23__ul js-tabs-links-list']//a"
    location_item_xpath = "//div[@class = 'tabs-23__ul js-tabs-links-list']//a[text() = '{}']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def get_our_location(self):
        location_list = self.driver.find_elements(By.XPATH, self.location_list_xpath)
        print("Returning a list of our location block...")
        return [element.text for element in location_list]


    def check_selected_location(self, location: str):
        return self.driver.find_element(By.XPATH, self.location_item_xpath.format(location)).get_attribute('class')

    def click_location (self, location: str) -> None:
        self.driver.find_element(By.XPATH, self.location_item_xpath.format(location)).click()


