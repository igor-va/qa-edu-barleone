import pytest
from Pages.HomePage import HomePage
from Configurations.TestData import TestData
from Info.Titles import Titles


class TestHome:

    # @pytest.mark.skip
    def test_go_rightbar_catalog(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_catalog()
        page_title = home_page.get_page_title()
        assert Titles.catalog_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_rightbar_wishlist(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_wishlist()
        page_title = home_page.get_page_title()
        assert Titles.wishlist_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_rightbar_sale(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_sale()
        page_title = home_page.get_page_title()
        assert Titles.sale_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_rightbar_authorization(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_authorization()
        page_title = home_page.get_page_title()
        assert Titles.authorization_title in page_title, Titles.error_title

    # @pytest.mark.skip
    def test_go_rightbar_cart(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        home_page = HomePage(self.driver)
        home_page.click_item_rightbar_cart()
        page_title = home_page.get_page_title()
        assert Titles.cart_title in page_title, Titles.error_title
