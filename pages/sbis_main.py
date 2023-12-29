import  allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class SbisMain(BasePage):
    PAGE_URL = Links.SBIS_MAIN

    CONTACT_PAGE = ("css selector", "a[href = '/contacts']")

    @allure.step("Open contact page")
    def open_contact_page(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_PAGE)).click()