from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class DetailProductLocators:

    PRODUCT_CARD: tuple = (By.CSS_SELECTOR, 'div.cc-item--fields')
    PRODUCT_TITLE: tuple = (By.CSS_SELECTOR, 'a.cc-item--title')
    PRODUCT_CARD_RECIPE_STRICT: tuple = (By.CSS_SELECTOR, 'button.recipe__tooltip')
    PRODUCT_DETAIL_CARD_TITLE: tuple = (By.CSS_SELECTOR, 'div.sec-item > h1')
