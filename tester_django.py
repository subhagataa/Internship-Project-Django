import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_app.settings')
django.setup()

from django.db import connection

def test_django_pooler():
    try:
        connection.ensure_connection()
        print("✅ Django connection pooler connection successful!")
        
        # Test if we can execute queries
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Query test successful: {result}")
            
        return True
    except Exception as e:
        print(f"❌ Django connection failed: {e}")
        return False

if __name__ == "__main__":
    test_django_pooler()