# app/models.py
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    content: str
