import  allure
from base.base_page import BasePage
from config.contact import contacts
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ContactPage(BasePage):
    PAGE_URL = Links.MY_CONTACT_PAGE
    TENSOR_LOGO = ("xpath", r"//a[@class='sbisru-Contacts__logo-tensor mb-12']")

    REGION_CHOOSE = ("xpath", r"//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']")
    FIRST_PARTNER = ("xpath", r"//div[@class='sbisru-Contacts-List__col-1']/div")

    @allure.step("Click on Tensor logo")
    def click_tensor_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_LOGO)).click()

    @allure.feature("Get region info")
    def cheak_region_data(self, region="Свердловская обл."):
        self.wait.until(EC.url_to_be(url=contacts[region]["URL"]))
        cur_url = self.get_url()
        cur_title = self.get_title()
        cur_region = self.browser.find_element(*self.REGION_CHOOSE).text
        cur_first_partner = self.browser.find_element(*self.FIRST_PARTNER).text


        assert cur_url == contacts[region]["URL"], "URL don't match"
        assert cur_title == contacts[region]["TITLE"], "TITLE don't match"
        assert cur_region == contacts[region]["REGION"], "Region don't match"
        assert cur_first_partner == contacts[region]["PARTNER"], "Partner don't match"

    @allure.step("Change region")
    def change_region(self, reg):
        self.browser.find_element(*self.REGION_CHOOSE).click()
        region_pass = ("xpath", fr"//span[@title='{reg}']")
        self.wait.until(EC.element_to_be_clickable(region_pass)).click()
