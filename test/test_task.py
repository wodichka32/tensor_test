import allure
from  base.base_test import  BaseTest
from  pytest import  mark



@mark.All
@allure.feature("Site Functionality")
class TaskTest(BaseTest):

    @mark.test1
    @allure.title("Photo size")
    @allure.severity("Critical")
    def test_task_one(self):
        self.sbis_main_page.open()
        self.sbis_main_page.open_contact_page()
        self.contacts_page.is_opened()
        self.contacts_page.click_tensor_logo()
        self.contacts_page.switch_to_new_window()
        self.tensor_main_page.find_people_block()
        self.tensor_about_page.is_opened()
        self.tensor_about_page.cheak_photo_size_work_block()

    @mark.test2
    @allure.title("Region change")
    @allure.severity("Critical")
    def test_task_two(self):
        self.sbis_main_page.open()
        self.sbis_main_page.open_contact_page()
        self.contacts_page.cheak_region_data()
        self.contacts_page.change_region("Камчатский край")
        self.contacts_page.cheak_region_data("Камчатский край")


