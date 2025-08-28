from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents="Why is the sky blue"
)

for stream in response:
    print(stream.text)