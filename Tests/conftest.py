import pytest
from selenium import webdriver


@pytest.fixture(params=['Firefox'], scope="class")
def fixture_setup(request):
    driver = None
    if request.param == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "Firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(params=['Chrome'], scope="class")
# def fixture_setup(request):
#     driver = None
#     if request.param == "Chrome":
#         chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_argument("--start-maximized")
#         # chrome_options.add_argument("--headless")
#         chrome_options.add_argument('--ignore-ssl-errors=yes')
#         chrome_options.add_argument('--ignore-certificate-errors')
#         driver = webdriver.Remote(
#             command_executor='http://localhost:4444/wd/hub',
#             options=chrome_options
#         )
#     elif request.param == "Firefox":
#         firefox_options = webdriver.ChromeOptions()
#         firefox_options.add_argument('--ignore-ssl-errors=yes')
#         firefox_options.add_argument('--ignore-certificate-errors')
#         driver = webdriver.Remote(
#             command_executor='http://localhost:4444/wd/hub',
#             options=firefox_options
#         )
#     return driver
