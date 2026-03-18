import uuid
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from ai.agent import Agent
from db import (
    generate_db,
    query_db,
    save_chat_session,
    get_chat_session,
    get_all_chat_sessions,
    delete_chat_session,
    rename_chat_session,
    cleanup_old_chat_sessions,
)

load_dotenv()

CHAT_SESSION_TTL_DAYS = int(os.getenv("CHAT_SESSION_TTL_DAYS", "7"))

# --- Database setup ---
DB_PATH = "./sample_datasets/travel_company_customer_db/travel_company.db"
SCHEMA_PATH = "./sample_datasets/travel_company_customer_db/schema.sql"

print("Generating Mock Travel Company Customer Data...")
generate_db(DB_PATH)

print(f"Cleaning up chat sessions older than {CHAT_SESSION_TTL_DAYS} days...")
deleted = cleanup_old_chat_sessions(CHAT_SESSION_TTL_DAYS)
if deleted > 0:
    print(f"Deleted {deleted} old chat sessions")

# --- Load schema for tool declaration ---
schema = open(SCHEMA_PATH, "r").read()

query_db_declaration = {
    "name": "query_db",
    "description": "Searches the sqlite 3 database and returns a tuple of the values requested",
    "parameters": {
        "type": "object",
        "properties": {
            "sqlite3_query": {
                "type": "string",
                "description": f"""
                    An SQLITE3 query to search the database. This is the current schema:
                    {schema}
                    """,
            },
        },
        "required": ["sqlite3_query"],
    },
}


def query_db_tool(args):
    """Wrapper for query_db that accepts args dict from Gemini."""
    return query_db(args["sqlite3_query"])


system_instruction = """
You are an AI assistant supporting customer service agents at a travel company. Your role is to help agents
quickly access customer information, booking details, and resolve support cases efficiently.

## Your Capabilities:
- Query the customer database to retrieve information about customers, bookings, packages, destinations, payments, and support cases
- Provide accurate, data-driven responses based on database records
- Help draft professional emails, phone scripts, and customer communications
- Suggest appropriate actions based on case priority, status, and customer history

## Database Structure:
The database contains: customers (contact info, loyalty points), destinations (locations, pricing), packages
(travel offerings), bookings (reservations with dates and status), payments (transaction records), and cases
(support tickets with priority levels).

## Response Guidelines:
- Always query the database first before providing specific customer information
- Be concise and professional - agents need quick, actionable information
- Include relevant IDs (customer_id, booking_id, case_id) in your responses
- For customer communications, maintain a warm, empathetic, and solution-focused tone
- If multiple records match, ask for clarification (e.g., "I found 3 bookings for this customer. Which one?")
- Prioritize critical and high-priority cases in your recommendations

## When Drafting Communications:
- Match the urgency to the case priority level
- Reference specific booking/case details to show attentiveness
- Offer concrete solutions or next steps
- Acknowledge customer loyalty points or booking history when relevant
"""

# --- Create the Agent ---
travel_agent = Agent(
    models=["gemini-3.1-flash-lite-preview"],
    tool_declarations=[query_db_declaration],
    tool_implementations={"query_db": query_db_tool},
    system_instruction=system_instruction,
)

# --- Flask app ---
app = Flask(__name__)
CORS(app)


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' in request body"}), 400

    message = data["message"].strip()
    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    session_id = data.get("session_id")

    if session_id:
        existing_session = get_chat_session(session_id)
        if existing_session:
            chat_history = existing_session.get("messages", [])
            current_title = existing_session.get("title", "")
        else:
            chat_history = []
            current_title = ""
    else:
        session_id = str(uuid.uuid4())
        chat_history = []
        current_title = ""

    try:
        response_text, updated_history = travel_agent.call_with_history(
            prompt=message,
            chat_history=chat_history,
        )

        # Convert Content objects back to dict format for storage
        messages_to_save = []
        for msg in updated_history:
            if hasattr(msg, "role") and hasattr(msg, "parts"):
                # It's a types.Content object
                text = msg.parts[0].text if msg.parts and msg.parts[0].text else ""
                # Map "model" to "assistant" for frontend compatibility
                role = "assistant" if msg.role == "model" else msg.role
                if text:  # Only save non-empty messages
                    messages_to_save.append({"role": role, "text": text})
            else:
                # It's already a dict - also map model to assistant
                msg_role = msg.get("role", "user")
                role = "assistant" if msg_role == "model" else msg_role
                msg_text = msg.get("text", "") or ""
                if msg_text:  # Only save non-empty messages
                    messages_to_save.append({"role": role, "text": msg_text})

        if not current_title:
            title = f"Conversation - {message[:30]}..."
            if len(message) > 30:
                title += "..."
        else:
            title = current_title

        save_chat_session(session_id, title, messages_to_save)

        return jsonify(
            {
                "response": response_text,
                "session_id": session_id,
            }
        )
    except Exception as e:
        return jsonify({"error": f"Agent error: {str(e)}"}), 500


@app.route("/api/sessions", methods=["GET"])
def list_sessions():
    sessions = get_all_chat_sessions()
    return jsonify({"sessions": sessions})


@app.route("/api/sessions/<session_id>", methods=["GET"])
def get_session(session_id):
    session = get_chat_session(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404
    return jsonify(session)


@app.route("/api/sessions/<session_id>", methods=["DELETE"])
def delete_session(session_id):
    deleted = delete_chat_session(session_id)
    if not deleted:
        return jsonify({"error": "Session not found"}), 404
    return jsonify({"status": "deleted"})


@app.route("/api/sessions/<session_id>/rename", methods=["POST"])
def rename_session(session_id):
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' in request body"}), 400

    new_title = data["title"].strip()
    if not new_title:
        return jsonify({"error": "Title cannot be empty"}), 400

    updated = rename_chat_session(session_id, new_title)
    if not updated:
        return jsonify({"error": "Session not found"}), 404
    return jsonify({"status": "renamed", "title": new_title})


@app.route("/api/session/<session_id>", methods=["DELETE"])
def clear_session(session_id):
    deleted = delete_chat_session(session_id)
    return jsonify({"status": "cleared"})


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
