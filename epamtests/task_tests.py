import unittest

from selenium import webdriver

from core.driver_manager import Drivers
from enums.browsers import Browsers
from pages.header import Header
from pages.careers import Careers
from pages.footer import Footer
from enums.policies import Policies
from pages.body import Body
from pages.contact import Contact
from pages.about import About


class TaskTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver: webdriver = Drivers.get_driver(Browsers.firefox)

    def test_task_title(self) -> None:
        expected_title: str = "EPAM | Software Engineering & Product Development Services"
        self.assertIn(expected_title, self.driver.title)

    def test_color_mode_button(self) -> None:
        page: Header = Header(self.driver)
        self.assertTrue(page.is_color_mode_selected('dark-mode'))
        page.click_on_color_mode_button()
        self.assertTrue(page.is_color_mode_selected('light-mode'))

    def test_change_locale(self) -> None:
        page: Header = Header(self.driver)
        self.assertIn("EN", page.get_current_locale())
        page.change_locale_to_ua()

        new_page: Careers = Careers(self.driver)
        self.assertIn("UA", new_page.get_current_locale())

    def test_check_policies_list(self) -> None:
        page_footer: Footer = Footer(self.driver)
        page_footer.scroll_the_page_down()
        list_policies = page_footer.extract_policies_list()
        assert (list_policies == Policies.list(), 'Policies list is not the same')

    def test_check_our_location_list(self) -> None:
        page_body: Body = Body(self.driver)
        page_body.get_our_location()
        self.assertIn("AMERICAS", page_body.get_our_location())
        self.assertIn("EMEA", page_body.get_our_location())
        self.assertIn("APAC", page_body.get_our_location())

    def test_check_switching_location(self) -> None:
        page_body: Body = Body(self.driver)
        page_body.click_location('AMERICAS')
        self.assertIn("active", page_body.check_selected_location('AMERICAS'))
        page_body.click_location('EMEA')
        self.assertIn("active", page_body.check_selected_location('EMEA'))
        page_body.click_location('APAC')
        self.assertIn("active", page_body.check_selected_location('APAC'))

    def test_search_function(self) -> None:
        page: Header = Header(self.driver)
        page.click_search()
        page.input_into_search_form()
        page.click_find_button()
        expected_url: str = "https://www.epam.com/search?q=AI"
        self.assertIn(expected_url, self.driver.current_url)

    def test_contact_required_field(self) -> None:
        page_contact: Contact = Contact(self.driver)
        self.driver.get("https://www.epam.com/about/who-we-are/contact")
        page_contact.click_submit_button()
        expected_required_fields = ['Select the Reason for Your Inquiry*', 'First Name*', 'Last Name*', 'Email*', 'Phone*', 'Location*', 'How did you hear about EPAM?*', 'I consent to EPAM Systems, Inc. ("EPAM") processing my personal information as set out in the Privacy Policy and Cookie Policy and that, given the global nature of EPAM\'s business, such processing may take place outside of my home jurisdiction.\n*']
        assert expected_required_fields == page_contact.get_required_fields()

    def test_check_logo(self) -> None:
        page_about: About = About(self.driver)
        self.driver.get("https://www.epam.com/about")
        page_about.click_company_logo()
        expected_url: str = "https://www.epam.com/"
        self.assertIn(expected_url, self.driver.current_url)

    def test_download_report(self):
        page_about: About = About(self.driver)
        self.driver.get("https://www.epam.com/about")
        page_about.click_download_button()
        assert page_about.is_file_downloaded("\\Users\\Downloads","EPAM_Corpotrate_Overview_2023.pdf"), "Failed to download the report"




    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
