from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("What is the capital of India?")
#or
response = model.invoke("What is the capital of India?")

print(response.text)
