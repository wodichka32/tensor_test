import allure
from  allure_commons.types import  AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)


    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.browser.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def switch_to_new_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def get_url(self):
        with allure.step(f"Cur page URL is {self.browser.current_url}"):
            return self.browser.current_url

    def get_title(self):
        with allure.step(f"Cur page Title is {self.browser.title}"):
            return self.browser.title
