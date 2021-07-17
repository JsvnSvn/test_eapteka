from random import choice
from typing import List

import allure
from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from pages.base_steps import BaseSteps
from pages.search_page.search_page_locators import SearchPageLocators


class SearchPageSteps(BaseSteps):

    locators = SearchPageLocators()

    @allure.step('Закрытие окна с предложением скачать приложение')
    def close_notification(self):
        self.is_element_present(self.locators.CLOSE_NOTIFICATION_BTN)
        self.find_element(*self.locators.CLOSE_NOTIFICATION_BTN).click()
        assert self.not_is_element_present(*self.locators.CLOSE_NOTIFICATION_BTN)
        logger.info('close notification')

    @allure.step('Принятие региона')
    def accept_region(self):
        self.is_element_present(self.locators.ACCEPT_REGION_BTN)
        self.find_element(*self.locators.ACCEPT_REGION_BTN).click()
        assert self.not_is_element_present(*self.locators.ACCEPT_REGION_BTN)
        logger.info('accept region')

    @allure.step('Ввод запроса в поисковую строку')
    def fill_search_input(self, value: str):
        self.is_element_present(self.locators.SEARCH_INPUT)
        search_input: WebElement = self.find_element(*self.locators.SEARCH_INPUT)
        self.fill_input(search_input, value)
        search_tips_block: WebElement = self.find_element(*self.locators.SEARCH_TIPS)
        tips_block_style: str = self.get_element_attribute(search_tips_block, 'style')
        assert tips_block_style == 'display: block;'
        logger.info('fill search input')

    @allure.step('ЛКМ по кнопке "Найти"')
    def click_search_btn(self):
        self.is_element_present(self.locators.GO_SEARCH_BTN)
        self.find_element(*self.locators.GO_SEARCH_BTN).click()
        assert self.is_element_present(self.locators.SEARCH_COUNTS)
        logger.info('click search btn')

    @allure.step('Переход на детальную страницу товара')
    def go_to_detail_product_recipe_strict(self):
        self.is_element_present(self.locators.PRODUCT_CARD)
        all_product_list: List[WebElement] = self.find_elements(*self.locators.PRODUCT_CARD)
        recipe_strict_list: List[WebElement] = []

        for i in all_product_list:
            try:
                i.find_element(*self.locators.PRODUCT_CARD_RECIPE_STRICT)
                recipe_strict_list.append(i)
            except NoSuchElementException:
                pass

        product: WebElement = choice(recipe_strict_list)
        product_title: WebElement = product.find_element(*self.locators.PRODUCT_TITLE)
        product_title_text: str = product_title.text
        product_title.click()
        self.is_element_present(self.locators.PRODUCT_DETAIL_CARD_TITLE)
        product_detail_title_text: str = self.find_element(*self.locators.PRODUCT_DETAIL_CARD_TITLE).text
        assert product_title_text in product_detail_title_text
        logger.info('go to detail product with recipe strict')
