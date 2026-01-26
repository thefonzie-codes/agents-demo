import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from ai.agent import Agent
from db import generate_db, query_db

load_dotenv()

# --- Database setup ---
DB_PATH = "./sample_datasets/travel_company_customer_db/travel_company.db"
SCHEMA_PATH = "./sample_datasets/travel_company_customer_db/schema.sql"

print("Generating Mock Travel Company Customer Data...")
generate_db(DB_PATH)

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
    models=["gemini-2.5-flash"],
    tool_declarations=[query_db_declaration],
    tool_implementations={"query_db": query_db_tool},
    system_instruction=system_instruction,
)

# --- Session store: session_id -> chat_history (list of Gemini Content objects) ---
sessions: dict[str, list] = {}

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
    if not session_id or session_id not in sessions:
        session_id = str(uuid.uuid4())
        sessions[session_id] = []

    chat_history = sessions[session_id]

    try:
        response_text, updated_history = travel_agent.call_with_history(
            prompt=message,
            chat_history=chat_history,
        )
        sessions[session_id] = updated_history

        return jsonify({
            "response": response_text,
            "session_id": session_id,
        })
    except Exception as e:
        return jsonify({"error": f"Agent error: {str(e)}"}), 500


@app.route("/api/session/<session_id>", methods=["DELETE"])
def clear_session(session_id):
    if session_id in sessions:
        del sessions[session_id]
    return jsonify({"status": "cleared"})


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
