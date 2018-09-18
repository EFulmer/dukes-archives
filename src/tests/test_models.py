"""Unit tests for the database models."""
import pytest
from ..model.book import Book


class TestBooks:
    """Tests for the Book model."""
    def test_cannot_create_future_book(self):
        with pytest.raises(Exception) as e:
            pass
