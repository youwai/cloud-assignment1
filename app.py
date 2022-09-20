from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
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
        ethnicity = request.form['ethnicity']
        address1 = request.form['address1']
        address2 = request.form['address2']
        postcode = request.form['postcode']
        state = request.form['state']
        country = request.form['country']
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
            'ethnicity': ethnicity,
            'address1': address1,
            'address2': address2,
            'postcode': postcode,
            'state': state,
            'country': country,
            'image': image
        }

    return render_template('employee_list.html')

@app.route('/emp_details')
@app.route('/emp_details/<emp_id>')
def emp_details(emp_id = None):
    return render_template('employee_details.html', emp_id=emp_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)