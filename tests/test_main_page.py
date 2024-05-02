import allure
import data
from pages.main_page import MainPage
from conftest import driver
from pages.order_page import OrderPage

class TestMainPageQuestions:
    def test_question(self, driver):
        MainPage.click_on_question()

    def test_transition_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        assert 'dzen' in driver.current_url

    def test_transition_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_scooter_logo()

class TestLogoPage:

    @allure.title('Проверка возврата на домашнюю страницу по клику на логотип Самоката')
    @allure.description('Кликаем на кнопку "Принять куки", далее на кнопку "Заказать", чтобы уйти с домашней страницы, а потом возвращаемся на нее обратно')
    def test_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_pop_up()
        order_page.click_on_scooter_logo()

        assert 'scooter' in order_page.get_current_url()

    @allure.title('Проверка редиректа на сайт Дзена по клику на лого Яндекса')
    @allure.description('Кликаем на кнопку "Принять куки", далее клик на лого Яндекса и проверяем, что произошел редирект на страничку Дзена')
    def test_logo_yandex(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_cookie()
        logo_page.click_logo_yandex()
        logo_page.wait_for_url_changes_dzen()
        logo_page.switch_driver()
        logo_page.wait_for_title()
        assert 'dzen.ru' in logo_page.get_current_url()


