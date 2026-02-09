# services/book_actions.py
class BookService:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def create_book(self, data):
        # Логіка збереження
        book = self.repository.save(data)
        # Логіка сповіщення
        self.notifier.send(f"Книга '{book.title}' додана успішно!")
        return book
