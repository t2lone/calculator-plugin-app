# 🧮 calculator-plugin-app

> Веб-калькулятор с поддержкой динамических плагинов на Python/Flask

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Описание

**calculator-plugin-app** — это модульное веб-приложение калькулятора, построенное на микрофреймворке Flask. Главная особенность проекта — **архитектура с поддержкой плагинов**, которая позволяет добавлять новые математические операции без изменения основного кода приложения.

### ✨ Возможности

- 🔌 **Динамическая загрузка плагинов** — новые операции подключаются автоматически при добавлении файла в папку `plugins/`
- 🧩 **Расширяемость** — добавляйте свои операции (сложение, умножение, тригонометрия и др.) через простой интерфейс
- 🌐 **REST API** — endpoints для получения списка операций и выполнения вычислений
- 💻 **Веб-интерфейс** — простой и понятный интерфейс на HTML/CSS
- 🐍 **Чистый Python** — использование `importlib` для безопасной загрузки модулей

---

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8 или выше
- pip (менеджер пакетов Python)

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/t2lone/calculator-plugin-app.git
cd calculator-plugin-app
```
2. Установите зависимости:
```bash
pip install flask
```
3.Запустите приложение:
```bash
python app.py
```
4.Откройте в браузере:
```bash
http://localhost:5000
```
📁 Структура проекта
-  calculator-plugin-app/
- ├── app.py                 # Основной файл приложения (Flask + PluginManager)
- ├── plugins/               # Папка для плагинов
- │   └── plugin_*.py        # Шаблоны плагинов (например, plugin_add.py)- 
- ├── templates/             # HTML-шаблоны
- │   └── index.html         # Главная страница калькулятора
- ├── static/                # Статические файлы
- │   ├── css/              # Стили
- │   └── js/               # Скрипты (при необходимости)
- ├── README.md             # Этот файл
- └── requirements.txt      # Зависимости проекта (опционально)
