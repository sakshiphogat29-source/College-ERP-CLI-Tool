
import pandas as pd
from database import db
from logger import logger
class Student:
    @staticmethod    
    def add_student(rollno, name, dob, fathername, mothername, sem, branch, phone, address):
        db.connect_db()

        check_query = "SELECT * FROM students WHERE ROLLNO=%s"
        check_values = (rollno,)

        result = db.fetch_query(check_query, check_values)

        if result:
            print("Roll number already exists.")
        else:
            query = """
            INSERT INTO students
            (ROLLNO, NAME, DOB, FATHERNAME, MOTHERNAME, SEM, BRANCH, PHONE, ADDRESS, PASSWORD)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            password = dob.strftime("%d-%m-%Y")

            values = (
            rollno,
            name,
            dob,
            fathername,
            mothername,
            sem,
            branch,
            phone,
            address, password
            )

            db.execute_query(query, values)
            logger.info("Student added successfully for Roll No %s", rollno)

        db.close_db()
    @staticmethod    
    def delete_student(rollno):
        db.connect_db()
        query="DELETE FROM students WHERE ROLLNO = %s"
        values=(rollno,)
        db.execute_query(query,values)
        logger.info("Student deleted successfully for Roll No %s", rollno)
        db.close_db()
    @staticmethod
    def update_student(rollno):

        db.connect_db()
        query="SELECT name, dob, fathername, mothername, sem, branch, phone, address FROM students WHERE rollno=%s"
        result=db.fetch_query(query,(rollno,))
        if not result:
            print("No data found for the given roll number.")
            db.close_db()
            return
        else:
            current_name=result[0][0]
            current_dob=result[0][1]
            current_fathername=result[0][2]
            current_mothername=result[0][3]
            current_sem=result[0][4]
            current_branch=result[0][5]
            current_phone=result[0][6]
            current_address=result[0][7]
            name=input(f"Enter new name (current: {current_name}): ")
            dob=input(f"Enter new date of birth (current: {current_dob}): ")
            
            fathername=input(f"Enter new father's name (current: {current_fathername}): ")
            mothername=input(f"Enter new mother's name (current: {current_mothername}): ")
            sem=input(f"Enter new semester (current: {current_sem}): ")
            
            branch=input(f"Enter new branch (current: {current_branch}): ")
            phone=input(f"Enter new phone number (current: {current_phone}): ")
            
            address=input(f"Enter new address (current: {current_address}): ")
            
            if not name:
                name=current_name
            if not dob:
                dob=current_dob
            if not fathername:
                fathername=current_fathername
            if not mothername:
                mothername=current_mothername
            if not sem:
                sem=current_sem
            if not branch:
                branch=current_branch
            if not phone:
                phone=current_phone
            if not address:
                address=current_address

        query = "UPDATE students SET name=%s, dob=%s, fathername=%s, mothername=%s, sem=%s, branch=%s, phone=%s, address=%s WHERE rollno=%s"
        values = (name, dob, fathername, mothername, sem, branch, phone, address, rollno)

        db.execute_query(query, values)

        db.close_db()
        logger.info("Student updated successfully for Roll No %s", rollno)
    @staticmethod
    def search_student(rollno,name):
        db.connect_db()
        query = "SELECT * FROM students WHERE rollno=%s OR name=%s"
        values=(rollno,name)
        result=db.fetch_query(query,values)
        db.close_db()
        return result 
    @staticmethod
    def view_student(branch,sem):
        db.connect_db()
        query="SELECT * FROM students WHERE sem=%s AND branch=%s"
        values=(sem,branch)
        result = db.fetch_query(query,values)
        if result:
            df=pd.DataFrame(result,columns=['rollno','name','dob','fathername','mothername','sem','branch','phone','address'])
            print(df)
        db.close_db()
        
    @staticmethod    
    def view_all_students():  
        db.connect_db()
        query="SELECT rollno,name,dob,fathername,mothername,sem,branch,phone,address FROM students"
        result = db.fetch_query(query)
        df = pd.DataFrame(result,columns=['rollno','name','dob','fathername','mothername','sem','branch','phone','address'])
        print(df)
        db.close_db()
        
    @staticmethod
    def view_student_by_rollno(rollno):
        db.connect_db()
        query="SELECT rollno,name,dob,fathername,mothername,sem,branch,phone,address FROM students WHERE rollno=%s"
        values=(rollno,)
        result = db.fetch_query(query,values)
        df = pd.DataFrame(result,columns=['rollno','name','dob','fathername','mothername','sem','branch','phone','address'])
        pd.set_option('display.max_columns', None)

        print(df)
        db.close_db()
        
    @staticmethod    
    def view_student_by_name(name):
        db.connect_db()
        query="SELECT * FROM students WHERE name=%s"
        values=(name,)
        result = db.fetch_query(query,values)
        db.close_db()
        df = pd.DataFrame(result,columns=['rollno','name','dob','fathername','mothername','sem','branch','phone','address'])
        print(df)
    @staticmethod    
    def order_students_by_rollno():
        db.connect_db()
        query="SELECT * FROM students ORDER BY rollno"
        result = db.fetch_query(query)
        db.close_db()
        return result
    @staticmethod    
    def order_students_by_name():
        db.connect_db()
        query="SELECT * FROM students ORDER BY name"
        result = db.fetch_query(query)
        db.close_db()
        return result
    @staticmethod    
    def count_students():
        db.connect_db()
        query="SELECT COUNT(*) FROM students"
        result = db.fetch_query(query)
        db.close_db()
        return result
    @staticmethod    
    def count_students_by_branch(branch):
        db.connect_db()
        query="SELECT COUNT(*) FROM students WHERE branch=%s"
        values=(branch,)
        result = db.fetch_query(query,values)
        db.close_db()
        return result
        
    @staticmethod
    def count_student_by_sem(sem):
        db.connect_db()
        query="SELECT COUNT(*) FROM students WHERE sem=%s"
        values=(sem,)
        result=db.fetch_query(query,values)
        db.close_db()
        return result
    @staticmethod
    def count_student_by_branch_and_sem(branch,sem): 
        db.connect_db()
        query="SELECT COUNT(*) FROM students WHERE branch=%s AND sem=%s"
        values=(branch,sem)
        result = db.fetch_query(query,values)
        db.close_db()
        return result

    @staticmethod
    def get_students(sem,branch):
        
        query="SELECT rollno, name FROM students WHERE sem=%s AND branch=%s"
        result=db.fetch_query(query,(sem,branch))
        if result and result[0][0]:
            return result
            
      
