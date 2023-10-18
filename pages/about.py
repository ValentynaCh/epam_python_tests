from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class About:
    company_logo_xpath: str = "//a[@class = 'header__logo-container desktop-logo']"
    download_overview_xpath: str = "//span[@class = 'button__content button__content--desktop']"


    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver = driver

    def click_company_logo(self) -> None:
        self.driver.find_element(By.XPATH, self.company_logo_xpath).click()

    def click_download_button(self) -> None:
        self.driver.find_element(By.XPATH, self.download_overview_xpath)

    @staticmethod
    def is_file_downloaded(file_download_path, file_name) -> bool:
        flag = False
        directory = os.path.expanduser("~") + "/Downloads"
        content = os.listdir(directory)
        for file in content:
            if file == file_name:
                flag = True
        return flag
