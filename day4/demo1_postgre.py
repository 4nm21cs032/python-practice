import psycopg2 as psy
from psycopg2 import OperationalError
def create_connection():
    try:
        connection=psy.connect(
            dbname="emp",
            user="postgres",
            password="aprameya2003",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        print("Connection sucessful")
        # insert_query="""
        # INSERT INTO employee(ename, position, esalary) values(%s,%s,%s)
        # """
        # employee_data=[
        #     ("Swaroop","developer", 600000)
        # ]
        # cursor.executemany(insert_query, employee_data)
        # connection.commit()
        # print("Data inserted sucessfully")

        # update_query = """
        # UPDATE employee
        # SET esalary = %s
        # WHERE ename = %s
        # """
        # update_data = [
        #     (700000, "john")  
        # ]
        # cursor.executemany(update_query, update_data)
        # connection.commit()
        # print("Data updated successfully")

        # delete_query = """
        # DELETE FROM employee
        # WHERE ename = %s
        # """
        # delete_data = [
        #     ("Jack",)  
        # ]
        # cursor.executemany(delete_query, delete_data)
        # connection.commit()
        # print("Data deleted successfully")
    except OperationalError as e:
        print('Error:not establish the connection')
create_connection()

# def insert_employee():
#     connetion=create_connection():

# def count_rows():
#     connection = create_connection()
#     print("YES")
#     if connection:
#         print("YES")
#         cursor=connection.cursor()
#         cursor.execute("SELECT COUNT(*) FROM employee; ")
#         count=cursor.fetchone()[0]
#         print(f"Number of rows: {count}")
        # cursor.close()
        # connection.close()
# # count_rows()

# def fetch_col():
#     connection = create_connection()
#     if connection:
#         cursor=connection.cursor()
#         cursor.execute("SELECT ename, position FROM employee; ")
#         rows=cursor.fetchall()
#         print("Name| Department")
#         for row in rows:
#             print(f"{row[0]}|{row[1]}")
        # cursor.close()
        # connection.close()

# fetch_col()

# def fetch_on_cond():
#     connection = create_connection():

# def update_salary():
#     connection = create_connection()
#     if connection:
#         cursor=connection.cursor()
#         update_query="""
#         UPDATE employee
#         SET salary=salary+10000
#         WHERE position="Developer"
#         """
#         cursor.execute(update_query)
#         connection.commit()
#         print("Successfully updated")
#         cursor.close()
#         connection.close()

# update_salary()

def check_and_insert():
    connection = create_connection()
    if connection:
        cursor=connection.cursor()
        check_query="SELECT COUNT(*) FROM employee WHERE id =%s;"
        employee_id=1
        cursor.execute(check_query, employee_id)
        count=cursor.fetchone()[0]
        if count > 0:
            print(f"employee with id {employee_id} already exists")
        else:
            insert_query="INSERT INTO employee(ename, position, esalary) values(%s,%s,%s)"
            new_emp_data=('manu',"Developer",600000)
            cursor.execute(insert_query, new_emp_data)
            connection.commit()
            print("sucessfully data inserted")
        cursor.close()
        connection.close()
check_and_insert()