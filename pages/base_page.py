from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
import data



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_url_to_change(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))

    def click_on_cookie_pop_up(self):
        self.driver.find_element(self, BasePageLocators.ACCEPT_COOKIE).click()

    def locator_click(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_to_locator(self, locator):
        self.driver.find_element(*locator).execute_script("arguments[0].scrollIntoView();")

    def click_on_yandex_logo(self):
        BasePage.wait_and_find_element(self, BasePageLocators.YANDEX_LOGO)

    def click_on_scooter_logo(self):
        BasePage.wait_and_find_element(self, BasePageLocators.SCOOTER_LOGO)




