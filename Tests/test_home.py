import pytest
import allure
from Pages.HomePage import HomePage
from Configurations.TestData import TestData
from Info.Titles import Titles


@allure.feature("Page 'Home'")
class TestHome:

    @pytest.mark.smoke
    @allure.story("Right Sidebar")
    @allure.description("Check open page 'Catalog'")
    def test_go_rightbar_catalog(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_catalog()
        page_title = home_page.get_page_title()
        assert Titles.catalog_title in page_title, Titles.error_title

    @allure.story("Right Sidebar")
    @allure.description("Check open page 'Wishlist'")
    def test_go_rightbar_wishlist(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_wishlist()
        page_title = home_page.get_page_title()
        assert Titles.wishlist_title in page_title, Titles.error_title

    @allure.story("Right Sidebar")
    @allure.description("Check open page 'Sale'")
    def test_go_rightbar_sale(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_sale()
        page_title = home_page.get_page_title()
        assert Titles.sale_title in page_title, Titles.error_title

    @allure.story("Right Sidebar")
    @allure.description("Check open page 'Authorization'")
    def test_go_rightbar_authorization(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_authorization()
        page_title = home_page.get_page_title()
        assert Titles.authorization_title in page_title, Titles.error_title

    @allure.story("Right Sidebar")
    @allure.description("Check open page 'Cart'")
    def test_go_rightbar_cart(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_cart()
        page_title = home_page.get_page_title()
        assert Titles.cart_title in page_title, Titles.error_title
