from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

upload_file = client.files.upload(file="") # .mp3, .jpg, .mp4, .pdf...

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Describe this image for me", upload_file]
)

print(response.text)