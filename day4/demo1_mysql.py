import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",         # Replace with your MySQL server hostname
            database="emp",           # Replace with your database name
            user="root",              # Replace with your MySQL username
            password="aprameya@2003"    # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            
            # Create a cursor
            cursor = connection.cursor()
            # Example: Check the MySQL server version
            cursor.execute("SELECT * from employee;")
            version = cursor.fetchone()
            print(f"MySQL Server Version: {version[0]}")
            
    except Error as e:
        print(f"Error: Unable to establish the connection. Details: {e}")
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function to test the connection
create_connection()
