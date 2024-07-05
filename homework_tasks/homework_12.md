## Домашнее задание №12

### Задание №1
1. в файле test_check_modal.py автоматизируйте тест кейс
   1. страница https://demoqa.com/modal-dialogs
        1. на странице присутствуют 2 кнопки “Small modal” и “Large modal”
        2. при клике на каждую открывается модальное окно
        3. у каждого окна есть кнопка “close” по клику окно закрывается
        4. (⭐ **задание со звёздочкой**) Доработайте тестовый файл так, чтоб тест пропускался если страница недоступна.  
      Подумайте, как можно проверять страницу на доступность.

### Задание №2
1. в файле test_check_alert.py автоматизируйте тест кейс:
   1. Страница https://demoqa.com/alerts
      1. на странице присутствует кнопка “#timerAlertButton”
      2. через 5 сек после клика на кнопку всплывает алерт

### Задание №3
1. в файле test_sort.py автоматизируйте тест кейс:
   1. Страница https://demoqa.com/webtables
   2. при клике на каждый заголовок столбца страницы, происходит сортировка таблицы по этому столбцу  
   (Для проверки сортировки, в данном кейсе, достаточно считывать соответствующий класс элемента)


### Задание №4
1. (⭐ **задание со звёздочкой**) в файле test_window_tab.py автоматизируйте тест кейс:
   1. Страница https://demoqa.com/links
   2. На странице имеется ссылка “Home”
   3. текст ссылки == “Home”
   4. href ссылки == “https://demoqa.com”
   5. При клике на ссылку открывается новая вкладка


### Решения
1. Задача №1: https://github.com/a-marinin/demoqa_home/blob/master/tests/tests_hw/test_check_modal.py
2. Задача №2: https://github.com/a-marinin/demoqa_home/blob/master/tests/tests_hw/test_check_alert.py
3. Задача №3 (решил её 2-мя способами: по классу элемента и через значения колонок): https://github.com/a-marinin/demoqa_home/blob/master/tests/tests_hw/test_sort.py
4. Задача №4: https://github.com/a-marinin/demoqa_home/blob/master/tests/tests_hw/test_window_tab.py
