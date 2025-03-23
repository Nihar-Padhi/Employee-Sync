import customtkinter as ctk
import mysql.connector
from mysql.connector import Error

# Database configuration for AWS RDS
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
        print(f"Error connecting to RDS: {e}")
        return None

# Function to add an employee
def add_employee():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            id_val = id_entry.get()
            name_val = name_entry.get()
            age_val = age_entry.get()
            role_val = role_entry.get()
            sql = "INSERT INTO empdata (id, name, age, role) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_val, name_val, age_val, role_val))
            connection.commit()
            result_label.configure(text="Employee added successfully!")
        except Error as e:
            result_label.configure(text=f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to view all employees
def view_employees():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM empdata")
            rows = cursor.fetchall()
            result_text = "\n".join([f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Role: {row[3]}" for row in rows])
            result_label.configure(text=result_text if rows else "No employees found.")
        except Error as e:
            result_label.configure(text=f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Set up the GUI
app = ctk.CTk()
app.title("EmployeeSync - Employee Management System")
app.geometry("600x500")

# Fonts
font1 = ("Arial", 20, "bold")
font2 = ("Arial", 15)

# Input fields
ctk.CTkLabel(app, text="ID:", font=font1).place(x=20, y=20)
id_entry = ctk.CTkEntry(app, font=font2, width=200)
id_entry.place(x=100, y=20)

ctk.CTkLabel(app, text="Name:", font=font1).place(x=20, y=80)
name_entry = ctk.CTkEntry(app, font=font2, width=200)
name_entry.place(x=100, y=80)

ctk.CTkLabel(app, text="Age:", font=font1).place(x=20, y=140)
age_entry = ctk.CTkEntry(app, font=font2, width=200)
age_entry.place(x=100, y=140)

ctk.CTkLabel(app, text="Role:", font=font1).place(x=20, y=200)
role_entry = ctk.CTkEntry(app, font=font2, width=200)
role_entry.place(x=100, y=200)

# Buttons
ctk.CTkButton(app, text="Add Employee", command=add_employee, font=font1).place(x=20, y=260)
ctk.CTkButton(app, text="View Employees", command=view_employees, font=font1).place(x=20, y=320)

# Result label
result_label = ctk.CTkLabel(app, text="", font=font2, wraplength=500)
result_label.place(x=20, y=380)

# Start the app
app.mainloop()