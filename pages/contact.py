from selenium import webdriver
from selenium.webdriver.common.by import By

submit_button_xpath = "//button[@type = 'submit']"
ask_anything_form_xpath = "(//div[@data-required='true'] //label[@class='form-component__label']) | (//div[@data-required = 'true']//label[@class = 'checkbox__label checkbox-custom-label checkbox__label-text'])"


class Contact:
    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def click_submit_button(self) -> None:
        self.driver.find_element(By.XPATH, submit_button_xpath).click()

    def get_required_fields(self):
        elements = self.driver.find_elements(By.XPATH, ask_anything_form_xpath)
        #print([element.text for element in elements])
        return [element.text for element in elements]


