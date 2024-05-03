import allure

from pages.main_page import MainPage
from conftest import driver

class TestMainPageQuestions:
    # def test_question(self, driver):
    #     MainPage.click_and_get_answer()

    def test_transition_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        assert 'dzen' in driver.current_url

    def test_transition_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_scooter()

    @allure.title('Проверка возврата на домашнюю страницу по клику на логотип Самоката')
    @allure.description('Кликаем на кнопку "Принять куки", далее на кнопку "Заказать", чтобы уйти с домашней страницы, а потом возвращаемся на нее обратно')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_cookie()
        main_page.click_logo_scooter()

        assert 'scooter' in main_page.get_current_url()




