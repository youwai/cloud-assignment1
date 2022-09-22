from pymysql import connections
from config import *

db_conn = connections.Connection(
    host = customhost,
    port = 3306,
    user = customuser,
    password= custompass,
)

cursor = db_conn.cursor()

create_db = "CREATE DATABASE HRSystem"
cursor.execute(create_db)
print('Created Database.')
cursor.execute("USE HRSystem")

create_table = "CREATE TABLE Employees (emp_id varchar(10), name varchar(100), ic_no varchar(50), gender varchar(10), dob Date, age int(2), position varchar(50), department varchar(20), salary double(10,2), created_date Date, url varchar(100), primary key (emp_id))"

cursor.execute(create_table)
print('Created table.')
db_conn.commit()