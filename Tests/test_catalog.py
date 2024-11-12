import pytest
import allure
from Pages.CatalogPage import CatalogPage
from Configurations.TestData import TestData
from Info.Titles import Titles
from Info.Texts import Texts


@allure.feature("Page 'Catalog'")
class TestCatalog:

    @pytest.mark.smoke
    @allure.story("Section page 'Catalog'")
    @allure.description("Check open page 'Catalog'")
    def test_go_catalog_costume(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL_CATALOG)
        catalog_page = CatalogPage(self.driver)
        catalog_page.click_item_catalog_costume()
        page_title = catalog_page.get_page_title()
        assert Titles.catalog_costume in page_title, Titles.error_title

    @pytest.mark.temp
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
