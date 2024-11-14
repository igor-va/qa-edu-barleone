# Проект автотестирования UI сайта "Barleone"


## Оглавление
[1. Описание проекта](#1-описание-проекта)
- [Структура проекта](#структура-проекта)
- [Основные функции](#основные-функции)
- [Технологии и инструменты](#технологии-и-инструменты)
- [Настройка окружения](#настройка-окружения)
- [Запуск тестов](#запуск-тестов)


## 1. Описание проекта
Проект представляет собой учебный набор автоматизированных UI тестов веб-сайта "https://barleone.ru/"


## Структура проекта
```
qa-edu-barleone/
│
├── Configurations/        # Конфигурационные файлы
├── Info/                  # Информационные файлы
├── Locators/              # Локаторы
├── Logs/                  # Логи
├── Pages/                 # Страницы POM
├── Reports/               # Отчеты
├── Screenshots/           # Скриншоты
├── TestData/              # Тестовые данные
├── Tests/                 # Тестовые модули
│   └── conftest.py        # Фикстуры PyTest
├── Utilities/             # Вспомогательные утилиты
├── .gitignore             # Исключенные файлы
├── docker-compose.yaml    # Инструкции для Docker Compose
├── Dockerfile             # Инструкции для Docker Image
├── pytest.ini             # Конфигурации PyTest
├── README.md              # Описание проекта
└── requirements.txt       # Зависимости проекта
```


## Основные функции
- Открытие основных страниц сайта
- Добавление товаров в корзину
- Авторизации в личном кабинете


## Технологии и инструменты
- Python 3.12+
- Pytest
- Selenium
- Allure


## Настройка окружения
1. Убедитесь, что у вас установлен Python 3.12+
2. Склонируйте репозиторий:
   ```
   https://github.com/igor-va/qa-edu-barleone.git
   cd qa-edu-barleone
   ```
3. Создайте виртуальное окружение и активируйте его:
   ```
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```
4. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```


## Запуск тестов
Для запуска всех тестов:
```
pytest
```

Для генерации Allure-отчета:
```
pytest --alluredir=./AllureResults
allure serve ./AllureResults
```
