📋 Описание
calculator-plugin-app — это модульное веб-приложение калькулятора, построенное на микрофреймворке Flask. Главная особенность проекта — архитектура с поддержкой плагинов, которая позволяет добавлять новые математические операции без изменения основного кода приложения.
✨ Возможности
🔌 Динамическая загрузка плагинов — новые операции подключаются автоматически при добавлении файла в папку plugins/
🧩 Расширяемость — добавляйте свои операции (сложение, умножение, тригонометрия и др.) через простой интерфейс
🌐 REST API — endpoints для получения списка операций и выполнения вычислений
💻 Веб-интерфейс — простой и понятный интерфейс на HTML/CSS
🐍 Чистый Python — использование importlib для безопасной загрузки модулей
🚀 Быстрый старт
Предварительные требования
Python 3.8 или выше
pip (менеджер пакетов Python)
Установка
Клонируйте репозиторий:
git clone https://github.com/t2lone/calculator-plugin-app.git
cd calculator-plugin-app
Установите зависимости:
pip install flask
Запустите приложение:
python app.py
Откройте в браузере:
http://localhost:5000

📁 Структура проекта
calculator-plugin-app/
├── app.py                 # Основной файл приложения (Flask + PluginManager)
├── plugins/               # Папка для плагинов
│   └── plugin_*.py        # Шаблоны плагинов (например, plugin_add.py)
├── templates/             # HTML-шаблоны
│   └── index.html         # Главная страница калькулятора
├── static/                # Статические файлы
│   ├── css/              # Стили
│   └── js/               # Скрипты (при необходимости)
├── README.md             # Этот файл
└── requirements.txt      # Зависимости проекта (опционально)



🔌 Как создать плагин
Плагины — это обычные Python-файлы, которые должны:
Находиться в папке plugins/
Иметь имя в формате plugin_*.py
Содержать функцию register(), возвращающую словарь с описанием плагина
📝 Шаблон плагина
# plugins/plugin_multiply.py

def register():
    """Регистрация плагина в системе"""
    return {
        'name': 'Умножение',
        'operations': ['multiply'],  # Список операций, которые предоставляет плагин
        'calculate': calculate       # Функция для выполнения вычислений
    }

def calculate(a, b):
    """Логика вычисления операции"""
    return a * b

🧪 Примеры плагинов
<details>
<summary>➕ plugin_add.py</summary>
def register():
    return {
        'name': 'Сложение',
        'operations': ['add'],
        'calculate': calculate
    }

def calculate(a, b):
    return a + b
</details>

<details>
<summary>➖ plugin_subtract.py</summary>
def register():
    return {
        'name': 'Вычитание',
        'operations': ['subtract'],
        'calculate': calculate
    }

def calculate(a, b):
    return a - b
</details>

<details>
<summary>✖️ plugin_power.py (возведение в степень)</summary>
def register():
    return {
        'name': 'Степень',
        'operations': ['power'],
        'calculate': calculate
    }

def calculate(a, b):
    return a ** b
</details>
🌐 API Документация
Получить список доступных операций
GET /api/operations
