import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load GEMINI_API_KEY from .env
genai.configure(api_key=os.getenv("AIzaSyDax0EQ0l2yuN8-B5-P2NVk4pLwiyCwI58"))

# List all available models and their methods
models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)
