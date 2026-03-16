# imports
from google import genai
from google.genai import types
from dotenv import load_dotenv
import datetime
import sys
from db import generate_db, delete_db, query_db

schema = open("./sample_datasets/travel_company_customer_db/schema.sql", "r").read()

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

def call_gemini_api(user_query):
    """
    Try/Except:
    This is what we call 'error handling' - it is a way to deal with errors without crashing the program.
    Basically, whatever happens in the 'try' block runs, and if something goes wrong, 
    it skips right to the 'except' block.
    """

    # This calls the Gemini API
    try:
        client = genai.Client() #The API key located in the env file is found and automatically used
        tools = types.Tool(function_declarations=[query_db_declaration])
        
        # Add system instructions here
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
        
        config = types.GenerateContentConfig(
            tools=[tools],
            system_instruction=system_instruction
        )
        contents = [
            types.Content(
                role="user", parts=[types.Part(text=user_query)]
            )
        ]
        response = client.models.generate_content(
            model="gemini-3.1-flash-preview",
            contents=contents,
            config=config
        )

        if response.candidates[0].content.parts[0].function_call:
            tool_call = response.candidates[0].content.parts[0].function_call
            if tool_call.name == "query_db":
                result = query_db(tool_call.args['sqlite3_query'])
                print(f"TOOL CALL: {tool_call}")

            function_response_part = types.Part.from_function_response(
                name=tool_call.name,
                response={"result": result},
            )

            contents.append(response.candidates[0].content) # Append the content from the model's response.
            contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

            client = genai.Client()
            final_response = client.models.generate_content(
                # model="gemini-2.5-flash",
                model="gemma-3-27b",
                config=config,
                contents=contents,
            )
            return(final_response.candidates[0].content.parts[0].text)
        # return(final_response.text)
        return response.candidates[0].content.parts[0].text
    except Exception as e:
        print(e)

def main():
    """
    We do NOT want to place the API key in the code.  Leaving it in the code allows others to view the key.
    And if you're paying for that API key, and the cost increases based on usage - well, that won't be fun for you.
    Instead, it's placed in the environment, or a dotfile.  Dotfiles are hidden by default.
    We use a '.env' file to store configuration settings, environment variables etc.
    Basically, this is sensitive information, securely.
    """
try:
    load_dotenv() #This loads the .env file
except Exception as e:
    print(e)

print("Generating Mock Travel Company Customer Data...")
generate_db("./sample_datasets/travel_company_customer_db/travel_company.db")
chats = []
print("Hi! How can I help today?")
user_query = ""
while user_query != "exit":
    user_query = input()
    if user_query == "exit":
        print("Goodbye!")
        sys.exit()
    else:
        print("Thinking...")
    chats.append(f"🧑 User: {user_query}\n")
    response = call_gemini_api("".join(chats) + user_query)
    print(f"� Agent: {response}")
    chats.append(f"🤖 Agent: {response}\n")

with open(f"./chat_logs/{datetime.datetime.now()}", "a") as f:
    f.write("".join(chats))

if __name__ == "__main__":
    main()
