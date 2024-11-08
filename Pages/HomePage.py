from .BasePage import BasePage
from Locators.HomeLocators import HomeLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_rightbar_catalog(self):
        BasePage.action_click(self, element=HomeLocators.loc_link_rightbar_catalog)

    def click_item_rightbar_wishlist(self):
        BasePage.action_click(self, element=HomeLocators.loc_xpath_rightbar_wishlist)

    def click_item_rightbar_sale(self):
        BasePage.action_click(self, element=HomeLocators.loc_xpath_rightbar_sale)

    def click_item_rightbar_authorization(self):
        BasePage.action_click(self, element=HomeLocators.loc_xpath_rightbar_authorization)

    def click_item_rightbar_cart(self):
        BasePage.action_click(self, element=HomeLocators.loc_xpath_rightbar_cart)
