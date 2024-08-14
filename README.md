# ToDo List App

## Особенности

>Приложение должно предоставлять REST API для выполнения CRUD операций с задачами и пользователями.

Реализованно на **FastAPI framework**.

## To Do

- [ ] Документация
- [ ] Тесты
- [x] База данных клиентов
- [x] Реализовать валидацию входящих данных
- [x] Логирование действий (создание, обновление, удаление)
- [x] Реализовать фильтрацию задач по статусу

## Оглавление 📚
- [To Do](#to-do)
- [Оглавление📚](#оглавление-)
- [🛠️Начало работы](#️начало-работы)
- [💡Использование](#использование)
    - [API Эндпоинты](#api-эндпоинты)
- [Примеры](#примеры)

## 🛠️Начало работы
1. Создать виртуальное окружение
```bash
python -m venv venv
```
2. Установить необходимые компоненты
```bash
pip install -r requirements.txt
```

## 💡Использование
**ПРИМЕЧАНИЕ:** Запуск с корня проекта
```bash
uvicorn app.main:app --reload
```

### API Эндпоинты

#### *Пользователи:*
- **GET /users** - получить список всех пользователей
- **GET /users/{id}** - получить информацию о конкретном пользователе
- **POST /users** - создать нового пользователя
- **PUT /users/{id}** - обновить информацию о пользователе
- **DELETE /users/{id}** - удалить пользователя

#### *Задачи:*
- **GET /tasks** - получить список всех задач
- **GET /tasks/{id}** - получить информацию о конкретной задаче
- **POST /tasks** - создать новую задачу
- **PUT /tasks/{id}** - обновить информацию о задаче
- **DELETE /tasks/{id}** - удалить задачу

## FastAPI

ASGI/WSGI подход

## Тесты 
Используем pytest

## Примеры

**Get** /users/ *users_list*
```json
[
    {
    "username": "Cool enjoyer",
    "email": "enjoyer@gmail.com",
    "full_name": "Enjoer Collson Wats",
    "id": 1,
    "tasks": [
        {
        "title": "cook dinner",
        "description": "Buy french chicken",
        "completed": false,
        "id": 1,
        "owner_id": 1
      },
      {
        "title": "Create tests",
        "description": "Chat GPT to resolve",
        "completed": false,
        "id": 2,
        "owner_id": 1
      }
    ]
    },
    {
    "username": "string",
    "email": "string@gmail.com",
    "full_name": "Stringovich",
    "id": 2,
    "tasks": []
    }
]
``` 
