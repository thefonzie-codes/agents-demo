import pytest
import json
import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import (
    save_chat_session,
    get_chat_session,
    get_all_chat_sessions,
    delete_chat_session,
    rename_chat_session,
    cleanup_old_chat_sessions,
)


class TestSaveChatSession:
    def test_save_new_session(self, mock_get_chat_conn, sample_messages):
        """Test saving a new chat session."""
        session_id = "new-session-123"
        title = "New Conversation"

        save_chat_session(session_id, title, sample_messages)

        result = get_chat_session(session_id)

        assert result is not None
        assert result["session_id"] == session_id
        assert result["title"] == title
        assert result["messages"] == sample_messages

    def test_save_session_update_existing(self, mock_get_chat_conn, sample_messages):
        """Test updating an existing chat session."""
        session_id = "update-session-456"
        title = "Original Title"

        save_chat_session(session_id, title, sample_messages)

        new_messages = sample_messages + [{"role": "user", "text": "New message"}]
        new_title = "Updated Title"

        save_chat_session(session_id, new_title, new_messages)

        result = get_chat_session(session_id)

        assert result is not None
        assert result["title"] == new_title
        assert result["messages"] == new_messages


class TestGetChatSession:
    def test_get_existing_session(self, mock_get_chat_conn, sample_messages):
        """Test getting an existing session."""
        session_id = "get-session-789"
        title = "Get Test"

        save_chat_session(session_id, title, sample_messages)

        result = get_chat_session(session_id)

        assert result is not None
        assert result["session_id"] == session_id
        assert result["title"] == title
        assert result["messages"] == sample_messages

    def test_get_nonexistent_session(self, mock_get_chat_conn):
        """Test getting a non-existent session returns None."""
        result = get_chat_session("nonexistent-id")

        assert result is None


class TestGetAllChatSessions:
    def test_get_all_sessions_sorted_by_updated_at(
        self, mock_get_chat_conn, sample_messages
    ):
        """Test getting all sessions sorted by updated_at descending."""
        cursor = mock_get_chat_conn.return_value._conn.cursor()

        cursor.execute(
            "INSERT INTO chat_sessions (session_id, title, messages, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (
                "session-1",
                "First Session",
                "[]",
                "2024-01-01 10:00:00",
                "2024-01-01 10:00:00",
            ),
        )
        cursor.execute(
            "INSERT INTO chat_sessions (session_id, title, messages, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (
                "session-2",
                "Second Session",
                "[]",
                "2024-01-01 11:00:00",
                "2024-01-01 11:00:00",
            ),
        )
        cursor.execute(
            "INSERT INTO chat_sessions (session_id, title, messages, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (
                "session-3",
                "Third Session",
                "[]",
                "2024-01-01 12:00:00",
                "2024-01-01 12:00:00",
            ),
        )
        mock_get_chat_conn.return_value._conn.commit()

        results = get_all_chat_sessions()

        assert len(results) == 3
        assert results[0]["session_id"] == "session-3"
        assert results[1]["session_id"] == "session-2"
        assert results[2]["session_id"] == "session-1"

    def test_get_all_sessions_empty(self, mock_get_chat_conn):
        """Test getting all sessions when none exist."""
        results = get_all_chat_sessions()

        assert results == []


class TestDeleteChatSession:
    def test_delete_existing_session(self, mock_get_chat_conn, sample_messages):
        """Test deleting an existing session."""
        session_id = "delete-session-101"

        save_chat_session(session_id, "To Delete", sample_messages)

        result = delete_chat_session(session_id)

        assert result is True

        session = get_chat_session(session_id)
        assert session is None

    def test_delete_nonexistent_session(self, mock_get_chat_conn):
        """Test deleting a non-existent session returns False."""
        result = delete_chat_session("nonexistent-delete")

        assert result is False


class TestRenameChatSession:
    def test_rename_existing_session(self, mock_get_chat_conn, sample_messages):
        """Test renaming an existing session."""
        session_id = "rename-session-202"

        save_chat_session(session_id, "Old Title", sample_messages)

        result = rename_chat_session(session_id, "New Title")

        assert result is True

        session = get_chat_session(session_id)
        assert session["title"] == "New Title"

    def test_rename_nonexistent_session(self, mock_get_chat_conn):
        """Test renaming a non-existent session returns False."""
        result = rename_chat_session("nonexistent-rename", "New Title")

        assert result is False


class TestCleanupOldSessions:
    def test_cleanup_old_sessions(self, mock_get_chat_conn, sample_messages):
        """Test cleanup deletes sessions older than TTL."""
        old_date = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S")
        recent_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

        cursor = mock_get_chat_conn.return_value.cursor()
        cursor.execute(
            "INSERT INTO chat_sessions (session_id, title, messages, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            ("old-session", "Old", "[]", old_date, old_date),
        )
        cursor.execute(
            "INSERT INTO chat_sessions (session_id, title, messages, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            ("recent-session", "Recent", "[]", recent_date, recent_date),
        )
        mock_get_chat_conn.return_value.commit()

        deleted_count = cleanup_old_chat_sessions(days=7)

        assert deleted_count == 1

        assert get_chat_session("old-session") is None
        assert get_chat_session("recent-session") is not None

    def test_cleanup_no_old_sessions(self, mock_get_chat_conn, sample_messages):
        """Test cleanup does nothing when no sessions are old."""
        recent_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

        cursor = mock_get_chat_conn.return_value.cursor()
        cursor.execute(
            "INSERT INTO chat_sessions (session_id, title, messages, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            ("recent-session", "Recent", "[]", recent_date, recent_date),
        )
        mock_get_chat_conn.return_value.commit()

        deleted_count = cleanup_old_chat_sessions(days=7)

        assert deleted_count == 0
        assert get_chat_session("recent-session") is not None
