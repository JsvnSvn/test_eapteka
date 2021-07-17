from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class NotificationLocators:

    CLOSE_NOTIFICATION_BTN: tuple = (By.CSS_SELECTOR, 'button.notification__close')