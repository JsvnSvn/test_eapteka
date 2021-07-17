from typing import List

from selenium.webdriver.remote.webelement import WebElement

from fragments.product_fragments.product_steps import ProductSteps
from fragments.main_page_fragments.search_fragment.search_locators import SearchLocators

from loguru import logger
import allure


class SearchSteps(ProductSteps):

    search_locators = SearchLocators()

    @allure.step('Ввод запроса в поисковую строку')
    def fill_search_input(self, value: str):
        self.is_element_present(self.search_locators.SEARCH_INPUT)
        search_input: WebElement = self.find_element(*self.search_locators.SEARCH_INPUT)
        self.fill_input(search_input, value)
        search_tips_block: WebElement = self.find_element(*self.search_locators.SEARCH_TIPS)
        tips_block_style: str = self.get_element_attribute(search_tips_block, 'style')
        assert tips_block_style == 'display: block;'
        logger.info('fill search input')

    @allure.step('ЛКМ по кнопке "Найти"')
    def click_search_btn(self):
        self.is_element_present(self.search_locators.GO_SEARCH_BTN)
        self.find_element(*self.search_locators.GO_SEARCH_BTN).click()
        assert self.is_element_present(self.search_locators.SEARCH_COUNTS)
        logger.info('click search btn')