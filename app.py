from flask import Flask, render_template, request
from pymysql import connections

app = Flask(__name__)

db_conn = connections.Connection(
    host = 'hr-db1.cwrevot9vajh.us-east-1.rds.amazonaws.com',
    port = 3306,
    user = 'admin',
    password= 'hrdb12345'
)

@app.route("/")
def index():
    cursor = db_conn.cursor()
    create_table = "CREATE TABLE Employees (emp_id varchar(10), name varchar(100), ic_no varchar(50), gender varchar(10), dob Date, age int(2), position varchar(50), department varchar(20), salary double(10,2), created_date Date, primary key (emp_id))"

    cursor.execute(create_table)
    cursor.commit()
    print('Created table')

    cursor.execute("Select * from Employees")
    result = cursor.fetchall()
    print(result)
    print("attempt to fetch data")

    return render_template('index.html')

@app.route("/employee_list")
def employee_list():
    data = [{'emp_id': '0001', 'name': 'You Wai', 'date': '31-MAY-2022'}, {'emp_id': '0002', 'name': 'You Wai', 'date': '31-MAY-2022'}]

    return render_template('employee_list.html', data=data)
    
@app.route("/insert", methods=['post'])
def insert():
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        name = request.form['name']
        ic_no = request.form['ic_no']
        gender = request.form['gender']
        dob = request.form['dob']
        age = request.form['age']
        position = request.form['position']
        department = request.form['department']
        salary = request.form['salary']
        image = request.form['image']

        data = {
            'emp_id': emp_id,
            'name': name,
            'ic_no':ic_no,
            'gender': gender,
            'dob': dob,
            'age': age,
            'position': position,
            'department': department,
            'salary': salary,
            'image': image
        }

    return render_template('employee_list.html')

@app.route('/emp_details')
@app.route('/emp_details/<emp_id>')
def emp_details(emp_id = None):
    return render_template('employee_details.html', emp_id=emp_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)