# FastAPI Demo Project

Современный backend-проект на FastAPI с использованием Poetry, SQLAlchemy 2.0, PostgreSQL и Alembic. Проект построен с учетом принципов чистой архитектуры и готов к масштабированию.

## 🏗️ Архитектура проекта

Проект организован по принципу разделения ответственности (Separation of Concerns):

```
src/                                   # Исходный код приложения
├── account/                           # Модуль "Аккаунт/Пользователи"
│   ├── models/                        # SQLAlchemy модели
│   │   ├── __init__.py
│   │   └── user.py                    # Модель пользователя
│   ├── repositories/                  # Слой репозиториев
│   │   ├── __init__.py
│   │   └── user.py                    # Репозиторий пользователя
│   ├── router/                        # API роуты
│   │   ├── __init__.py
│   │   ├── role.py                    # Роут для ролей
│   │   └── user.py                    # Роут для пользователей
│   ├── schemas/                       # Pydantic схемы
│   │   ├── __init__.py
│   │   └── user.py                    # Схемы пользователя
│   └── services/                      # Бизнес-логика
│       ├── __init__.py
│       └── constants.py               # Константы модуля account
│
├── core/                              # Ядро приложения
│   ├── __init__.py
│   ├── async_test.py                  # Тесты асинхронности
│   └── main.py                        # Точка входа FastAPI
│
└── tests/                             # Тесты приложения
```

### 🔧 Используемые технологии

| Компонент | Технология |
|-----------|------------|
| **Web Framework** | FastAPI 0.115.0+ |
| **ORM** | SQLAlchemy 2.0+ |
| **Миграции** | Alembic |
| **База данных** | PostgreSQL |
| **Управление зависимостями** | Poetry |
| **Валидация** | Pydantic v2 |
| **Линтер/Форматтер** | Ruff |
| **Сервер** | Uvicorn |

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone <url-репозитория>
cd FastAPI-demo
```

### 2. Установка Poetry (если не установлен)

```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Linux/macOS
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Установка зависимостей

```bash
poetry install
```

### 4. Настройка окружения

Создайте файл `.env` на основе шаблона:

```bash
cp .env.example .env
```

Отредактируйте `.env` и укажите свои параметры:

```env
# PostgreSQL
PG_HOST=localhost
PG_USER=your_username
PG_PASS=your_password
PG_NAME=fastapi_demo
PG_PORT=5432
```

### 5. Настройка базы данных

Запустите PostgreSQL (локально или через Docker):

```bash
# Docker (опционально)
docker run -d --name fastapi-db -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=fastapi_demo -p 5432:5432 postgres:16-alpine
```

### 6. Применение миграций

```bash
poetry run alembic upgrade head
```

### 7. Запуск приложения

```bash
poetry run uvicorn src.main:app --reload
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

**Документация API:**
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📦 Управление проектом

### Основные команды Poetry

```bash
# Установка зависимостей
poetry install

# Добавление новой зависимости
poetry add fastapi

# Добавление dev-зависимости
poetry add --group dev ruff

# Обновление зависимостей
poetry update

# Запуск в виртуальном окружении
poetry run python script.py
```

### Работа с Alembic

```bash
# Создание новой миграции
poetry run alembic revision --autogenerate -m "описание изменений"

# Применение миграций
poetry run alembic upgrade head

# Откат на предыдущую миграцию
poetry run alembic downgrade -1

# История миграций
poetry run alembic history
```

### Контроль качества кода

```bash
# Проверка кода (линтер)
poetry run ruff check src/

# Автоисправление ошибок
poetry run ruff check --fix src/

# Форматирование кода
poetry run ruff format src/

# Проверка типов (если настроено)
poetry run mypy src/
```

## 🧪 Тестирование

```bash
# Запуск всех тестов
poetry run pytest

# Запуск с покрытием
poetry run pytest --cov=src

# Запуск конкретного теста
poetry run pytest tests/test_user.py -v
```

## 📁 Структура проекта

```
FastAPI-demo/                              # Корень проекта
├── .venv/                                 # Виртуальное окружение (не в репозитории)
│   └── library root
│
├── alembic/                               # Миграции Alembic
│   ├── versions/                          # Файлы миграций
│   ├── env.py                             # Конфигурация Alembic
│   ├── README                             # Документация Alembic
│   └── script.py.mako                     # Шаблон для миграций
│
├── src/                                   # Исходный код приложения
│   ├── account/                           # Модуль "Аккаунт/Пользователи"
│   │   ├── models/                        # SQLAlchemy модели
│   │   │   ├── __init__.py
│   │   │   └── user.py                    # Модель пользователя
│   │   ├── repositories/                  # Слой репозиториев
│   │   │   ├── __init__.py
│   │   │   └── user.py                    # Репозиторий пользователя
│   │   ├── router/                        # API роуты
│   │   │   ├── __init__.py
│   │   │   ├── role.py                    # Роут для ролей
│   │   │   └── user.py                    # Роут для пользователей
│   │   ├── schemas/                       # Pydantic схемы
│   │   │   ├── __init__.py
│   │   │   └── user.py                    # Схемы пользователя
│   │   └── services/                      # Бизнес-логика
│   │       ├── __init__.py
│   │       └── constants.py               # Константы модуля account
│   │
│   ├── core/                              # Ядро приложения
│   │   ├── __init__.py
│   │   ├── async_test.py                  # Тесты асинхронности
│   │   └── main.py                        # Точка входа FastAPI
│   │
│   └── tests/                             # Тесты приложения
│
├── .env                                   # Переменные окружения (не в репозитории)
├── .env.example                           # Шаблон переменных окружения
├── .gitignore                             # Игнорируемые файлы Git
├── alembic.ini                            # Настройки Alembic
├── poetry.lock                            # Фиксированные версии зависимостей
├── pyproject.toml                         # Настройки Poetry и проекта
└── README.md                              # Документация проекта
```

## 🔐 Переменные окружения

| Переменная | Описание | Пример         |
|------------|----------|----------------|
| `PG_HOST` | Хост PostgreSQL | `localhost`    |
| `PG_USER` | Пользователь БД | `your_username`     |
| `PG_PASS` | Пароль БД | `your_pass`    |
| `PG_NAME` | Имя базы данных | `fastapi_demo` |
| `PG_PORT` | Порт PostgreSQL | `5432`         |

## 🛠️ Требования к разработчику

Для работы с проектом необходимо:
- Python 3.12+
- PostgreSQL 15+
- Poetry 1.8+
- Git

## 🤝 Вклад в проект

1. Создайте ветку для вашей фичи: `git checkout -b feature/your-feature`
2. Внесите изменения и добавьте тесты
3. Запустите линтер: `poetry run ruff check src/`
4. Отправьте Pull Request

## 📝 Важные принципы

1. **API слой** (`routers/`) — только маршруты и валидация
2. **Сервисный слой** (`services/`) — бизнес-логика
3. **Репозитории** (`repositories/`) — работа с БД
4. **Схемы** (`schemas/`) — Pydantic для валидации
5. **Модели** (`models/`) — SQLAlchemy описания таблиц

## 📚 Полезные ссылки

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

---
