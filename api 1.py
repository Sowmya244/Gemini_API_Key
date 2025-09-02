from google import genai
import re

genai_client = genai.Client(api_key="AIzaSyANGD69ceqW88bDqqyKNx5i-nUOOfYIN6w")
chat = genai_client.chats.create(model="gemini-2.5-flash")

print("Gemini Chatbot 🤖 (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nChatbot: Goodbye!")
        break
    response = chat.send_message(user_input)
    clean_text = re.sub(r'[\$*]', '', response.text).strip()
    print("\nChatbot:", clean_text, "\n")
