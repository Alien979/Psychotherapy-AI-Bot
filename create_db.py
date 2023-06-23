import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('C:\\Users\\User\\Desktop\\language\\EDITH_MENTAL_HEALTH\\database.db')

# Create a new table
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS test_table (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Commit the transaction and close the connection
conn.commit()
conn.close()







