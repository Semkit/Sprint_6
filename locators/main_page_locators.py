from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    QUESTION_1 = (By.ID, "//div[@id='accordion__heading-0']")
    ANSWER_1 = (By.ID, "//div[@id='accordion__panel-0']")

    QUESTION_2 = (By.ID, "//div[@id='accordion__heading-1']")
    ANSWER_2 = (By.ID, "//div[@id='accordion__panel-1']")

    QUESTION_3 = (By.ID, "//div[@id='accordion__heading-2']")
    ANSWER_3 = (By.ID, "//div[@id='accordion__panel-2']")

    QUESTION_4 = (By.ID, "//div[@id='accordion__heading-3']")
    ANSWER_4 = (By.ID, "//div[@id='accordion__panel-3']")

    QUESTION_5 = (By.ID, "//div[@id='accordion__heading-4']")
    ANSWER_5 = (By.ID, "//div[@id='accordion__panel-4']")

    QUESTION_6 = (By.ID, "//div[@id='accordion__heading-5']")
    ANSWER_6 = (By.ID, "//div[@id='accordion__panel-5']")

    QUESTION_7 = (By.ID, "//div[@id='accordion__heading-6']")
    ANSWER_7 = (By.ID, "//div[@id='accordion__panel-6']")

    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
