import sqlite3

# Connect to the database
conn = sqlite3.connect("comps.db")  # Create or connect to the SQLite database file comps.db
print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Ensure the table exists
c1.execute('''
CREATE TABLE IF NOT EXISTS buy_comp_parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customername TEXT NOT NULL,
    phoneno INTEGER NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    computerpart TEXT NOT NULL
)
''')

# Function to handle part purchases
def buy_part():
    print('---COMPUTER SALES---')
    customername = input('Please enter your name: ')
    phoneno = int(input('Please enter your phone number: '))
    email = input('Please enter your e-mail ID: ')
    address = input('Please enter your address: ')
    computerpart = input('Please enter the type of computer part you need: ')
    
    # Insert purchase details into table using a parameterized query
    insert_query = '''
    INSERT INTO buy_comp_parts (customername, phoneno, email, address, computerpart)
    VALUES (?, ?, ?, ?, ?)
    '''
    c1.execute(insert_query, (customername, phoneno, email, address, computerpart))
    conn.commit()
    print(f"Thank you, {customername}. Your computer part will be delivered shortly.")

# Call the function to simulate buying a part
buy_part()

# Close the connection
conn.close()
