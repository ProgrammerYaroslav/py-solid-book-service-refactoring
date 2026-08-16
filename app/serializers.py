# app/serializers.py
import json
import xml.etree.ElementTree as ET
from typing import Protocol
from app.models import Book

class Serializer(Protocol):
    def serialize(self, book: Book) -> str: ...

class JsonSerializer:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

class XmlSerializer:
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")