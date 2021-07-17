from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from loguru import logger


class BaseSteps:
    def __init__(self, browser: webdriver, url: str = 'https://www.eapteka.ru'):
        self.browser: webdriver = browser
        self.url: str = url

    @allure.step('Открытие браузера')
    def open(self):
        try:
            self.browser.get(self.url)
            logger.info(f'\nuser-agent: {self.browser.execute_script("return navigator.userAgent;")}')
        except TimeoutException:
            self.browser.get(self.url)

    def is_element_present(self, locator):
        """Проверка, что элемент видим"""
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
        except NoSuchElementException:
            return False
        return True

    def not_is_element_present(self, how, what):
        """Проверка, что элемента нет"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    @staticmethod
    def get_element_attribute(how: WebElement, what: str):
        """Получение значение атрибута элемента: например значение value у чекбокса"""
        return how.get_attribute(what)

    @staticmethod
    def value_of_css_property(element: WebElement, css_property: str) -> str:
        """получение значения css-свойства элемента на странице"""
        logger.info(element.value_of_css_property(css_property))
        return element.value_of_css_property(css_property)

    def find_element(self, how: str, what: str) -> WebElement:
        """поиск элемента на странице"""
        return self.browser.find_element(how, what)

    def find_elements(self, how, what) -> List[WebElement]:
        """поиск элементов на странице"""
        elements_list: List[WebElement] = self.browser.find_elements(how, what)
        logger.info(f'Число найденных элементов: {len(elements_list)}')
        return elements_list

    def wait_element_clickable(self, locator: tuple) -> WebElement:
        """ожидание, пока элемент станет кликабельным"""
        element: WebElement = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        return element

    @allure.step('Рефреш страницы')
    def refresh_page(self):
        self.browser.refresh()

    @allure.step('Заполнение инпута')
    def fill_input(self, element: WebElement, value: str):
        self.clear_input(element)
        element.send_keys(value)
        logger.info('fill input')

    def scroll_page(self):
        """прокрутка страницы к футеру"""
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    @allure.step('Очистка поля ввода')
    def clear_input(self, element: WebElement):
        element.clear()
        logger.info('clear input')


