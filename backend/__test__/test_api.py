import pytest
import json
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestHealthEndpoint:
    def test_health_returns_ok(self, app, mock_get_chat_conn):
        """Test health check endpoint returns ok."""
        response = app.get("/api/health")

        assert response.status_code == 200
        assert response.json == {"status": "ok"}


class TestChatEndpoint:
    @patch("app.travel_agent")
    def test_chat_new_session(self, mock_agent, app, mock_get_chat_conn):
        """Test creating a new chat session."""
        mock_agent.call_with_history.return_value = ("Hello! How can I help?", [])

        response = app.post("/api/chat", json={"message": "Hello"})

        assert response.status_code == 200
        data = response.json
        assert "session_id" in data
        assert data["response"] == "Hello! How can I help?"

    @patch("app.travel_agent")
    def test_chat_existing_session(
        self, mock_agent, app, mock_get_chat_conn, sample_messages
    ):
        """Test continuing an existing chat session."""
        from db import save_chat_session

        session_id = "existing-session-123"
        save_chat_session(session_id, "Test", sample_messages)

        mock_agent.call_with_history.return_value = (
            "Following up on that",
            sample_messages,
        )

        response = app.post(
            "/api/chat", json={"message": "Tell me more", "session_id": session_id}
        )

        assert response.status_code == 200
        data = response.json
        assert data["session_id"] == session_id
        assert data["response"] == "Following up on that"

    def test_chat_missing_message(self, app, mock_get_chat_conn):
        """Test chat endpoint returns error when message is missing."""
        response = app.post("/api/chat", json={})

        assert response.status_code == 400
        assert "error" in response.json

    def test_chat_empty_message(self, app, mock_get_chat_conn):
        """Test chat endpoint returns error for empty message."""
        response = app.post("/api/chat", json={"message": "   "})

        assert response.status_code == 400
        assert "error" in response.json


class TestListSessionsEndpoint:
    def test_list_sessions_empty(self, app, mock_get_chat_conn):
        """Test listing sessions when none exist."""
        response = app.get("/api/sessions")

        assert response.status_code == 200
        assert response.json == {"sessions": []}

    def test_list_sessions_with_data(self, app, mock_get_chat_conn, sample_messages):
        """Test listing sessions with data."""
        from db import save_chat_session

        save_chat_session("session-1", "First", sample_messages)
        save_chat_session("session-2", "Second", sample_messages)

        response = app.get("/api/sessions")

        assert response.status_code == 200
        assert len(response.json["sessions"]) == 2


class TestGetSessionEndpoint:
    def test_get_session_exists(self, app, mock_get_chat_conn, sample_messages):
        """Test getting an existing session."""
        from db import save_chat_session

        session_id = "get-test-123"
        save_chat_session(session_id, "Test Session", sample_messages)

        response = app.get(f"/api/sessions/{session_id}")

        assert response.status_code == 200
        data = response.json
        assert data["session_id"] == session_id
        assert data["title"] == "Test Session"
        assert data["messages"] == sample_messages

    def test_get_session_not_found(self, app, mock_get_chat_conn):
        """Test getting a non-existent session returns 404."""
        response = app.get("/api/sessions/nonexistent")

        assert response.status_code == 404
        assert "error" in response.json


class TestDeleteSessionEndpoint:
    def test_delete_session_exists(self, app, mock_get_chat_conn, sample_messages):
        """Test deleting an existing session."""
        from db import save_chat_session

        session_id = "delete-test-456"
        save_chat_session(session_id, "To Delete", sample_messages)

        response = app.delete(f"/api/sessions/{session_id}")

        assert response.status_code == 200
        assert response.json["status"] == "deleted"

    def test_delete_session_not_found(self, app, mock_get_chat_conn):
        """Test deleting a non-existent session returns 404."""
        response = app.delete("/api/sessions/nonexistent-delete")

        assert response.status_code == 404
        assert "error" in response.json


class TestRenameSessionEndpoint:
    def test_rename_session_exists(self, app, mock_get_chat_conn, sample_messages):
        """Test renaming an existing session."""
        from db import save_chat_session

        session_id = "rename-test-789"
        save_chat_session(session_id, "Old Name", sample_messages)

        response = app.post(
            f"/api/sessions/{session_id}/rename", json={"title": "New Name"}
        )

        assert response.status_code == 200
        assert response.json["status"] == "renamed"
        assert response.json["title"] == "New Name"

    def test_rename_session_missing_title(self, app, mock_get_chat_conn):
        """Test rename returns error when title is missing."""
        response = app.post("/api/sessions/session-123/rename", json={})

        assert response.status_code == 400
        assert "error" in response.json

    def test_rename_session_empty_title(self, app, mock_get_chat_conn):
        """Test rename returns error for empty title."""
        response = app.post("/api/sessions/session-123/rename", json={"title": "   "})

        assert response.status_code == 400
        assert "error" in response.json

    def test_rename_session_not_found(self, app, mock_get_chat_conn):
        """Test renaming a non-existent session returns 404."""
        response = app.post(
            "/api/sessions/nonexistent-rename/rename", json={"title": "New Name"}
        )

        assert response.status_code == 404
        assert "error" in response.json
