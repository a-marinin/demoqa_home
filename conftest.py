import pytest
from selenium import webdriver


'''В данном случае декоратор @pytest.fixture изменяет поведение функции browser'''
@pytest.fixture(scope="session") # Это декоратор (функция-обёртка, изменяющая поведение другой функции)
def browser():
    driver = webdriver.Chrome()  # Передали наш драйвер
    # browser.set_window_size(width=1000, height=1000)  # Установили размер браузера.
    yield driver  # Чтобы наш драйвер мог использовать в функции
    driver.quit()  # Закрываем драйвер

""" Не работает. Удалю потом, после 13-го занятия """
# """ Для дополнительного пункта, первой задачи, 12 домашнего задания """
# def pytest_addoption(parser):
#     parser.addoption(
#         "--runslow", action="store_true", default=False, help="run slow tests"
#     )
#
#
# def pytest_configure(config):
#     config.addinivalue_line("markers", "slow: mark test as slow to run")
#
#
# def pytest_collection_modifyitems(config, items):
#     if config.getoption("--runslow"):
#         # --runslow given in cli: do not skip slow tests
#         return
#     skip_slow = pytest.mark.skip(reason="need --runslow option to run")
#     for item in items:
#         if "slow" in item.keywords:
#             item.add_marker(skip_slow)
