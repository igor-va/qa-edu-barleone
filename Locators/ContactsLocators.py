from selenium.webdriver.common.by import By


class ContactsLocators:
    loc_link_contacts_msk = (By.LINK_TEXT, "МОСКВА")
    loc_link_contacts_spb = (By.LINK_TEXT, "САНКТ-ПЕТЕРБУРГ")
    loc_link_contacts_nn = (By.LINK_TEXT, "НИЖНИЙ НОВГОРОД")

    loc_xpath_text = (By.XPATH, "//div[@class='title contacts-main-title']")
