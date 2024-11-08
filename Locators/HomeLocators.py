from selenium.webdriver.common.by import By


class HomeLocators:
    loc_link_rightbar_catalog = (By.LINK_TEXT, "Перейти в каталог")

    loc_xpath_rightbar_wishlist = (By.XPATH, "//div[@class='control-panel catalog-widget__panel']//a[@href='/wishlist/']")
    loc_xpath_rightbar_sale = (By.XPATH, "//div[@class='control-panel catalog-widget__panel']//a[@href='/sale/']")
    loc_xpath_rightbar_authorization = (By.XPATH, "//div[@class='control-panel catalog-widget__panel']//a[@href='/authorization/']")
    loc_xpath_rightbar_cart = (By.XPATH, "//div[@class='control-panel catalog-widget__panel']//a[@href='https://barleone.ru/cart/']")

