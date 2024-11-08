from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def action_text_clear(self, element):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).clear()

    def action_text_type(self, element, text):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).send_keys(text)

    def action_click(self, element):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).click()

    def get_text_element(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).text

    def element_status_enabled(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).is_enabled()

    def element_status_displayed(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).is_displayed()

    def find_element_tag(self, element):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element))
        ActionChains(self.driver).scroll_to_element(element).perform()

    def get_page_title(self):
        return self.driver.title



