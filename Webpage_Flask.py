from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# RDS configuration
db_config = {
    'host': 'employee-db.xxxxx.us-east-1.rds.amazonaws.com',  # Replace with your RDS endpoint
    'user': 'admin',
    'password': 'MySecurePass123',  # Replace with your RDS password
    'database': 'employees'
}

# Function to connect to RDS
def connect_db():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Home route - Display employees and add new employee
@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST' and 'add' in request.form:
        id_val = request.form['id']
        name_val = request.form['name']
        age_val = request.form['age']
        role_val = request.form['role']
        connection = connect_db()
        if connection:
            cursor = connection.cursor()
            try:
                sql = "INSERT INTO empdata (id, name, age, role) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (id_val, name_val, age_val, role_val))
                connection.commit()
                message = "Employee added successfully!"
            except Error as e:
                message = f"Error: {e}"
            finally:
                cursor.close()
                connection.close()

    # Fetch all employees
    connection = connect_db()
    employees = []
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM empdata")
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
    
    return render_template('index.html', employees=employees, message=message)

# Delete employee
@app.route('/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            sql = "DELETE FROM empdata WHERE id = %s"
            cursor.execute(sql, (id,))
            connection.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

# Update employee - Display update form
@app.route('/update/<int:id>', methods=['GET'])
def update_employee_form(id):
    connection = connect_db()
    employee = None
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM empdata WHERE id = %s", (id,))
        employee = cursor.fetchone()
        cursor.close()
        connection.close()
    return render_template('update.html', employee=employee)

# Update employee - Process update
@app.route('/update/<int:id>', methods=['POST'])
def update_employee(id):
    name_val = request.form['name']
    age_val = request.form['age']
    role_val = request.form['role']
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            sql = "UPDATE empdata SET name = %s, age = %s, role = %s WHERE id = %s"
            cursor.execute(sql, (name_val, age_val, role_val, id))
            connection.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)