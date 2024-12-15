'''
    create 2 tables :employess and projects
        - project had fields: project_id,project_name,employee_id
        - write a sccript to fetch all project names along with employee 
          names working on them

'''
import psycopg2
from psycopg2 import OperationalError
def fetch_project_details():
    try:
        db_con=psycopg2.connect(
            dbname="employee",
            user="postgres",
            password="aprameya2003",
            host="localhost",
            port="5432"
        )
        print('Connection successful\n')
        query="""
            select p.project_name,e.name as employee_name
            from projects p join employees e on p.emp_id=e.id;
        """
        cursor=db_con.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(f'Project: {row[0]}, EmployeeName: {row[1]}')
        cursor.close()
        db_con.close()
    except OperationalError as e:
        print(f'Error: {e}')
fetch_project_details()