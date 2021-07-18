## Подготовка окружения

### Установка Selenoid
- установить homebrew https://brew.sh/index_ru
- установить wget (brew install wget)
- установить Selenoid https://aerokube.com/selenoid/latest/
- обновить/скачать образы браузеров ./cm selenoid update

### Подготовка к запуску тестов
- установить глобально python 3.8
- установить глобально poetry
- установить allure (brew install allure)
- скачать PyCharm
- создать проект Pure Python, интерпретатор: 3.8
- склонировать репозиторий https://github.com/JsvnSvn/test_eapteka.git
- перейти в папку проекта
- установить зависимости (poetry install)
  
### Запуск тестов
- запустить тесты с помощью скрипта run_tests.sh (для мобильных тестов заменить desktop на mobile)


