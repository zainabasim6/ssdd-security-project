import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT
)
''')

# Add some test data
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Alice', 'alice@test.com', 'pass123')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Bob', 'bob@test.com', 'pass456')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Charlie', 'charlie@test.com', 'pass789')")

conn.commit()
conn.close()
print("Database created with test data!")