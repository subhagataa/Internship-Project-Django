import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def test_pooler_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('SUPABASE_DB_HOST'),
            database=os.getenv('SUPABASE_DB_NAME'),
            user=os.getenv('SUPABASE_DB_USER'),
            password=os.getenv('SUPABASE_DB_PASSWORD'),
            port=os.getenv('SUPABASE_DB_PORT'),
            sslmode='require'
        )
        print("✅ Connection pooler connection successful!")
        
        # Test a simple query
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print(f"✅ Database version: {version[0]}")
        
        cur.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Connection pooler connection failed: {e}")
        return False

if __name__ == "__main__":
    test_pooler_connection()