# Student ERP System

A Python and MySQL-based Student ERP System designed to efficiently manage student records, academic information, attendance, fees, marks, and subjects through a simple menu-driven interface.

The system provides separate login access for students and administrators and includes analytics features to visualize and analyze student data.

## Screenshots
### Main menu
![Main menu](Screenshots/Main%20menu.png)
### Mark attendance
![Mark attendance](Screenshots/Mark%20attendance.png)
### Students Exported
![students exported](Screenshots/students%20exported)
### Analytics
### Student strength
![Student strength](Screenshots/Student%20strength)
#### Students at risk
![Students at Risk](https://github.com/sakshiphogat29-source/College-ERP-CLI-Tool/raw/refs/heads/main/Screenshots/Student%20at%20risk.png)
![Student risk analysis](Screenshots/Student%20risk%20analysis)



## Features
### Student Login

Students can log in using their roll number and password and access:

-View fee records

-View attendance

-View marks

-View personal profile

-Reset password

-Admin Login

Administrators can log in and manage the complete student system.

### Student Management
-Add student records

-Update student information

-Delete student records

-View all students

-Search students by roll number

-Search students by name

-Filter students by semester and branch

-Prevent duplicate student entries

### Fees Management
-Add fee records

-Update fee records

-Delete fee records

-View all fee records

-View fees by roll number

-View fees by branch and semester

###Attendance Management
Mark student attendance

View attendance records

View attendance by subject

View attendance by semester and branch

### Marks Management
-Add marks records

-Update marks

-Delete marks

-View marks by subject

-View marks by student

-View marks by semester and branch

-View all marks records

### Subject Management
-Add subjects

-Update subjects

-Delete subjects

-View subjects

-Check for existing subject IDs

### Analytics

The system provides analytical features to understand student-related data and identify trends.

-Student strength analysis

-Student strength by semester and branch

-Marks analysis

-Attendance analysis

-Student performance analysis

-Fees analysis

-Student-at-risk analysis

-CSV Import/Export

Student and academic data can be easily imported from and exported to CSV files.

## Supported data:

Students

Fees

Attendance

Marks

Subjects


## Technologies Used
Python

MySQL

Pandas

Matplotlib

CSV

Logging


## Project Structure
Student-ERP-System/
│
├── main menu.py

├── database.py

├── student.py

├── fees.py

├── attendance.py

├── subjects.py

├── marks.py

├── authentication.py

├── analytics.py

├── importexport.py

├── logger.py

├── requirements.txt

├── README.md

└── .gitignore

## How to Run
1. Clone the Repository
   
git clone <repository-url>

cd Student-ERP-System

3. Install Python Dependencies

Install the required Python libraries using:

pip install -r requirements.txt

3. Set Up MySQL
Install and start MySQL.

Create the required database.

Create the required tables.

Configure the database connection in database.py.

5. Run the Application
python main.py

## Login

The system provides two types of users:

Student: Login using roll number and password.

Admin: Login using admin credentials configured in the application.

### Data Management

The system uses MySQL to store student-related information and supports CSV import/export for convenient data transfer and management.

## Future Improvements
GUI or web-based interface

Role-based access control

Secure password hashing

Automated database backup

More advanced analytics and visualizations

Attendance and performance reports

## Author

Sakshi
