from pymysql import connections

db_conn = connections.Connection(
    host = 'hr-db1.cwrevot9vajh.us-east-1.rds.amazonaws.com',
    port = 3306,
    user = 'admin',
    password= 'hrdb12345'
)

cursor = db_conn.cursor()
create_table = "CREATE TABLE Employees (emp_id varchar(10), name varchar(100), ic_no varchar(50), gender varchar(10), dob Date, age int(2), position varchar(50), department varchar(20), salary double(10,2), created_date Date, primary key (emp_id))"

cursor.execute(create_table)
cursor.commit()
print('Created table')

cursor.execute("Select * from Employees")
result = cursor.fetchall()
print(result)
print("attempt to fetch data")