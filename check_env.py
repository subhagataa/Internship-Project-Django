import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print("=== Checking Environment Variables ===")
print(f"SECRET_KEY: {os.getenv('SECRET_KEY')}")
print(f"DB_HOST: {os.getenv('SUPABASE_DB_HOST')}")
print(f"DB_USER: {os.getenv('SUPABASE_DB_USER')}")
print(f"DB_NAME: {os.getenv('SUPABASE_DB_NAME')}")

# Test if we can read the password (show first few characters for security)
db_password = os.getenv('SUPABASE_DB_PASSWORD')
if db_password:
    print(f"DB_PASSWORD: {db_password[:4]}... (length: {len(db_password)})")
else:
    print("DB_PASSWORD: Not found")

print("=== Environment Check Complete ===")