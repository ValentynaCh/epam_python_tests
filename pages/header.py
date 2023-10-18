from selenium import webdriver
from selenium.webdriver.common.by import By


class Header:
    color_mode_button_xpath: str = "(//div[@class='switch'])[2]"
    current_color_mode_xpath: str = "//body[contains(@class, '{}')]"
    language_dropdown_xpath: str = "(//span[@class='location-selector__button-language'])[2]"
    locales_block_xpath: str = "(//li/a[@lang='uk'])[2]"
    search_button_xpath: str = "//button[@class='header-search__button header__icon']"
    search_form_xpath: str = "//input[@id='new_form_search']"
    find_button_xpath: str = "//button[@class='custom-button button-text font-900 gradient-border-button large-gradient-button uppercase-text custom-search-button']"

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def click_on_color_mode_button(self) -> None:
        print("Clicking on header [Color Mode] button")
        self.driver.find_element(By.XPATH, self.color_mode_button_xpath).click()

    def is_color_mode_selected(self, color_mode: str) -> bool:
        print(f"Is color mode [{color_mode}] selected")
        return self.driver.find_element(By.XPATH, self.current_color_mode_xpath.format(color_mode)).is_displayed()

    def change_locale_to_ua(self) -> None:
        print("Click on language dropdown")
        self.driver.find_element(By.XPATH, self.language_dropdown_xpath).click()
        print("Select [UA] language locale")
        self.driver.find_element(By.XPATH, self.locales_block_xpath).click()
        print("[UA] language is selected")

    def get_current_locale(self) -> str:
        print("Get current locale")
        return self.driver.find_element(By.XPATH, self.language_dropdown_xpath).text

    def click_search(self) -> None:
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def input_into_search_form(self):
        self.driver.find_element(By.XPATH, self.search_form_xpath).send_keys("AI")

    def click_find_button(self):
        self.driver.find_element(By.XPATH, self.find_button_xpath).click()
