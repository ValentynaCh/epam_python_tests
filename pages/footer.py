from selenium import webdriver
from selenium.webdriver.common.by import By


class Footer:
    policies_list_xpath: str = "//div[@class='policies-links-wrapper']//a[@class='fat-links']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def scroll_the_page_down(self):
        print("Scroll the page down")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def extract_policies_list(self):
        print("Extracting list..")
        elements = self.driver.find_elements(By.XPATH, self.policies_list_xpath)
        print("Returning a list...")
        return [(element.text,) for element in elements]

