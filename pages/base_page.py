import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Запрашиваем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключаем драйвер')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Выставляем ожидание до появления элемента с указанным локатором')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Вытягиваем текст из элемента с указанным локатором')
    def find_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Ожидание появления заголовка на странице')
    def wait_for_title_is(self, title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(title))

    @allure.step('Дожидаемся смены URL страницы')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    @allure.step('Скроллим, пока не увидим нужный элемент по локатору')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем на кнопку Принять Куки')
    def cookie_click(self):
        self.click(*BasePageLocators.ACCEPT_COOKIE)

    @allure.step('Нажимаем на кнопку Заказа вверху страницы')
    def order_upper_button_click(self):
        self.click(*BasePageLocators.UPPER_ORDER_BUTTON)

    @allure.step('Нажимаем на кнопку сервиса Самокат вверху страницы')
    def order_upper_button_click(self):
        self.click(*BasePageLocators.SCOOTER_LOGO)

    @allure.step('Нажимаем на кнопку Яндекса вверху страницы')
    def order_upper_button_click(self):
        self.click(*BasePageLocators.YANDEX_LOGO)




