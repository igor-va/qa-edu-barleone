import pytest
from Pages.CommonPage import CommonPage
from Configurations.TestData import TestData
from Info.Titles import Titles


class TestCommon:

    # @pytest.mark.skip
    def test_go_header_catalog(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_header_catalog()
        page_title = common_page.get_page_title()
        assert Titles.catalog_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_header_contacts(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_header_contacts()
        page_title = common_page.get_page_title()
        assert Titles.contacts_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_header_wishlist(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_header_wishlist()
        page_title = common_page.get_page_title()
        assert Titles.wishlist_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_header_sale(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_header_sale()
        page_title = common_page.get_page_title()
        assert Titles.sale_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_header_authorization(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_header_authorization()
        page_title = common_page.get_page_title()
        assert Titles.authorization_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_header_cart(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_header_cart()
        page_title = common_page.get_page_title()
        assert Titles.cart_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_delivery(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_delivery()
        page_title = common_page.get_page_title()
        assert Titles.delivery_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_return(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_return()
        page_title = common_page.get_page_title()
        assert Titles.return_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_guarantee(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_guarantee()
        page_title = common_page.get_page_title()
        assert Titles.guarantee_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_puboffer(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_puboffer()
        page_title = common_page.get_page_title()
        assert Titles.puboffer_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_contacts(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_contacts()
        page_title = common_page.get_page_title()
        assert Titles.contacts_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_sitemap(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_sitemap()
        page_title = common_page.get_page_title()
        assert Titles.sitemap_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_sale(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_sale()
        page_title = common_page.get_page_title()
        assert Titles.sale_title in page_title, Titles.error_title

#     @pytest.mark.skip
    def test_go_footer_account(self, fixture_setup):
        """Add login fixture"""
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_account()
        page_title = common_page.get_page_title()
        assert Titles.account_title in page_title, Titles.error_title

    @pytest.mark.skip
    def test_go_footer_account_orders(self, fixture_setup):
        pass

#     @pytest.mark.skip
    def test_go_footer_wishlist(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        common_page = CommonPage(self.driver)
        common_page.click_item_footer_wishlist()
        page_title = common_page.get_page_title()
        assert Titles.wishlist_title in page_title, Titles.error_title
