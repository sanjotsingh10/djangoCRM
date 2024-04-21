import mysql.connector


# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass"
)

# Create a cursor
mycursor = mydb.cursor()

# Execute the CREATE DATABASE statement
mycursor.execute("CREATE DATABASE mydatabase")

# Print a success message
print("Database 'mydatabase' created successfully.")
