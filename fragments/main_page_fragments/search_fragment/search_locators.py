from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class SearchLocators:

    SEARCH_INPUT: tuple = (By.CSS_SELECTOR, 'input#search')
    SEARCH_TIPS: tuple = (By.CSS_SELECTOR, 'div.searchbar__tips')
    GO_SEARCH_BTN: tuple = (By.CSS_SELECTOR, 'button.searchbar__button')
    SEARCH_COUNTS: tuple = (By.CSS_SELECTOR, 'div.search-count')
