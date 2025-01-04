import sqlite3

# Connect to the database
conn = sqlite3.connect("comps.db")  # Create or connect to the SQLite database file
print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Ensure the table exists
c1.execute('''
CREATE TABLE IF NOT EXISTS compservice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customername TEXT NOT NULL,
    phoneno INTEGER NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    service TEXT NOT NULL
)
''')

# Function to handle service requests
def request_service():
    print('---COMPUTER SERVICE---')
    customername = input('Please enter your name: ')
    phoneno = int(input('Please enter your phone number: '))
    email = input('Please enter your e-mail ID: ')
    address = input('Please enter your address: ')
    service = input('Please enter the service you need: ')
    
    # Insert service request into table using a parameterized query
    insert_query = '''
    INSERT INTO compservice (customername, phoneno, email, address, service)
    VALUES (?, ?, ?, ?, ?)
    '''
    c1.execute(insert_query, (customername, phoneno, email, address, service))
    conn.commit()
    print(f"Thank you, {customername}. Your service request has been recorded.")

# Call the function to simulate a service request
request_service()

# Close the connection
conn.close()
