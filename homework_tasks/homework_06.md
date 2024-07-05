#### Домашнее задание №6

### Задание №1 (Повторите алгоритм построения архитектуры)
1. Повторите алгоритм построения архитектуры
2. создайте новый проект demoqa_home
   1. Создаем директорию pages
   2. Создаем директорию tests
   3. Создаем директорию components
   4. копируем драйвер в корень проекта
   5. В корне создаем файл .gitignore
   6. В корне создаем файл readme.md
   7. В корне создаем файл conftest.py
   8. команды:
      1. pip install pytest
      2. pip install selenium
      3. git init
      4. pip freeze > requirements.txt
   9. в гитигнор вставляем
      1. /venv
      2. .idea
      3. *.pytest_cache


### Задание №2 (реализация фикстуры и base_page.py)
1. В директории tests создайте файл test_check_swag.py
2. В файле conftest.py создайте фикстуру, код такой же как в рабочем проекте
3. реализация base_page.py
   1. В каталоге pages создайте файл base_page.py
   2. в файле создайте класс BasePage
   3. При инициализации у класса есть 2 атрибута:
      1. driver - принимается в качестве аргумента
      2. base_url - не принимается, установлено значение по умолчанию, 'https://www.saucedemo.com/'.
   4. Создайте метод visit который возвращает переход на страницу (.get())
   5. Создайте метод find_element
      1. метод принимает аргумент locator
      2. возвращает поиск элемента (.find_element())
   6. также необходимо добавить импорт from selenium.webdriver.common.by import By


### Задание №3 (реализация страницы swag_labs)
1. реализация swag_labs.py
   1. В каталоге pages создайте файл swag_labs.py
   2. в файле создайте класс SwagLabs
   3. класс не имеет атрибутов, конструктор не требуется
   4. наследуйте класс от класса BasePage (при импорте не забудьте указать путь вместе с каталогом pages.base_page )
   5. Создайте метод exist_icon
   6. метод вызывает метод find_element родительского класса и передает в него локатор locator='div.login_logo'
   7. Для красоты кода воспользуемся конструкцией try except
      1. try:
         1. self.find_element(locator='div.login_logo')
      2. except NoSuchElementException:
         1. return False
      3. return True
   8. Исключение надо импортировать from selenium.common.exceptions import NoSuchElementException


### Задание №4 (1-я проверка в тест кейсе test_check_swag.py)
1. реализуйте тест кейс
   1. в файле test_check_swag.py реализуйте следующий тест кейс:
      1. перейти на страницу https://www.saucedemo.com/
      2. проверить наличие иконки

### Задание №5 (2-я проверка в тест кейсе test_check_swag.py)
1. реализуйте тест кейс
   1. в файле test_check_swag.py реализуйте следующий тест кейс:
      1. перейти на страницу https://www.saucedemo.com/
      2. проверить наличие поля имени

### Задание №6 (3-я проверка в тест кейсе test_check_swag.py)
1. реализуйте тест кейс
   1. в файле test_check_swag.py реализуйте следующий тест кейс:
      1. перейти на страницу https://www.saucedemo.com/
      2. проверить наличие поля пароля

    
### Решения