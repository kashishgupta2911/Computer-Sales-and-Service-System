import sqlite3

# Connect to the database
conn = sqlite3.connect("comps.db")  # Create or connect to the SQLite database file
print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Ensure the table exists (for demonstration, you may modify this as needed)
c1.execute('''
CREATE TABLE IF NOT EXISTS comp_parts_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_name TEXT NOT NULL,
    part_type TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

# Function to display available computer parts
def view_parts():
    print('---COMPUTER PARTS DETAILS---')
    c1.execute('SELECT * FROM comp_parts_details')
    details = c1.fetchall()
    if details:
        for part in details:
            print(part)
    else:
        print("No computer parts available.")

# Call the function to display parts
view_parts()

# Close the connection
conn.close()
