from google import genai
from google.genai import types
from typing import Optional, List, Dict, Callable

class Agent:
    """
    Reusable AI agent class for industry-specific assistants.

    Args:
        models: List of model names to use (defaults to gemini-2.5-flash)
        tool_declarations: List of tool/function declarations for the agent
        tool_implementations: Dict mapping tool names to their implementation functions
        system_instruction: System prompt defining agent behavior
    """

    def __init__(
        self,
        models: Optional[List[str]] = None,
        tool_declarations: Optional[List[Dict]] = None,
        tool_implementations: Optional[Dict[str, Callable]] = None,
        system_instruction: str = ""
    ):
        self.client = genai.Client()

        # Set default model if none provided
        if models is None or len(models) == 0:
            models = ["gemini-2.5-flash"]
        self.models = models

        # Set up tools
        self.tool_declarations = tool_declarations or []
        self.tool_implementations = tool_implementations or {}

        # Create Tool object if tools are provided
        tools = None
        if self.tool_declarations:
            tools = [types.Tool(function_declarations=self.tool_declarations)]

        # Create config
        self.config = types.GenerateContentConfig(
            tools=tools,
            system_instruction=system_instruction
        )

        # Store system instruction for reference
        self.system_instruction = system_instruction

    def call(self, prompt: str, chat_history: Optional[List] = None) -> str:
        """
        Call the agent with a prompt and optional chat history.

        Args:
            prompt: User's message/query
            chat_history: Previous conversation history (list of Content objects)

        Returns:
            Agent's response as a string
        """
        try:
            # Build contents - start with chat history if provided
            contents = []
            if chat_history:
                contents.extend(chat_history)

            # Add current user prompt
            contents.append(
                types.Content(
                    role="user",
                    parts=[types.Part(text=prompt)]
                )
            )

            # Make initial API call
            response = self.client.models.generate_content(
                model=self.models[0],
                contents=contents,
                config=self.config
            )

            # Check if the model wants to call a tool/function
            if response.candidates[0].content.parts[0].function_call:
                tool_call = response.candidates[0].content.parts[0].function_call

                # Execute the tool if we have an implementation
                if tool_call.name in self.tool_implementations:
                    result = self.tool_implementations[tool_call.name](tool_call.args)

                    # Create function response part
                    function_response_part = types.Part.from_function_response(
                        name=tool_call.name,
                        response={"result": result},
                    )

                    # Append model's response and function result to contents
                    contents.append(response.candidates[0].content)
                    contents.append(types.Content(role="user", parts=[function_response_part]))

                    # Make second API call with function results
                    final_response = self.client.models.generate_content(
                        model=self.models[0],
                        config=self.config,
                        contents=contents,
                    )

                    return final_response.candidates[0].content.parts[0].text
                else:
                    return f"Error: Tool '{tool_call.name}' not implemented"

            # No tool call - return direct response
            return response.candidates[0].content.parts[0].text

        except Exception as e:
            return f"Error calling agent: {str(e)}"

    def call_with_history(self, prompt: str, chat_history: Optional[List] = None) -> tuple:
        """
        Call the agent and return both response and updated chat history.

        Args:
            prompt: User's message/query
            chat_history: Previous conversation history

        Returns:
            Tuple of (response_text, updated_chat_history)
        """
        # Initialize chat history if not provided
        if chat_history is None:
            chat_history = []

        # Add user message to history
        chat_history.append(
            types.Content(
                role="user",
                parts=[types.Part(text=prompt)]
            )
        )

        # Get response
        response = self.call(prompt, chat_history[:-1])  # Pass history without the current prompt

        # Add agent response to history
        chat_history.append(
            types.Content(
                role="model",
                parts=[types.Part(text=response)]
            )
        )

        return response, chat_history