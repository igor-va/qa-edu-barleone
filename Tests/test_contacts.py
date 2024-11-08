import pytest
from Pages.ContactsPage import ContactsPage
from Configurations.TestData import TestData
from Info.Texts import Texts


class TestCommon:

    # @pytest.mark.skip
    def test_go_contacts_msk(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL_CONTACTS)
        contacts_page = ContactsPage(self.driver)
        contacts_page.click_item_contacts_msk()
        page_text = contacts_page.page_text_element()
        assert Texts.msk_word in page_text, Texts.error_word

#     @pytest.mark.skip
    def test_go_contacts_spb(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL_CONTACTS)
        contacts_page = ContactsPage(self.driver)
        contacts_page.click_item_contacts_spb()
        page_text = contacts_page.page_text_element()
        assert Texts.spb_word in page_text, Texts.error_word

#     @pytest.mark.skip
    def test_go_contacts_nn(self, fixture_setup):
        self.driver = fixture_setup
        self.driver.get(TestData.URL_CONTACTS)
        contacts_page = ContactsPage(self.driver)
        contacts_page.click_item_contacts_nn()
        page_text = contacts_page.page_text_element()
        assert Texts.nn_word in page_text, Texts.error_word
