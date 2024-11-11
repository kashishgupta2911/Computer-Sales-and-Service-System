import mysql.connector as sql

# Connect to the database
conn = sql.connect(host="localhost", user="root", passwd="root1234", database="kashishg")
if conn.is_connected():
    print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Function to display available computer parts
def view_parts():
    print('---COMPUTER PARTS DETAILS---')
    c1.execute('SELECT * FROM comp_parts_details')
    details = c1.fetchall()
    for part in details:
        print(part)

# Call the function to display parts
view_parts()

# Close the connection
conn.close()
