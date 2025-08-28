from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

with open("", "rb") as f:
    image_bytes = f.read()
    
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Describe this image for me", image]
)

print(response.text)