import psycopg2
from psycopg2 import OperationalError
def create_connection():
    try:
        connection=psycopg2.connect(
            dbname="emp",
            user="postgres",
            password="aprameya2003",
            host="localhost",
            port="5432"
        )
        cursor=connection.cursor()
        print("successfully connected")
    except OperationalError as e:
        print('Error:not establish the connection')
create_connection()