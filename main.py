import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) == 1:
    print("Please provide a prompt.")
    sys.exit(1)

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
)

if response.function_calls:
    for function_call_part in response.function_calls:       
        result = call_function(function_call_part, verbose={"--verbose" in sys.argv})

        if not result.parts[0].function_response.response:
            raise RuntimeError("Fatal error occured")
        else:
            if "--verbose" in sys.argv:
                print(f"-> {result.parts[0].function_response.response}")
else:
    print(response.text)