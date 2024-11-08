from selenium.webdriver.common.by import By


class CommonLocators:
    loc_tag_footer = (By.TAG_NAME, "footer")

    loc_link_sign_in = (By.LINK_TEXT, "Sign In")
    loc_link_catalog = (By.LINK_TEXT, "Каталог")
    loc_link_contacts = (By.LINK_TEXT, "Контакты")
    loc_link_delivery = (By.LINK_TEXT, "Доставка и оплата")
    loc_link_return = (By.LINK_TEXT, "Возврат товара")
    loc_link_guarantee = (By.LINK_TEXT, "Гарантия")
    loc_link_puboffer = (By.LINK_TEXT, "Публичная оферта")
    loc_link_sitemap = (By.LINK_TEXT, "Карта сайта")
    loc_link_sale = (By.LINK_TEXT, "Акции")
    loc_link_account = (By.LINK_TEXT, "Личный кабинет")
    loc_link_orders = (By.LINK_TEXT, "История заказов")
    loc_link_wishlist = (By.LINK_TEXT, "Закладки")

    loc_xpath_header_wishlist = (By.XPATH, "//div[@class='control-panel header__panel']//a[@href='/wishlist/']")
    loc_xpath_header_sale = (By.XPATH, "//div[@class='control-panel header__panel']//a[@href='/sale/']")
    loc_xpath_header_authorization = (By.XPATH, "//div[@class='control-panel header__panel']//a[@href='/authorization/']")
    loc_xpath_header_cart = (By.XPATH, "//div[@class='control-panel header__panel']//a[@href='https://barleone.ru/cart/']")
