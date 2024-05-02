import allure
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
import locators.main_page_locators

class OrderPage(BasePage):

    @allure.step('Заполняем поле имя')
    def set_name_input(self, name):
        name_input = self.wait_and_find_element(*OrderPageLocators.NAME_INPUT_FIELD)
        name_input.send_keys(name)

    @allure.step('Заполняем поле фамилия')
    def set_second_name_input(self, second_name):
        second_name_input = self.wait_and_find_element(*OrderPageLocators.SECOND_NAME_INPUT_FIELD)
        second_name_input.send_keys(second_name)

    @allure.step('Заполняем поле адрес')
    def set_second_name__input(self, adress):
        adress_input = self.wait_and_find_element(*OrderPageLocators.ADRESS_INPUT_FIELD)
        adress_input.send_keys(adress)

    @allure.step('Заполняем поле адрес')
    def set_second_name_input(self, adress):
        adress_input = self.wait_and_find_element(*OrderPageLocators.ADRESS_INPUT_FIELD)
        adress_input.send_keys(adress)

    @allure.step('Находим поле Метро')
    def metro_field(self):
        self.wait_and_find_element(*OrderPageLocators.METRO_STATION_INPUT_FILED)