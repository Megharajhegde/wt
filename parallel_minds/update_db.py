import sqlite3
import os

# Updated to match the exact database name in your config.py
DB_PATH = 'library.db' 

def upgrade_database():
    conn = None # Initializes the variable to prevent the UnboundLocalError
    try:
        # Connect directly to your specific SQLite file
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Add the new column and default everyone to 'student'
        cursor.execute("ALTER TABLE users ADD COLUMN role VARCHAR(20) DEFAULT 'student'")
        conn.commit()
        
        print("✅ Success! The 'role' column was added.")
        print("All existing users are now officially 'students'.")
        
    except sqlite3.OperationalError as e:
        print(f"⚠️ Notice: {e}")
        print("If it says 'duplicate column name', the update already worked!")
    finally:
        # Safely checks if the connection actually opened before trying to close it
        if conn:
            conn.close()

if __name__ == '__main__':
    upgrade_database()