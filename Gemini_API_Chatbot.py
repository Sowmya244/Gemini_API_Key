from google import genai
from dotenv import load_dotenv
import os, re

load_dotenv("Gemini_API.env")
API_KEY = os.getenv("GENAI_API_KEY")

genai_client = genai.Client(api_key=API_KEY)
chat = genai_client.chats.create(model="gemini-2.5-flash")

print("Gemini Chatbot  (type 'exit' to quit)\n")

def clean_response(text):
    text = re.sub(r'[\$*]', '', text)
    text = text.replace("times", "*").replace("plus", "+").replace("minus", "-").replace("divided by", "/")
    return text.strip()

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nChatbot: Goodbye!")
        break
    response = chat.send_message(message=user_input)
    clean_text = clean_response(response.text)
    print("\nChatbot:", clean_text, "\n")
