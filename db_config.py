import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # Load values from .env file

# Debugging output
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "policiease"),
        cursorclass=pymysql.cursors.DictCursor
    )
