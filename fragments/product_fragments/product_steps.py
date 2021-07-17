from typing import List
from random import choice
from loguru import logger
import allure

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from fragments.region_fragments.region_steps import RegionSteps
from fragments.product_fragments.product_locators import DetailProductLocators
from fragments.notification_fragments.notification_steps import NotificationSteps


class ProductSteps(RegionSteps):

    detail_product_locators = DetailProductLocators()

    @allure.step('Переход на детальную страницу товара')
    def go_to_detail_product_recipe_strict(self):
        self.is_element_present(self.detail_product_locators.PRODUCT_CARD)
        all_product_list: List[WebElement] = self.find_elements(*self.detail_product_locators.PRODUCT_CARD)
        recipe_strict_list: List[WebElement] = []

        for i in all_product_list:
            try:
                i.find_element(*self.detail_product_locators.PRODUCT_CARD_RECIPE_STRICT)
                recipe_strict_list.append(i)
            except NoSuchElementException:
                pass

        product: WebElement = choice(recipe_strict_list)
        product_title: WebElement = product.find_element(*self.detail_product_locators.PRODUCT_TITLE)
        product_title_text: str = product_title.text
        product_title.click()
        self.is_element_present(self.detail_product_locators.PRODUCT_DETAIL_CARD_TITLE)
        product_detail_title_text: str = self.find_element(*self.detail_product_locators.PRODUCT_DETAIL_CARD_TITLE).text
        assert product_title_text in product_detail_title_text
        logger.info('go to detail product with recipe strict')
