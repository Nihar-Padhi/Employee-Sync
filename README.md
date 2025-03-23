# Employee Sync: Cloud-Based Employee Management System

## Overview
EmployeeSync is a cloud-based employee management system designed to streamline the process of adding, updating, and deleting employee records. Initially developed as a desktop application using Python with CustomTkinter and MySQL on Amazon RDS, it has evolved into a web-based application using Flask and HTML/CSS, hosted on AWS EC2 and accessible via a custom GoDaddy domain (`learn.xyz`). This project demonstrates the integration of AWS cloud services with a web application for scalable, real-time employee data management.

## Purpose
The goal of EmployeeSync is to:
- Provide a user-friendly interface for managing employee records (ID, Name, Age, Role).
- Leverage AWS cloud infrastructure (RDS for database, EC2 for hosting) for scalability and reliability.
- Transition from a local GUI app to a web-accessible solution, making it available globally via a custom domain.
- Showcase a practical application of Python, Flask, MySQL, and AWS for educational and professional purposes.

## Features
- Add Employee: Input new employee details into the system.
- View Employees: Display a list of all employees in a colorful, responsive table.
- Update Employee: Modify existing employee records via a dedicated form.
- Delete Employee: Remove employee records with a single click.
- Cloud Hosting: Deployed on AWS EC2 with data stored in Amazon RDS (MySQL).
- Custom Domain: Accessible via `learn.xyz` (configured through GoDaddy DNS).

## Why This Approach?
- AWS Integration: Using RDS and EC2 ensures a scalable, secure, and production-ready environment compared to local hosting.
- Web Transition: Moving from CustomTkinter (desktop GUI) to Flask (web framework) allows broader accessibility without requiring local installation.
- Colorful UI: Enhanced HTML/CSS design improves user experience over the initial minimalistic layout.
- Database Management: MySQL on RDS provides robust data storage with constraints (e.g., unique IDs, required fields) for integrity.

## Project Structure
1. AWS Setup:
   - RDS: MySQL database (`employees` with `empdata` table) for storing employee records.
   - EC2: Hosts the Flask app on an Amazon Linux 2 instance.
2. Backend:
   - Flask (`app.py`) handles CRUD operations (Create, Read, Update, Delete) with MySQL Connector for RDS integration.
3. Frontend:
   - HTML templates (`index.html`, `update.html`) with CSS for a vibrant, user-friendly interface.
4. Domain Configuration:
   - GoDaddy DNS points `learn.xyz` to the EC2 public IP.

## How It Works
1. Setup AWS Environment:
   - Configure RDS with a MySQL database and EC2 with a public IP.
2. Develop the Application:
   - Flask backend processes requests and interacts with RDS.
   - HTML/CSS frontend provides an interactive UI.
3. Deploy:
   - Upload files to EC2, install dependencies, and run the Flask app.
4. Access:
   - Point `learn.xyz` to EC2 via GoDaddy DNS and access the app online.

## Prerequisites
- Python 3.x
- AWS Account (RDS, EC2)
- GoDaddy Domain (`learn.xyz`)
- MySQL Client (e.g., MySQL Workbench)
- Dependencies: `flask`, `mysql-connector-python`

## Installation
1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/employeesync.git
   cd employeesync
   ```
2. Set Up AWS:
   - Follow the AWS RDS and EC2 setup steps (see document).
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Update Configuration:
   - Edit `app.py` with your RDS endpoint, username, and password.
5. Run Locally (optional):
   ```bash
   python app.py
   ```
6. Deploy to EC2:
   - Upload files, install dependencies, and run with `nohup python3 app.py &`.

## Deployment
- EC2: Use SCP to upload `app.py` and `templates/`, then run the app.
- Domain: Update GoDaddy DNS with the EC2 public IP.
- Test at `http://learn.xyz` after DNS propagation.

## Future Improvements
- HTTPS: Add SSL via AWS Certificate Manager for security.
- Validation: Enhance input validation (e.g., duplicate IDs, age limits).
- Scalability: Migrate to AWS Elastic Beanstalk or App Runner.

