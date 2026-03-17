import pytest
import sqlite3
import os
import sys
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def test_db():
    """Create an in-memory SQLite database for testing."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE chat_sessions (
            session_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            messages TEXT NOT NULL
        )
    """)
    conn.commit()

    yield conn

    conn.close()


class PersistentConnection:
    """Wrapper to provide a persistent connection that doesn't close."""

    def __init__(self, conn):
        self._conn = conn
        self._closed = False

    def cursor(self):
        return self._conn.cursor()

    def commit(self):
        return self._conn.commit()

    def close(self):
        self._closed = True

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


@pytest.fixture
def mock_get_chat_conn(test_db):
    """Mock the get_chat_conn function to return test database."""
    persistent_conn = PersistentConnection(test_db)
    with patch("db.get_chat_conn") as mock:
        mock.return_value = persistent_conn
        yield mock


@pytest.fixture
def app(test_db):
    """Create Flask test application."""
    with patch("db.get_chat_conn") as mock_get_chat_conn:
        persistent_conn = PersistentConnection(test_db)
        mock_get_chat_conn.return_value = persistent_conn

        with patch("db.cleanup_old_chat_sessions") as mock_cleanup:
            mock_cleanup.return_value = 0

            from app import app

            app.config["TESTING"] = True

            with app.test_client() as client:
                yield client


@pytest.fixture
def sample_messages():
    """Sample messages for testing."""
    return [
        {"role": "user", "text": "Hello"},
        {"role": "assistant", "text": "Hi there!"},
    ]


@pytest.fixture
def sample_session():
    """Sample session data for testing."""
    return {
        "session_id": "test-session-123",
        "title": "Test Conversation",
        "messages": [
            {"role": "user", "text": "Hello"},
            {"role": "assistant", "text": "Hi there!"},
        ],
    }
