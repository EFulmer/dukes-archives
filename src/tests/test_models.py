"""Unit tests for the database models."""
import pytest
from sqlalchemy.

from ..models import Book, engine


class TestBooks:
    """Tests for the Book model."""
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_cannot_create_future_book(self):
        with pytest.raises(Exception) as e:
            pass

    def test_can_add_book(self):
        pass

    def test_get_books_from_year(self):
        pass
