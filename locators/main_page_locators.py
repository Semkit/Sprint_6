from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    QUESTION_1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
