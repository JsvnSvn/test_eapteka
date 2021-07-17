import allure
from loguru import logger

from fragments.region_fragments.region_locators import RegionLocators
from fragments.notification_fragments.notification_steps import NotificationSteps


class RegionSteps(NotificationSteps):

    region_locators = RegionLocators()

    @allure.step('Принятие региона')
    def accept_region(self):
        self.is_element_present(self.region_locators.ACCEPT_REGION_BTN)
        self.find_element(*self.region_locators.ACCEPT_REGION_BTN).click()
        assert self.not_is_element_present(*self.region_locators.ACCEPT_REGION_BTN)
        logger.info('accept region')
