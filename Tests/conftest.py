import pytest
from selenium import webdriver


@pytest.fixture(params=['Chrome'], scope="class")
def fixture_setup(request):
    driver = None
    if request.param == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif request.param == "Firefox":
        driver = webdriver.Firefox()
    return driver
