from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class RegionLocators:

    ACCEPT_REGION_BTN: tuple = (By.CSS_SELECTOR, 'a[data-action="changeCity"]')
