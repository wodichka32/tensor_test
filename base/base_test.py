import pytest
from pages.contacts import ContactPage
from pages.sbis_main import SbisMain
from pages.tensor_main import TensorMain
from pages.tensor_about import TensorAbout


class BaseTest:
    contacts_page: ContactPage
    sbis_main_page: SbisMain
    tensor_main_page: TensorMain
    tensor_about_page: TensorAbout

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.contacts_page = ContactPage(browser)
        request.cls.sbis_main_page = SbisMain(browser)
        request.cls.tensor_main_page = TensorMain(browser)
        request.cls.tensor_about_page = TensorAbout(browser)
