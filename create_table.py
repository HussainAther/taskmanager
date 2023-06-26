import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create a table for storing tasks
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        due_date TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Save the changes and close the connection
conn.commit()
conn.close()

