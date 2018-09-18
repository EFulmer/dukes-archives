from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy_utils import generic_repr
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite3:///:memory:', echo=True)
Base = declarative_base(bind=engine)


@generic_repr
class Book(Base):
    """Book model."""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    original_publish_year = Column(Date)
    title = Column(String, nullable=False)

    @classmethod
    def add_new_book(cls, title, original_publish_year):
        pass

    @classmethod
    def get_book_by_title(cls, title):
        pass

    @classmethod
    def get_books_from_year(cls, year):
        pass
