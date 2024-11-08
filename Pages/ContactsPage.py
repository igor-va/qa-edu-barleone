import os
from .BasePage import BasePage
from Locators.ContactsLocators import ContactsLocators


class ContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_contacts_msk(self):
        BasePage.action_click(self, element=ContactsLocators.loc_link_contacts_msk)

    def click_item_contacts_spb(self):
        BasePage.action_click(self, element=ContactsLocators.loc_link_contacts_spb)

    def click_item_contacts_nn(self):
        BasePage.action_click(self, element=ContactsLocators.loc_link_contacts_nn)

    def page_text_element(self):
        return BasePage.get_text_element(self, element=ContactsLocators.loc_xpath_text)
