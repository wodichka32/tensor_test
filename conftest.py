from pytest import fixture
from selenium import webdriver



@fixture(
    scope="function",
    params=[
    (webdriver.Chrome,webdriver.ChromeOptions),
    #(webdriver.Edge,webdriver.EdgeOptions),
    #(webdriver.Firefox,webdriver.FirefoxOptions)
    ])
def browser(request):
    driver = request.param
    options = driver[1]()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    drvr = driver[0](options = options)
    yield drvr
    drvr.quit()
