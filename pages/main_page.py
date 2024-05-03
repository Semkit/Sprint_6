from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
def question_locator(number):
    return f'*MainPageLocators.QUESTION_{number}'


def answer_locator(number):
    return f'MainPageLocators.ANSWER_{number}'


class MainPage(BasePage):
    @allure.step('Кликаем по кнопке "Заказать" вверху')
    def click_order_button(self):
        self.click(*MainPageLocators.UPPER_ORDER_BUTTON)

    @allure.step('Кликаем по лого Самоката')
    def click_logo_scooter(self):
        self.click(*BasePageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем по лого Яндекса')
    def click_logo_yandex(self):
        self.click(*BasePageLocators.YANDEX_LOGO)

    @allure.step('Ожидаем пока изменится страница на Дзен')
    def wait_for_url_changes_dzen(self):
        self.wait_url_changes(URL.DZEN_PAGE)

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_is('Дзен')

    @allure.step('Кликаем на кнопка Зказать для перехода на другу страницу и клик на лого самоката, чтобы вернуться обратно домой')
    def click_order_and_click_logo_scooter_back(self):
        self.click_order_button()
        self.click_logo_scooter()

    @allure.step('Ищем вопросы, раскрываем их и фиксируем ответы')
    def click_and_get_answer(self, number):
        self.wait_and_find_element(question_locator(number)).click()
        return self.wait_and_find_element(answer_locator(number))

    @allure.step('Скроллим до нужного элемента')
    def scroll_to_element(self):
        self.scroll(*MainPageLocators.QUESTION_1)

    @allure.step('Ожидаем появления элемента, до которого скроллили')
    def wait_for_element_appears(self):
        self.wait_and_find_element(*MainPageLocators.QUESTION_1)