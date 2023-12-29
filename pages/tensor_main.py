import allure
from base.base_page import BasePage
from config.links import Links
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TensorMain(BasePage):
    PAGE_URL = Links.TENSOR_MAIN


    BLOCK_PEOPLE = ("xpath", r"//*[contains(text(), 'Сила в людях')]")
    BLOCK_PEOPLE_ABOUT  = ("xpath",r"//a[@href = '/about']")

    @allure.step("Find block info")
    def find_people_block(self):
        try:
            bloack = self.browser.find_element(*self.BLOCK_PEOPLE)
            bloack = bloack.find_element(By.XPATH,"..")
            bloack.find_element(*self.BLOCK_PEOPLE_ABOUT).click()
        except NoSuchElementException:
            print("The paragraph element does not exist.")