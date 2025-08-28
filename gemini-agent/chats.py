from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

chat = client.chats.create(model="gemini-2.0-flash")

while True:
    message = input("> ")
    if message == "exit":
        break
    
    res = chat.send_message_stream(message)
    
    for chunk in res:   # stream ke andar har chunk aata hai
        if chunk.text:
            print(chunk.text, end="", flush=True)  # token by token print karo
    print()  # new line after full response
