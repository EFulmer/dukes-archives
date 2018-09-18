from sqlalchemy import Column, Integer, String, Date
from sqlalchemy_utils import generic_repr


@generic_repr
class Book:
    """Book model."""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    isbn = Column(String, unique=True)
    original_publish_year = Column(Date, nullable=False)
    title = Column(String, nullable=False)

    @classmethod
    def add_new_book(cls):
        pass
