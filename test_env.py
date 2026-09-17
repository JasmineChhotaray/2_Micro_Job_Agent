# Make sure my Python interpreter & Groq API Key are communicating perfectly.
import os
from dotenv import load_dotenv


# Load the keys from .env file in this exact directory
load_dotenv()

key = os.getenv("GROQ_API_KEY")

if key and key.startswith("gsk_"):
    print("Success! Env is Set Up & Groy key is loaded properly.")
else:
    print("Error! Could not find or read Groq API Key. Check .env file.")