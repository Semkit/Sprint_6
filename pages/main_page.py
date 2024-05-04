from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators

from selenium.webdriver.common.by import By
@allure.step('Вытаскиваем по номеру и возвращаем локаторы вопросов')
def question_locator(number):
    return (By.ID, f"accordion__heading-{number}")

@allure.step('Вытаскиваем по номеру и возвращаем локаторы ответов')
def answer_locator(number):
    return (By.ID, f"accordion__panel-{number}")


class MainPage(BasePage):

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_is('Дзен')

    @allure.step('Ищем вопросы, раскрываем их и фиксируем ответы')
    def click_and_get_answer(self, number):
        self.wait_and_find_element(question_locator(number)).click()
        return self.wait_and_find_element(answer_locator(number))

    @allure.step('Скроллим до нужного элемента')
    def scroll_to_element(self):
        self.scroll(MainPageLocators.QUESTION_1)

    @allure.step('Ожидаем появления элемента, до которого скроллили')
    def wait_for_element_appears(self):
        self.wait_and_find_element(MainPageLocators.QUESTION_1)
