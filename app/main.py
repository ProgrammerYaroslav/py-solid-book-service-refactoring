# app/main.py
import xml.etree.ElementTree as ET  # Виправлено N817: використовуємо стандартний аліас ET
from typing import Any
from services.book_actions import BookService
from services.notifications import EmailNotification
from repositories.book_repo import BookRepository

class App:
    def __init__(self) -> None:  # Виправлено ANN204: додано аннотацію -> None
        self.repo = BookRepository()
        self.notifier = EmailNotification()
        self.service = BookService(self.repo, self.notifier)

    def run(self, data: dict[str, Any]) -> Any:
        # Логіка має залишатися ідентичною оригінальній
        return self.service.create_book(data)
