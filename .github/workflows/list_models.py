from google import genai
import os

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

print("Modeller du kan använda:")
for model in client.models.list():
    if 'generateContent' in model.supported_methods:
        print(f"- {model.name}")
