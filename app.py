from flask import Flask, render_template, request
from pymysql import connections
import boto3
from datetime import date

app = Flask(__name__)

db_conn = connections.Connection(
    host = 'hr-db1.cwrevot9vajh.us-east-1.rds.amazonaws.com',
    port = 3306,
    user = 'admin',
    password= 'hrdb12345',
    db = 'HRSystem'
)

custombucket = 'jasonsorkeanyung-bucket'
customregion = 'us-east-1'

# cursor = db_conn.cursor()
# cursor.execute("USE HRSystem")

# create_table = "CREATE TABLE Employees (emp_id varchar(10), name varchar(100), ic_no varchar(50), gender varchar(10), dob Date, age int(2), position varchar(50), department varchar(20), salary double(10,2), created_date Date, primary key (emp_id))"

# cursor.execute(create_table)
# print('Created table')
# db_conn.commit()

def read_data_from_rds (emp_id = None):
    cursor = db_conn.cursor()

    if emp_id == None:
        cursor.execute("Select * from Employees")
    else:
        cursor.execute("Select * from Employees where emp_id = %s", (emp_id))

    records = cursor.fetchall()
    print(records)
    print("attempt to fetch data")

    result = []

    for record in records:
        temp = {
            'emp_id': record[0],
            'name': record[1],
            'ic_no': record[2],
            'gender': record[3],
            'dob': record[4],
            'age': record[5],
            'position': record[6],
            'department': record[7],
            'salary': record[8],
            'created_date': record[9]
        }

        result.append(temp)

    return result


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/employee_list")
def employee_list():
    data = read_data_from_rds()

    return render_template('employee_list.html', data=data)
    
@app.route("/insert", methods=['post'])
def insert():
    today = date.today()

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
        emp_image = request.files['emp_image']

        print(emp_image)

        if emp_image.filename == "":
            return "Please select a file"

        try:
            cursor = db_conn.cursor()
            # insert_sql = "INSERT INTO Employees VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            # cursor.execute(insert_sql, (emp_id, name, ic_no, gender, dob, age, position, department, salary, today))
            # db_conn.commit()

            emp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file"
            s3 = boto3.resource('s3')

            try:
                print("Data inserted in MySQL RDS... uploading imag eto S3...")
                s3.Bucket(custombucket).put_object(Key=emp_image_file_name_in_s3, Body=emp_image)
                bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
                s3_location = (bucket_location['LocationConstraint'])

                if s3_location is None:
                    s3_location = ''
                else:
                    s3_location = '-' + s3_location

                object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                    s3_location,
                    custombucket,
                    emp_image_file_name_in_s3)


            except Exception as e:
                return str(e)

        finally:
            cursor.close()

        print(object_url)

        data = read_data_from_rds()

    return render_template('employee_list.html', data = data)

@app.route('/emp_details')
@app.route('/emp_details/<emp_id>')
def emp_details(emp_id = None):
    data = read_data_from_rds(emp_id)

    result = data[0]

    return render_template('employee_details.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)