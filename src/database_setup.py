import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("comps.db") 
print("Successfully connected to the database")

# Create cursor
c1 = conn.cursor()

# Create tables
# Table for computer parts details
c1.execute('''
    CREATE TABLE IF NOT EXISTS comp_parts_details (
        Sno INTEGER PRIMARY KEY AUTOINCREMENT,
        computerpart TEXT NOT NULL,
        qtyavailable INTEGER NOT NULL,
        price_inclusiveoftax INTEGER NOT NULL
    )
''')

# Insert records into `comp_parts_details`
c1.execute("INSERT INTO comp_parts_details (computerpart, qtyavailable, price_inclusiveoftax) VALUES ('Keyboard', 89, 1300)")
c1.execute("INSERT INTO comp_parts_details (computerpart, qtyavailable, price_inclusiveoftax) VALUES ('Mouse', 69, 300)")
c1.execute("INSERT INTO comp_parts_details (computerpart, qtyavailable, price_inclusiveoftax) VALUES ('CPU', 71, 45300)")
# Add additional items as needed...
conn.commit()
print("Table 'comp_parts_details' created and populated.")

# Table for purchase records
c1.execute('''
    CREATE TABLE IF NOT EXISTS buy_comp_parts (
        customername TEXT NOT NULL,
        phoneno INTEGER NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        computerpart TEXT NOT NULL
    )
''')
print("Table 'buy_comp_parts' created.")

# Table for service requests
c1.execute('''
    CREATE TABLE IF NOT EXISTS compservice (
        customername TEXT NOT NULL,
        phoneno INTEGER NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        service TEXT NOT NULL
    )
''')
print("Table 'compservice' created.")

# Additional tables for feedback and complaints
c1.execute('''
    CREATE TABLE IF NOT EXISTS ratingsandcomment (
        phoneno INTEGER NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        rating INTEGER NOT NULL,
        comment TEXT
    )
''')
print("Table 'ratingsandcomment' created.")

c1.execute('''
    CREATE TABLE IF NOT EXISTS sales_prob (
        cus_name TEXT NOT NULL,
        phno1 INTEGER NOT NULL,
        sa_name TEXT NOT NULL,
        prob TEXT NOT NULL
    )
''')
print("Table 'sales_prob' created.")

c1.execute('''
    CREATE TABLE IF NOT EXISTS servive_prob (
        cus_name TEXT NOT NULL,
        phno INTEGER NOT NULL,
        se_name TEXT NOT NULL,
        prob TEXT NOT NULL
    )
''')
print("Table 'servive_prob' created.")

c1.execute('''
    CREATE TABLE IF NOT EXISTS sb_prob (
        cus_name TEXT NOT NULL,
        phno1 INTEGER NOT NULL,
        name1 TEXT NOT NULL,
        prob TEXT NOT NULL
    )
''')
print("Table 'sb_prob' created.")

# Commit changes and close connection
conn.commit()
conn.close()
