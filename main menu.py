from student import Student
from fees import Fees
from attendance import *
from subjects import SubjectManagement
from marks import MarksManagement
from authentication import reset_password, student_login, admin_login
from datetime import datetime
from analytics import *
from importexport import ImportExport
import getpass



def parse_date(date_string):
    date_string = date_string.strip()

    formats = [
        "%d-%m-%Y",   
        "%d/%m/%Y",   
        "%d.%m.%Y",   

        "%Y-%m-%d",   
        "%Y/%m/%d",   
        "%Y.%m.%d",   

        "%m-%d-%Y",   
        "%m/%d/%Y",   

        "%d-%m-%y",   
        "%d/%m/%y",   
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue

    return None


def student_menu(rollno):
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. Fees")
        print("2. Attendance")
        print("3. Marks")
        print("4. Profile")
        print("5. Reset Password")
        print("6. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            Fees.view_fees(rollno)

        elif ch == "2":
            view_attendance_by(rollno)

        elif ch == "3":
            MarksManagement.view_student_marks(rollno)

        elif ch == "4":
            Student.view_student_by_rollno(rollno)

        elif ch == "5":
            reset_password(rollno)

        elif ch == "6":
            print("Logging you out....")
            break

        else:
            print("Invalid choice.")


def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Student Management")
        print("2. Fees Management")
        print("3. Attendance Management")
        print("4. Marks Management")
        print("5. Subject Management")
        print("6. Analytics")
        print("7. Import/Export Data")
        print("8. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            student_management_menu()

        elif ch == "2":
            fees_management_menu()

        elif ch == "3":
            attendance_management_menu()

        elif ch == "4":
            marks_management_menu()

        elif ch == "5":
            subject_management_menu()

        elif ch == "6":
            analytics_menu()

        elif ch == "7":
            import_export_menu()

        elif ch == "8":
            break

        else:
            print("Invalid choice.")            


def student_management_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT MENU =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Back to Admin Menu")

        ch2 = input("Enter choice: ")

        if ch2 == "1":
            try:
                rollno=int(input("Roll No: "))
                if rollno<=0:
                    print("Invalid roll number. Please enter a positive integer.")
                    continue
            except ValueError:
                print("Please enter valid Roll no.")
                continue    
            name=input("Name: ")
            dob=input("Date of birth:")
            dob = parse_date(dob)

            
            fathername=input("Father's Name: ")
            mothername=input("Mother's Name: ")
            sem=int(input("Semester: "))
            if sem not in range(1,9):
                print("Invalid semester. Please enter a value between 1 and 8.")
                continue
            branch=input("Branch: ")
            if branch not in ["CSE", "ECE", "MECH", "CIVIL", "EEE", "AI/DS", "AI/ML"]:
                print("Invalid branch. Please enter a valid branch.")
                continue
            phone=input("Phone Number: ")
            if not phone.isdigit() or len(phone) != 10:
                print("Invalid phone number. Please enter a 10-digit number.")
                continue
            address=input("Address: ")
                        

            Student.add_student(rollno, name, dob, fathername, mothername, sem, branch, phone, address)
            print("Student added successfully.")

        elif ch2 == "2":
            rollno = input("Enter roll number of the student to update: ") 
            if not rollno:
               print("Roll number cannot be empty.")
            else:
               Student.update_student(rollno)
        elif ch2 == "3":
            rollno = input("Enter roll number of the student to delete: ")
            if not rollno:
                print("Roll number cannot be empty.")
            else:
                Student.delete_student(rollno)
                print(f"Roll no {rollno} deleted. ")
        elif ch2 == "4":
            print("1. View All Students")
            print("2. View Student by Roll Number")
            print("3. View Students by Semester and Branch")
            print("4. View Students by Name")
            print("5. Back to Student Management System Menu")
            ch3 = input("Enter choice: ")
            if ch3 == "1":
                Student.view_all_students()
            elif ch3 == "2":
                rollno = input("Enter roll number of the student to view: ")
                if not rollno:
                    print("Roll number cannot be empty.")
                else:
                    Student.view_student_by_rollno(rollno)
            elif ch3 == "3":
                sem = input("Enter semester: ")
                branch = input("Enter branch: ")
                if not sem or not branch:
                    print("Semester and branch cannot be empty.")
                else:
                    Student.view_student(branch,sem)
            elif ch3 == "4":
                name = input("Enter name of the student to view: ")
                if not name:
                    print("Name cannot be empty.")
                else:
                    Student.view_student_by_name(name)                
            elif ch3 == "5":
                break
            else:
                print("Invalid choice.")

        elif ch2 == "5":
            break
        else:
            print("Invalid choice........")        

def fees_management_menu():
    while True:
        print("\n===== FEES MANAGEMENT MENU =====")
        print("1. Add Fees Record")
        print("2. Update Fees Record")
        print("3. Delete Fees Record")
        print("4. View Fees Records")
        print("5. Back to Admin Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            rollno = int(input("Enter roll number of the student to add fees record: "))
            penalty = int(input("Enter Penalty if any: ") or 0)
            feespaid = int(input("Enter Fees Paid: ") or 0)
            feesconcession = int(input("Enter Fees Concession if any: ") or 0)
            Fees.add_fees(rollno, penalty, feespaid, feesconcession)

        elif ch == "2":
            rollno = int(input("Enter roll number of the student to update fees record: "))
            if not rollno:
                print("Roll number cannot be empty.")
            else:
                Fees.update_fees(rollno)

        elif ch == "3":
            rollno = int(input("Enter roll number of the student to delete fees record: "))
            if not rollno:
                print("Roll number cannot be empty.")
            else:
                Fees.delete_fees(rollno)

        elif ch == "4":
            print("1. View All Fees Records")
            print("2. View Fees Record by Roll Number")
            print("3. View Fees Records by Branch and Semester")
            print("4. Back to Fees Management Menu")
            ch = input("Enter choice: ")
            if ch == "1":
                Fees.view_all_fees()
            elif ch == "2":
                rollno = input("Enter roll number of the student to view fees record: ")
                if not rollno:
                    print("Roll number cannot be empty.")
                else:
                    Fees.view_fees(rollno)
            elif ch == "3":
                branch = input("Enter branch: ")
                sem = int(input("Enter semester: "))
                if not branch or not sem:
                    print("Branch and semester cannot be empty.")
                else:
                    Fees.view_fees_by_branch_sem(branch, sem)
            elif ch == "4":
                break
            else:
                print("Invalid choice.")

        elif ch == "5":
            break

        else:
            print("Invalid choice.")


def attendance_management_menu():
    while True:
        print("\n===== ATTENDANCE MANAGEMENT MENU =====")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. View Attendance Records by Subject")
        print("4. Back to Admin Menu")

        ch = input("Enter choice: ")
        if ch == "1":
            sem = int(input("Enter Semester: "))
            if sem not in range(1, 9):
                print("Invalid semester. Please enter a value between 1 and 8.")
                continue
            branch = input("Enter Branch: ").upper()
            if branch not in ["CSE", "ECE", "MECH", "CIVIL", "EEE", "AI/DS", "AI/ML"]:
                print("Invalid branch. Please enter a valid branch.")
                continue
            subjects=SubjectManagement.get_subjects(sem,branch)
        

            subject_id = int(input("Enter Subject ID: "))
            if not subject_id:
                print("Subject ID cannot be empty.")
                continue
            mark_attendance(sem,branch,subject_id)

        elif ch == "2":
            sem = int(input("Enter Semester: "))
            if sem not in range(1, 9):
                print("Invalid semester. Please enter a value between 1 and 8.")
                continue
            branch = input("Enter Branch: ").upper()
            if branch not in ["CSE", "ECE", "MECH", "CIVIL", "EEE", "AI/DS", "AI/ML"]:
                print("Invalid branch. Please enter a valid branch.")
                continue
            view_attendance_by_sem_branch(sem,branch)

        elif ch == "3":
            subject_id = int(input("Enter Subject ID: "))
            if not subject_id:
                print("Subject ID cannot be empty.")
                continue
            view_attendance_by_subject(subject_id)

        elif ch == "4":
            break

        else:
            print("Invalid choice.") 

def marks_management_menu():
    while True:
        print("\n===== MARKS MANAGEMENT MENU =====")
        print("1. Add Marks Record")
        print("2. Update Marks Record")
        print("3. Delete Marks Record")
        print("4. View Marks Records")
        print("5. Back to Admin Menu")

        ch = input("Enter choice: ")
        

        if ch == "1":
            sem=int(input("Enter sem:"))
            branch=input("Enter branch:").upper()                   

            MarksManagement.add_marks(sem,branch)
            print(f"Marks added for {sem} semester and {branch} branch.")

        elif ch == "2":
            rollno = int(input("Enter roll number of the student to update marks record: "))
            subject_id=int(input("Enter subject id: "))
            if not rollno and subject_id:
                print("Fields cannot be empty.")
            else:
                MarksManagement.update_marks(rollno,subject_id)
                print("Marks updated.")

        elif ch == "3":
            rollno = int(input("Enter roll number of the student to delete marks record: "))
            subject_id=int(input("Enter subject id :"))
            if not rollno:
                print("Roll number cannot be empty.")
            else:
                MarksManagement.delete_marks(rollno,subject_id)
                print("Marks delted.")

        elif ch == "4":
            print("1. View Marks Records by Subject Id")
            print("2. View Marks Record by Roll Number")
            print("3. View Marks Records by Branch and Semester")
            print("4. View all Marks Record")
            print("5. Back to Marks Management Menu")
            ch = input("Enter choice: ")
            if ch == "1":
                subject_id=int(input("Enter subject id: "))
                MarksManagement.view_marks(subject_id)
            elif ch == "2":
                rollno = input("Enter roll number of the student to view marks record: ")
                if not rollno:
                    print("Roll number cannot be empty.")
                else:
                    MarksManagement.view_student_marks(rollno)
            elif ch == "3":
                branch = input("Enter branch: ")
                sem = input("Enter semester: ")
                if not branch or not sem:
                    print("Branch and semester cannot be empty.")
                else:
                    MarksManagement.view_marks_by_sem_branch(sem, branch)
            elif ch=="4":
                MarksManagement.view_all_marks()        
            elif ch == "5":
                break
            else:
                print("Invalid choice.")

        elif ch == "5":
            break

        else:
            print("Invalid choice.")

def subject_management_menu():
    while True:
        print("\n===== SUBJECT MANAGEMENT MENU =====")
        print("1. Add Subject")
        print("2. Update Subject")
        print("3. Delete Subject")
        print("4. View Subjects")
        print("5. Back to Admin Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            subject_id = int(input("Enter Subject ID: "))
            subject_exists = SubjectManagement.subject_exists(subject_id)
            if subject_exists:
                print(f"Subject with Subject ID {subject_id} already exists.")
                break
                        
            subject_name = input("Enter Subject Name: ")    
            subject_code = input("Enter Subject Code: ")
            sem = int(input("Enter Semester: "))
            branch = input("Enter Branch: ").upper()    
            credits = int(input("Enter Credits: "))
            if not subject_id or not subject_name or not subject_code or not sem or not branch or not credits:
                print("All fields are required. Please provide valid inputs.")
            SubjectManagement.add_subject(subject_id,subject_name,subject_code,sem,branch,credits)
            print("Subject addedd successfully...")

        elif ch == "2":
            subject_id = int(input("Enter subject ID to update: "))
            if not subject_id:
                print("Subject ID cannot be empty.")
            else:
                SubjectManagement.update_subjects(subject_id)
                print("subject updated")

        elif ch == "3":
            subject_id = int(input("Enter subject ID to delete: "))
            if not subject_id:
                print("Subject ID cannot be empty.")
            else:
                SubjectManagement.delete_subject(subject_id)
                print("subject deleted")
        elif ch == "4":
            SubjectManagement.view_subjects()

        elif ch == "5":
            break

        else:
            print("Invalid choice.")    


def analytics_menu():
    while True:
        print("\n===== ANALYTICS MENU =====")
        print("1. Student Strength Analysis")
        print("2. Marks Analysis")
        print("3. Attendance Analysis")
        print("4. Student Performance Analysis")
        print("5. Fees Analysis")
        print("6. Student at risk")
        print("7. Back to Admin Menu")

        ch = input("Enter choice: ")

        if ch == "1":
          while True:  
            print("1.Student Strength")
            print("2.Student strength by sem")
            print("3. Student Strength by branch")
            print("4.Back")
            ch1=input("Enter :")
            
            if ch1=='2':
                student_strength()
            elif ch1=='1':
                student_strength_by_sem_and_branch()
            elif ch1=='3':
                student_strength_by_branch()
            elif ch1=='4':
                break
            else:
                print("Invalid choice....")
                continue
                    


        elif ch == "2":
            marks_analysis()

        elif ch == "3":
            attendance_analysis()

        elif ch == "4":
            student_performance_analysis()

        elif ch == "5":
            fees_analysis()

        elif ch == "6":
            risk_analysis()
        elif ch == "7":
            break    

        else:
            print("Invalid choice.")                                           
def import_export_menu():
    while True:
        print("\n===== IMPORT/EXPORT DATA MENU =====")
        print("1. Import Students from CSV")
        print("2. Export Students to CSV")
        print("3. Import Fees from CSV")
        print("4. Export Fees to CSV")
        print("5. Import Attendance from CSV")
        print("6. Export Attendance to CSV")
        print("7. Import Marks from CSV")
        print("8. Export Marks to CSV")
        print("9. Import subjects from CSV")
        print("10. Export subjects to CSV")
        print("11. Back to Admin Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            file_path = input("Enter the path of the CSV file to import students: ").strip().strip('"')
            ImportExport.import_students_from_csv(file_path)
            print("Student imported successfully...")

        elif ch == "2":
            file_path = input("Enter the path where the CSV file will be exported: ").strip().strip('"')
            ImportExport.export_students_to_csv(file_path)
            print("Students exported successfully...")

        elif ch == "3":
            file_path = input("Enter the path of the CSV file to import fees: ").strip().strip('"')
            ImportExport.import_fees_from_csv(file_path)
            print("Fees imported successfully...")
        elif ch == "4":
            file_path = input("Enter the path where the CSV file will be exported: ").strip().strip('"')
            ImportExport.export_fees_to_csv(file_path)
            print("Fees data exported successfully...")
        elif ch == "5":
            file_path = input("Enter the path of the CSV file to import attendance: ").strip().strip('"')
            ImportExport.import_attendance_from_csv(file_path)
            print("Attendance record imported successfully...")

        elif ch == "6":
            file_path = input("Enter the path where the CSV file will be exported: ").strip().strip('"')
            ImportExport.export_attendance_to_csv(file_path)
            print("Attendance record exported successfully...")

        elif ch == "7":
            file_path = input("Enter the path of the CSV file to import marks: ").strip().strip('"')
            ImportExport.import_marks_from_csv(file_path)
            print("marks imported successfully...")

        elif ch == "8":
            file_path = input("Enter the path where the CSV file will be exported: ").strip().strip('"')
            ImportExport.export_marks_to_csv(file_path)
            print("marks exported successfully...")

        elif ch == "9":
            file_path = input("Enter the path of the csv file to import subjects: ").strip().strip('"')
            ImportExport.import_subjects_from_csv(file_path)
            print("subjects imported successfully...")

        elif ch == "10":
            file_path = input("Enter the path where the CSV file will be exported: ").strip().strip('"')
            ImportExport.export_subjects_to_csv(file_path)
            print("subjects exported successfully")

        elif ch == "11":
            break    

        else:
            print("Invalid choice.")




while True:
    print("__________________________________________________________________") 
    print()
    print("             WELCOME TO STUDENT ERP SYSTEM    ")
    print("__________________________________________________________________")
    print(" MAIN MENU ")
    print(" 1.STUDENT LOGIN ")
    print(" 2.ADMIN LOGIN ")
    print(" 3.Exit ")
    while True:
        choice=input("Enter your choice: ")
        if choice=="1":
          rollno=int(input("Enter Roll Number: "))
          password=getpass.getpass("Enter password: ")
          if student_login(username=rollno,password=password):
            student_menu(rollno)
          else:
            print("Invalid Roll Number or Password. Please try again.")
            print("1. Reset your password?")
            print("2. Try again")
            ch=input("Enter your choice: ")
            if ch=="1":
                reset_password(username=rollno)
            else:
                continue
        elif choice=="2":
          username=input("Enter Username: ")
          password=getpass.getpass("Enter Password: ")
          if admin_login(username=username,password=password):
            admin_menu()

          else:   
            print("Invalid Username or Password. Please try again.")
            

        elif choice=="3":
          print("Thanks ... ") 
          break       
        else:
          print("Invalid choice. Please enter 1 for Student Login or 2 for Admin Login.")