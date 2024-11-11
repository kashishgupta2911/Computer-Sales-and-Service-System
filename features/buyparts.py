import mysql.connector as sql

# Connect to the database
conn = sql.connect(host="localhost", user="root", passwd="root1234", database="kashishg")
if conn.is_connected():
    print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Function to handle part purchases
def buy_part():
    print('---COMPUTER SALES---')
    customername = input('Please enter your name: ')
    phoneno = int(input('Please enter your phone number: '))
    email = input('Please enter your e-mail ID: ')
    address = input('Please enter your address: ')
    computerpart = input('Please enter the type of computer part you need: ')
    
    # Insert purchase details into table
    insert_query = f'''
    INSERT INTO buy_comp_parts (customername, phoneno, email, address, computerpart)
    VALUES ('{customername}', {phoneno}, '{email}', '{address}', '{computerpart}')
    '''
    c1.execute(insert_query)
    conn.commit()
    print(f"Thank you, {customername}. Your computer part will be delivered shortly.")

# Call the function to simulate buying a part
buy_part()

# Close the connection
conn.close()
