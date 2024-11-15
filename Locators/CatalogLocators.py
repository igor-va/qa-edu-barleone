import os
from selenium.webdriver.common.by import By


class CatalogLocators:
    loc_link_catalog_costume = (By.LINK_TEXT, "КОСТЮМЫ")
    loc_link_catalog_shirt = (By.LINK_TEXT, "РУБАШКИ")
    loc_link_catalog_trousers = (By.LINK_TEXT, "БРЮКИ")

    loc_xpath_city_msc = (By.XPATH, "//div[@class='sidebar']//label[@class='catalog-filter__label'][1]")
    loc_xpath_city_spb = (By.XPATH, "//div[@class='sidebar']//label[@class='catalog-filter__label'][2]")
    loc_xpath_city_nn = (By.XPATH, "//div[@class='sidebar']//label[@class='catalog-filter__label'][3]")

    loc_xpath_price_min = (By.XPATH, "//div[@class='sidebar']//input[@name='min_price']")
    loc_xpath_price_max = (By.XPATH, "//div[@class='sidebar']//input[@name='max_price']")

    loc_xpath_costume_size_catalog = (By.XPATH, "//div[@class='sidebar']//*[text()='56']")
    loc_xpath_shirt_size_catalog = (By.XPATH, "//div[@class='sidebar']//*[text()='XL']")
    loc_xpath_trousers_size_catalog = (By.XPATH, "//div[@class='sidebar']//*[text()='50']")

    loc_xpath_sort = (By.XPATH, "//div[@class='sidebar']//div[@id='catalog-filter-sort-select']")
    loc_xpath_sort_min = (By.XPATH, "//div[@class='sidebar']//*[text()=' Сначала дешевле ']")
    loc_xpath_sort_max = (By.XPATH, "//div[@class='sidebar']//*[text()=' Сначала дороже ']")
    loc_xpath_sort_popular = (By.XPATH, "//div[@class='sidebar']//*[text()=' Сначала популярные ']")

    loc_xpath_costume_model_min = (By.XPATH, "//ul[@class='shop__list']//child::li[1]")

    loc_xpath_costume_size_cart = (By.XPATH, "//span[text()='56']")
    loc_xpath_shirt_size_cart = (By.XPATH, "//span[contains(text(), 'xl')]")
    loc_xpath_trousers_size_cart = (By.XPATH, "//span[text()='50']")
    loc_xpath_cart_add = (By.XPATH, "//span[text()=' Добавить в корзину ']")

    loc_xpath_text_add_cart = (By.XPATH, "//div[contains(text(), 'has been added')]")

    loc_xpath_obscure_catalog = (By.XPATH, "//div[@class='blockUI blockOverlay']")




