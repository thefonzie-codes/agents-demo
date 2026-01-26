"""
Example demonstrating how to use the new Agent class with the travel agent.
This shows how to refactor main.py to use the Agent factory pattern.
"""

from ai.agent import Agent
from db import generate_db, query_db
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load schema
schema = open("./sample_datasets/travel_company_customer_db/schema.sql", "r").read()

# Define tool declaration
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

# Define tool implementation wrapper
def query_db_tool(args):
    """Wrapper for query_db that accepts args dict from Gemini."""
    return query_db(args['sqlite3_query'])

# System instruction
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

# Generate database
print("Generating Mock Travel Company Customer Data...")
generate_db("./sample_datasets/travel_company_customer_db/travel_company.db")

# Create the agent
travel_agent = Agent(
    models=["gemini-2.5-flash"],
    tool_declarations=[query_db_declaration],
    tool_implementations={"query_db": query_db_tool},
    system_instruction=system_instruction
)

# Example usage
if __name__ == "__main__":
    print("\n" + "="*60)
    print("Travel Agent - Example Usage")
    print("="*60 + "\n")

    # Example 1: Simple query without history
    print("Example 1: Simple query")
    print("-" * 40)
    query1 = "How many customers do we have in total?"
    print(f"User: {query1}")
    response1 = travel_agent.call(query1)
    print(f"Agent: {response1}\n")

    # Example 2: Using chat history
    print("Example 2: Conversation with history")
    print("-" * 40)
    chat_history = []

    query2 = "Find me a customer with email containing 'john'"
    print(f"User: {query2}")
    response2, chat_history = travel_agent.call_with_history(query2, chat_history)
    print(f"Agent: {response2}\n")

    query3 = "What bookings do they have?"
    print(f"User: {query3}")
    response3, chat_history = travel_agent.call_with_history(query3, chat_history)
    print(f"Agent: {response3}\n")

    query4 = "What are their loyalty points?"
    print(f"User: {query4}")
    response4, chat_history = travel_agent.call_with_history(query4, chat_history)
    print(f"Agent: {response4}\n")

    print("="*60)
    print("Example complete!")
    print("="*60)
