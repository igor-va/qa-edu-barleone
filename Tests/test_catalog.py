import pytest
import allure
from Pages.CatalogPage import CatalogPage
from Configurations.TestData import TestData
from Info.Titles import Titles
from Info.Texts import Texts


@allure.feature("Page 'Catalog'")
class TestCatalog:

    @allure.story("Add product to 'Cart'")
    @allure.description("Check add product 'Costume' to 'Cart'")
    def test_add_cart_costume(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL_CATALOG)
        catalog_page = CatalogPage(self.driver)
        catalog_page.click_item_catalog_costume()
        catalog_page.click_add_cart_costume()
        page_text = catalog_page.page_text_element()
        assert Texts.cart_add in page_text, Texts.error_word

    @allure.story("Add product to 'Cart'")
    @allure.description("Check add product 'Shirt' to 'Cart'")
    def test_add_cart_shirt(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL_CATALOG)
        catalog_page = CatalogPage(self.driver)
        catalog_page.click_item_catalog_shirt()
        catalog_page.click_add_cart_shirt()
        page_text = catalog_page.page_text_element()
        assert Texts.cart_add in page_text, Texts.error_word

    @allure.story("Add product to 'Cart'")
    @allure.description("Check add product 'Trousers' to 'Cart'")
    def test_add_cart_trousers(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL_CATALOG)
        catalog_page = CatalogPage(self.driver)
        catalog_page.click_item_catalog_trousers()
        catalog_page.click_add_cart_trousers()
        page_text = catalog_page.page_text_element()
        assert Texts.cart_add in page_text, Texts.error_word
