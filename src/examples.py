from typing import Dict
from fastapi.openapi.models import Example

TODO_EXAMPLES: Dict[str, Example] = {
    "SHOPPING": {
        "summary": "Список покупок",
        "value": {"id": 1, "item": {"item": "Купить молоко и хлеб", "status": False}},
    },
    "WORK": {
        "summary": "Рабочая задача",
        "value": {
            "id": 2,
            "item": {"item": "Завершить отчет по проекту", "status": False},
        },
    },
    "COMPLETED": {
        "summary": "Выполненная задача",
        "value": {
            "id": 3,
            "item": {"item": "Отправить письмо клиенту", "status": True},
        },
    },
    "HOME": {
        "summary": "Домашнее дело",
        "value": {"id": 4, "item": {"item": "Починить кран на кухне", "status": False}},
    },
    "LEARNING": {
        "summary": "Обучение",
        "value": {
            "id": 5,
            "item": {"item": "Изучить новую функцию FastAPI", "status": True},
        },
    },
}


TODO_UPDATE_EXAMPLES: Dict[str, Example] = {
    "SHOPPING": {
        "summary": "Список покупок",
        "value": {"item": {"item": "Купить молоко и хлеб", "status": False}},
    },
    "WORK": {
        "summary": "Рабочая задача",
        "value": {
            "item": {"item": "Завершить отчет по проекту", "status": False},
        },
    },
    "COMPLETED": {
        "summary": "Выполненная задача",
        "value": {
            "item": {"item": "Отправить письмо клиенту", "status": True},
        },
    },
    "HOME": {
        "summary": "Домашнее дело",
        "value": {"item": {"item": "Починить кран на кухне", "status": False}},
    },
    "LEARNING": {
        "summary": "Обучение",
        "value": {
            "item": {"item": "Изучить новую функцию FastAPI", "status": True},
        },
    },
}
