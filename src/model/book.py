from sqlalchemy import Column, Integer, String, Date


class Book:
    """Book model."""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    isbn = Column(String, unique=True)
    original_publich_year = Column(Date)

    @classmethod
    def add_new_book(cls):
        pass
