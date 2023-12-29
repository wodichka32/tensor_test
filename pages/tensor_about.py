import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By

class TensorAbout(BasePage):
    PAGE_URL = Links.TENSOR_ABOUT
    BLOCK_WORK = ("xpath", r"//*[contains(text(), 'Работаем')]")

    @allure.feature("Cheak photo size")
    def cheak_photo_size_work_block(self):
        block = self.browser.find_element(*self.BLOCK_WORK)
        block = block.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
        photos = block.find_elements(By.TAG_NAME, "img")

        pattern = None
        for photo in photos:
            if not pattern:
                pattern = photo.size
            else:
                assert photo.size == pattern, "Photos size don't match"
