import mysql.connector as sql

# Connect to the database
conn = sql.connect(host="localhost", user="root", passwd="root1234", database="kashishg")
if conn.is_connected():
    print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Function to record feedback
def feedback():
    phoneno = int(input("Please enter your phone number: "))
    email = input("Please enter your e-mail ID: ")
    address = input("Please enter your address: ")
    rating = int(input("Please enter your rating (out of 10): "))
    comment = input("Please leave a comment: ")

    # Insert feedback into table
    insert_query = f'''
    INSERT INTO ratingsandcomment (phoneno, email, address, rating, comment)
    VALUES ({phoneno}, '{email}', '{address}', {rating}, '{comment}')
    '''
    c1.execute(insert_query)
    conn.commit()
    print("Thank you for your feedback!")

# Call the function to record feedback
feedback()

# Close the connection
conn.close()
