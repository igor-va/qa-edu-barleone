import os
from .BasePage import BasePage
from Locators.CommonLocators import CommonLocators


class CommonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_header_catalog(self):
        BasePage.action_click(self, element=CommonLocators.loc_link_catalog)

    def click_item_header_contacts(self):
        BasePage.action_click(self, element=CommonLocators.loc_link_contacts)

    def click_item_header_wishlist(self):
        BasePage.action_click(self, element=CommonLocators.loc_xpath_header_wishlist)

    def click_item_header_sale(self):
        BasePage.action_click(self, element=CommonLocators.loc_xpath_header_sale)

    def click_item_header_authorization(self):
        BasePage.action_click(self, element=CommonLocators.loc_xpath_header_authorization)

    def click_item_header_cart(self):
        BasePage.action_click(self, element=CommonLocators.loc_xpath_header_cart)

    def click_item_footer_delivery(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_delivery)

    def click_item_footer_contacts(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_contacts)

    def click_item_footer_return(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_return)

    def click_item_footer_guarantee(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_guarantee)

    def click_item_footer_puboffer(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_puboffer)

    def click_item_footer_sitemap(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_sitemap)

    def click_item_footer_sale(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_sale)

    def click_item_footer_account(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_account)

    def click_item_footer_orders(self):
        pass

    def click_item_footer_wishlist(self):
        BasePage.scroll_to_element_tag(self, element=CommonLocators.loc_tag_footer)
        BasePage.action_click(self, element=CommonLocators.loc_link_wishlist)
