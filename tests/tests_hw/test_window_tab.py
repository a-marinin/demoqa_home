from pages.links import LinksPage
import time


def test_managing_new_tabs(browser):
    links_page = LinksPage(browser)

    links_page.visit()
    """ Проверяем элементы на стартовой странице (demoqa.com/links) """
    assert links_page.btn_home.exist()  # Проверяем, что кнопка "Home" существует
    assert links_page.btn_home.get_text() == 'Home'  # Проверяем текст кнопки "Home"
    assert links_page.btn_home.get_dom_attribute('href') == 'https://demoqa.com'  # Проверяем ссылку кнопки Home

    assert len(browser.window_handles) == 1  # Проверяем, что открыта 1 вкладка
    links_page.btn_home.click()  # Кликаем на кнопку "Home"
    time.sleep(2)
    assert len(browser.window_handles) == 2  # Проверяем, что открыты 2 вкладки

    """ Проверяем 1-ю стартовую вкладку (demoqa.com/links) """
    assert links_page.btn_home.exist()  # Проверяем в явном виде, что кнопка "Home" существует
    assert browser.current_url == 'https://demoqa.com/links'
    assert browser.title == 'DEMOQA'  # Также проверяем Title

    """ Проверяем 2-ю новую вкладку (demoqa.com/) """
    browser.switch_to.window(browser.window_handles[1])  # Переключаемся на 2-ю вкладку
    assert not links_page.btn_home.exist()  # Проверяем, что кнопка "Home" НЕ существует (на главной странице)
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'  # Также проверяем Title
