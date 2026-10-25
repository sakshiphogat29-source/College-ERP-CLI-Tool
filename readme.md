# 🎓 Student ERP System

A Python and MySQL-based Student ERP System designed to manage student records, fees, attendance, marks, and subjects through a menu-driven interface.

The application provides separate student and administrator login access, analytics, and CSV import/export functionality.

## 📸 Screenshots

### Main Menu
![Main Menu](Screenshots/Main%20menu.png)

### Mark Attendance
![Mark Attendance](Screenshots/Mark%20attendance.png)

### Students Exported
![Students Exported](Screenshots/students%20exported.png)

### Analytics: Student Strength
![Student Strength](Screenshots/Student%20strength.png)

### Analytics: Students at Risk
![Students at Risk](Screenshots/Student%20at%20risk.png)

### Student Risk Analysis
![Student Risk Analysis](Screenshots/Student%20risk%20analysis.png)

## ✨ Features

### 👨‍🎓 Student Login
- View fee records
- View attendance
- View marks
- View personal profile
- Reset password

### 🔐 Admin Login
Administrators can manage student records and academic information.

### 👥 Student Management
- Add, update, delete, and view student records
- Search by roll number or name
- Filter by semester and branch
- Prevent duplicate student entries

### 💰 Fees Management
- Add, update, delete, and view fee records
- View fees by roll number
- Filter fees by branch and semester

### 📅 Attendance Management
- Mark student attendance
- View attendance records
- View attendance by subject
- Filter attendance by semester and branch

### 📊 Marks Management
- Add, update, delete, and view marks records
- View marks by subject or student
- Filter marks by semester and branch

### 📚 Subject Management
- Add, update, delete, and view subjects
- Check for existing subject IDs

### 📈 Analytics
- Student strength analysis
- Student strength by semester and branch
- Marks analysis
- Attendance analysis
- Student performance analysis
- Fees analysis
- Student-at-risk analysis

### 📁 CSV Import/Export
Import and export student and academic data using CSV files.

Supported data may include:
- Students
- Fees
- Attendance
- Marks
- Subjects

## 🛠️ Technologies Used
- Python
- MySQL
- Pandas
- Matplotlib
- CSV
- Logging

## 📂 Project Structure

```text
College-ERP-CLI-Tool/
├── analytics.py
├── attendance.py
├── authentication.py
├── database.py
├── fees.py
├── importexport.py
├── logger.py
├── main.py
├── marks.py
├── student.py
├── subjects.py
├── requirements.txt
├── readme.md
├── .gitignore
└── Screenshots/
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sakshiphogat29-source/College-ERP-CLI-Tool.git
cd College-ERP-CLI-Tool
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL
- Install and start MySQL.
- Create the required database and tables.
- Configure your database connection in `database.py`.

### 4. Run the application

```bash
python main.py
```

Use the login credentials configured in the application. Student login uses the credentials required by your implementation, while administrator login uses the configured admin credentials.

**Security note:** Do not commit database passwords or other sensitive credentials to GitHub.

## 🔮 Future Improvements
- GUI or web-based interface
- Improved role-based access control
- Secure password hashing
- Automated database backups
- Advanced analytics and visualizations
- Attendance and performance reports

## 👩‍💻 Author

**Sakshi**

⭐ If you find this project useful, consider giving it a star on GitHub!