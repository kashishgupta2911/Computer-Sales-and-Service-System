import mysql.connector as sql

# Connect to MySQL database
conn = sql.connect(host="localhost", user="root", passwd="root1234", database="kashishg")
if conn.is_connected():
    print('Successfully connected to the database')

# Create cursor
c1 = conn.cursor()

# Create tables
# Table for computer parts details
c1.execute('''
    CREATE TABLE IF NOT EXISTS comp_parts_details (
        Sno INT PRIMARY KEY,
        computerpart VARCHAR(100),
        qtyavailable INT,
        price_inclusiveoftax INT
    )
''')
c1.execute("INSERT INTO comp_parts_details VALUES (1, 'Keyboard', 89, 1300)")
c1.execute("INSERT INTO comp_parts_details VALUES (2, 'Mouse', 69, 300)")
c1.execute("INSERT INTO comp_parts_details VALUES (3, 'CPU', 71, 45300)")
# Add other items similarly...
conn.commit()
print("Table 'comp_parts_details' created and populated.")

# Table for purchase records
c1.execute('''
    CREATE TABLE IF NOT EXISTS buy_comp_parts (
        customername VARCHAR(100),
        phoneno BIGINT,
        email VARCHAR(100),
        address VARCHAR(100),
        computerpart VARCHAR(100)
    )
''')
print("Table 'buy_comp_parts' created.")

# Table for service requests
c1.execute('''
    CREATE TABLE IF NOT EXISTS compservice (
        customername VARCHAR(100),
        phoneno BIGINT,
        email VARCHAR(100),
        address VARCHAR(100),
        service VARCHAR(100)
    )
''')
print("Table 'compservice' created.")

# Additional tables for feedback and complaints
c1.execute('''
    CREATE TABLE IF NOT EXISTS ratingsandcomment (
        phoneno BIGINT,
        email VARCHAR(100),
        address VARCHAR(100),
        rating INT,
        comment VARCHAR(255)
    )
''')
print("Table 'ratingsandcomment' created.")

c1.execute('''
    CREATE TABLE IF NOT EXISTS sales_prob (
        cus_name VARCHAR(100),
        phno1 BIGINT,
        sa_name VARCHAR(100),
        prob VARCHAR(255)
    )
''')
print("Table 'sales_prob' created.")

c1.execute('''
    CREATE TABLE IF NOT EXISTS servive_prob (
        cus_name VARCHAR(100),
        phno BIGINT,
        se_name VARCHAR(100),
        prob VARCHAR(255)
    )
''')
print("Table 'servive_prob' created.")

c1.execute('''
    CREATE TABLE IF NOT EXISTS sb_prob (
        cus_name VARCHAR(100),
        phno1 BIGINT,
        name1 VARCHAR(100),
        prob VARCHAR(255)
    )
''')
print("Table 'sb_prob' created.")

# Commit changes and close connection
conn.commit()
conn.close()
