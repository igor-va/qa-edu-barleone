import os
from selenium.webdriver.common.by import By


class CatalogLocators:
    loc_link_catalog_costume = (By.LINK_TEXT, "КОСТЮМЫ")

    loc_xpath_city = (By.XPATH, "//*[@id='catalog-filter']/div[2]/div[1]/div[1]/label[2]/text()")

    loc_xpath_price_min = (By.XPATH, "//div[@class='sidebar']//input[@name='min_price']")
    loc_xpath_price_max = (By.XPATH, "//div[@class='sidebar']//input[@name='max_price']")
    loc_xpath_costume_model = (By.XPATH, "//a[contains(text(), 'К476')]")
    loc_xpath_costume_size_catalog = (By.XPATH, "//div[@class='sidebar']//*[text()='56']")
    loc_xpath_sort = (By.XPATH, "//div[@class='sidebar']//div[@id='catalog-filter-sort-select']")
    loc_xpath_sort_min = (By.XPATH, "//div[@class='sidebar']//*[text()=' Сначала дешевле ']")

    loc_xpath_costume_size_cart = (By.XPATH, "//span[text()='56']")
    loc_xpath_cart_add = (By.XPATH, "//span[text()=' Добавить в корзину ']")

    loc_xpath_text_add_cart = (By.XPATH, "//div[contains(text(), 'Вы отложили')]")




