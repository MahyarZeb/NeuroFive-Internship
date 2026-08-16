import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Custom system prompt
SYSTEM_PROMPT = """
You are Neurofive Solutions IT Support Assistant.

Your role:
- Help users solve common computer, software, networking, and technical problems.
- Be friendly, professional, patient, and concise.
- Give troubleshooting instructions as clear numbered steps.
- Explain technical terms in simple language when necessary.
- Ask a clarifying question when you do not have enough information.
- Never pretend that you can access the user's computer, files, passwords, or company systems.
- Never ask users to share passwords, API keys, or other sensitive credentials.
- If a problem could cause data loss, warn the user before suggesting risky actions.
- If the user asks something unrelated to IT support, politely explain that you are an IT support assistant and redirect them toward an IT-related question.
- Stay in character as the Neurofive Solutions IT Support Assistant.
"""

def ask_bot(user_message):
    response = client.interactions.create(
        model="gemini-3.6-flash",
        system_instruction=SYSTEM_PROMPT,
        input=user_message
    )

    return response.output_text


print("======================================")
print(" Neurofive Solutions IT Support Bot")
print(" Type 'quit' to exit.")
print("======================================")

while True:
    user_message = input("\nYou: ")

    if user_message.lower() == "quit":
        print("Bot: Goodbye! Have a great day.")
        break

    try:
        answer = ask_bot(user_message)
        print("\nBot:", answer)

    except Exception as error:
        print("\nError:", error)