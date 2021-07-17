from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class SearchPageLocators:

    ACCEPT_REGION_BTN: tuple = (By.CSS_SELECTOR, 'a[data-action="changeCity"]')

    PRODUCT_CARD: tuple = (By.CSS_SELECTOR, 'div.cc-item--fields')
    PRODUCT_TITLE: tuple = (By.CSS_SELECTOR, 'a.cc-item--title')
    PRODUCT_CARD_RECIPE_STRICT: tuple = (By.CSS_SELECTOR, 'button.recipe__tooltip')
    PRODUCT_DETAIL_CARD_TITLE: tuple = (By.CSS_SELECTOR, 'div.sec-item > h1')

    CLOSE_NOTIFICATION_BTN: tuple = (By.CSS_SELECTOR, 'button.notification__close')

    SEARCH_INPUT: tuple = (By.CSS_SELECTOR, 'input#search')
    SEARCH_TIPS: tuple = (By.CSS_SELECTOR, 'div.searchbar__tips')
    GO_SEARCH_BTN: tuple = (By.CSS_SELECTOR, 'button.searchbar__button')
    SEARCH_COUNTS: tuple = (By.CSS_SELECTOR, 'div.search-count')