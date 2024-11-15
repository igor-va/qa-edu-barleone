import os
from .BasePage import BasePage
from Locators.CatalogLocators import CatalogLocators
from Info.Prices import Prices


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_catalog_costume(self):
        BasePage.action_click(self, element=CatalogLocators.loc_link_catalog_costume)

    def click_item_catalog_shirt(self):
        BasePage.action_click(self, element=CatalogLocators.loc_link_catalog_shirt)

    def click_item_catalog_trousers(self):
        BasePage.action_click(self, element=CatalogLocators.loc_link_catalog_trousers)

    def click_add_cart_costume(self):
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_city_msc)
        BasePage.action_text_clear(self, element=CatalogLocators.loc_xpath_price_min)
        BasePage.action_text_type(self, element=CatalogLocators.loc_xpath_price_min, text=Prices.costume_price_min)
        BasePage.action_text_clear(self, element=CatalogLocators.loc_xpath_price_max)
        BasePage.action_text_type(self, element=CatalogLocators.loc_xpath_price_max, text=Prices.costume_price_max)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_costume_size_catalog)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_sort)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_sort_min)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_costume_model_min)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_costume_size_cart)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_cart_add)

    def click_add_cart_shirt(self):
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_city_spb)
        BasePage.action_text_clear(self, element=CatalogLocators.loc_xpath_price_min)
        BasePage.action_text_type(self, element=CatalogLocators.loc_xpath_price_min, text=Prices.shirt_price_min)
        BasePage.action_text_clear(self, element=CatalogLocators.loc_xpath_price_max)
        BasePage.action_text_type(self, element=CatalogLocators.loc_xpath_price_max, text=Prices.shirt_price_max)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_shirt_size_catalog)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_sort)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_sort_max)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_costume_model_min)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_shirt_size_cart)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_cart_add)

    def click_add_cart_trousers(self):
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_city_nn)
        BasePage.action_text_clear(self, element=CatalogLocators.loc_xpath_price_min)
        BasePage.action_text_type(self, element=CatalogLocators.loc_xpath_price_min, text=Prices.trousers_price_min)
        BasePage.action_text_clear(self, element=CatalogLocators.loc_xpath_price_max)
        BasePage.action_text_type(self, element=CatalogLocators.loc_xpath_price_max, text=Prices.trousers_price_max)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_trousers_size_catalog)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_sort)
        BasePage.wait_load_element(self, element=CatalogLocators.loc_xpath_obscure_catalog)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_sort_popular)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_costume_model_min)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_trousers_size_cart)
        BasePage.action_click(self, element=CatalogLocators.loc_xpath_cart_add)

    def page_text_element(self):
        return BasePage.get_text_element(self, element=CatalogLocators.loc_xpath_text_add_cart)
