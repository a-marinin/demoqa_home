from pages.alerts import Alerts
import time


def test_alert_appearance_after_5_seconds(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.timerAlertButton.exist()  # Проверяем, что на странице есть кнопка для вызова алерта с тайм-аутом

    assert not alert_page.alert()  # Проверяем, что активных алертов на странице нет
    alert_page.timerAlertButton.click()  # Кликаем на кнопку для вызова алерта через 5 секунд
    assert not alert_page.alert()  # Проверяем, что активных алертов на странице нет
    time.sleep(1)  # Ждём 1 секунду
    assert not alert_page.alert()  # Проверяем, что активных алертов на странице нет
    time.sleep(1)  # Ждём 1 секунду (всего прошло 2 секунды)
    assert not alert_page.alert()  # Проверяем, что активных алертов на странице нет
    time.sleep(1)  # Ждём 1 секунду (всего прошло 3 секунды)
    assert not alert_page.alert()  # Проверяем, что активных алертов на странице нет
    time.sleep(1)  # Ждём 1 секунду (всего прошло 5 секунды)
    assert not alert_page.alert()  # Проверяем, что активных алертов на странице нет
    time.sleep(1)  # <<<<< Если закомментировать эту строку, то тест кейс упадёт

    assert alert_page.alert()  # Проверяем, что есть активный алерт на странице
