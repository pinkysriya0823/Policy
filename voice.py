from elevenlabs import set_api_key, voices
import os
from dotenv import load_dotenv
load_dotenv()

set_api_key(os.getenv("ELEVENLABS_API_KEY"))  # or paste your key directly here
print(voices())
