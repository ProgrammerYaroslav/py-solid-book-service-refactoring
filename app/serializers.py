import json
import xml.etree.ElementTree as etree
from typing import Protocol
from app.models import Book


class Serializer(Protocol):
    def serialize(self, book: Book) -> str:
        ...


class JsonSerializer:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    def serialize(self, book: Book) -> str:
        root = etree.Element("book")
        title = etree.SubElement(root, "title")
        title.text = book.title
        content = etree.SubElement(root, "content")
        content.text = book.content
        return etree.tostring(root, encoding="unicode")
