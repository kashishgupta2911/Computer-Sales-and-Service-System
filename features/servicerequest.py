import mysql.connector as sql

# Connect to the database
conn = sql.connect(host="localhost", user="root", passwd="root1234", database="kashishg")
if conn.is_connected():
    print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Function to handle service requests
def request_service():
    print('---COMPUTER SERVICE---')
    customername = input('Please enter your name: ')
    phoneno = int(input('Please enter your phone number: '))
    email = input('Please enter your e-mail ID: ')
    address = input('Please enter your address: ')
    service = input('Please enter the service you need: ')
    
    # Insert service request into table
    insert_query = f'''
    INSERT INTO compservice (customername, phoneno, email, address, service)
    VALUES ('{customername}', {phoneno}, '{email}', '{address}', '{service}')
    '''
    c1.execute(insert_query)
    conn.commit()
    print(f"Thank you, {customername}. Your service request has been recorded.")

# Call the function to simulate a service request
request_service()

# Close the connection
conn.close()
