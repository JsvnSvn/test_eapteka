import allure
from loguru import logger

from fragments.base_steps import BaseSteps
from fragments.notification_fragments.notification_locators import NotificationLocators


class NotificationSteps(BaseSteps):

    notification_locators = NotificationLocators()

    @allure.step('Закрытие окна с предложением скачать приложение')
    def close_notification(self):
        self.is_element_present(self.notification_locators.CLOSE_NOTIFICATION_BTN)
        self.find_element(*self.notification_locators.CLOSE_NOTIFICATION_BTN).click()
        assert self.not_is_element_present(*self.notification_locators.CLOSE_NOTIFICATION_BTN)
        logger.info('close notification')