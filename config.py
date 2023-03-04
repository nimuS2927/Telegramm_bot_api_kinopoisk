import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")
TOKEN_API = os.getenv("TOKEN_API")
