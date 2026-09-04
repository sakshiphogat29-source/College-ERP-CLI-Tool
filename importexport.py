from database import db
from pathlib import Path
import pandas as pd
from datetime import datetime
from logger import logger
class ImportExport:
    @staticmethod
    def import_students_from_csv(file_path):
        db.connect_db()
        df = pd.read_csv(file_path)
        for index, row in df.iterrows():
            dob = datetime.strptime(
            str(row['dob']),"%Y-%m-%d").date()

            password = dob.strftime("%d-%m-%Y")

            query = "INSERT INTO students (rollno, name, dob, fathername, mothername, sem, branch, phone, address,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
            values = (row['rollno'], row['name'], row['dob'], row['fathername'], row['mothername'], row['sem'], row['branch'], row['phone'], row['address'],password)
            db.execute_query(query, values)

        logger.info("Students imported successfully from CSV file: %s", file_path)
        db.close_db()

    @staticmethod
    def export_students_to_csv(file_path):
        db.connect_db()
        query = "SELECT * FROM students"
        result = db.fetch_query(query)
        df = pd.DataFrame(result, columns=['rollno', 'name', 'dob', 'fathername', 'mothername', 'sem', 'branch', 'phone', 'address'])
        df.to_csv(file_path, index=False)
        logger.info("Students exported successfully to CSV file: %s", file_path)
        db.close_db()


    @staticmethod
    def import_subjects_from_csv(file_path): 
        db.connect_db()
        df = pd.read_csv(file_path)
        for index, row in df.iterrows():
            query = "INSERT INTO subjects (subject_id, subject_name, subject_code, sem, branch, credits) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (row['subject_id'], row['subject_name'], row['subject_code'], row['sem'], row['branch'], row['credits'])
            db.execute_query(query, values)
        logger.info("Subjects imported successfully from CSV file: %s", file_path)
        db.close_db()

    @staticmethod
    def export_subjects_to_csv(file_path):
        db.connect_db()
        query = "SELECT * FROM subjects"
        result = db.fetch_query(query)
        df = pd.DataFrame(result, columns=['subject_id', 'subject_name', 'subject_code', 'sem', 'branch', 'credits'])
        df.to_csv(file_path, index=False)
        logger.info("Subjects exported successfully to CSV file: %s", file_path)
        db.close_db()  

    @staticmethod
    def import_attendance_from_csv(file_path):
        try:
            db.connect_db()
            df = pd.read_csv(file_path)
            for index, row in df.iterrows():
                query = "INSERT INTO attendancetable (rollno, attendance_date, status, subject_id, sem, branch) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (row['rollno'],row['attendance_date'], row['status'], row['subject_id'], row['sem'], row['branch'])
                db.execute_query(query, values)
                logger.info("Attendance imported successfully from CSV file: %s", file_path)
            db.close_db()
        except ValueError as e:
            print(f"Error in importing : {e}")        

    @staticmethod
    def export_attendance_to_csv(file_path):
        db.connect_db()
        query = "SELECT * FROM attendancetable"
        result = db.fetch_query(query)
        df = pd.DataFrame(result, columns=['rollno', 'name', 'attendance_date', 'status', 'subject_id', 'sem', 'branch'])
        df.to_csv(file_path, index=False)
        logger.info("Attendance exported successfully to CSV file: %s", file_path)
        db.close_db()

    @staticmethod
    def import_marks_from_csv(file_path):
        db.connect_db()
        df = pd.read_csv(file_path)
        for index, row in df.iterrows():
            query = "INSERT INTO marks (rollno, subject_id, internal, external, total, grade) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (row['rollno'], row['subject_id'], row['internal'], row['external'], row['total'], row['grade'])
            db.execute_query(query, values)
            logger.info("Marks imported successfully from CSV file: %s", file_path)
        db.close_db()

    @staticmethod
    def export_marks_to_csv(file_path): 
        db.connect_db()
        query = "SELECT * FROM marks"
        result = db.fetch_query(query)
        df = pd.DataFrame(result, columns=['rollno', 'subject_id', 'internal','external','total','grade'])
        df.to_csv(file_path, index=False)
        logger.info("Marks exported successfully to CSV file: %s", file_path)
        db.close_db()

    @staticmethod
    def import_fees_from_csv(file_path):    
        db.connect_db()
        df = pd.read_csv(file_path)
        for index, row in df.iterrows():
            query = "INSERT INTO fees (rollno, totalfees, feespaid, penalty, feesconcession, balancefees) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (int(row['rollno']),int(row['totalfees']),int(row['feespaid']),int(row['penalty']),int(row['feesconcession']),int(row['balancefees']))
            success = db.execute_query(query, values)
            if not success:
                print(f"failed to import row {index+1}")
        logger.info("Fees imported successfully from CSV file: %s", file_path)
        db.close_db()

    @staticmethod
    def export_fees_to_csv(file_path):
        db.connect_db()
        query = "SELECT * FROM fees"
        result = db.fetch_query(query)
        df = pd.DataFrame(result, columns=['rollno', 'totalfees','feespaid','penalty','feesconcession','balancefees'])
        df.to_csv(file_path, index=False)
        logger.info("Fees exported successfully to CSV file: %s", file_path)
        db.close_db()

    @staticmethod
    def import_subjects_from_csv(file_path):
        db.connect_db()
        df=pd.read_csv(file_path)
        for index,row in df.iterrows():
            query="INSERT INTO subjects(subject_id, subject_name, subject_code, sem, branch, credits) VALUES (%s,%s,%s,%s,%s,%s)"
            values=(row['subject_id'],row['subject_name'],row['subject_code'],row['sem'],row['branch'],row['credits'])
            success=db.execute_query(query,values)
            if not success:
                print(f"Failed to import row {index+1}")
        logger.info("File imported successfully.")
        

    @staticmethod
    def export_subjects_to_csv(file_path):
        db.connect_db()
        query="SELECT * FROM subjects"
        result=db.fetch_query(query)
        df=pd.DataFrame(result,columns=['subject_id','subject_name','subject_code','sem','branch','credits'])
        df.to_csv(file_path,index=False)
        logger.info("Subjects exported successfully.")            


    @staticmethod
    def backup_database(backup_file_path):
        db.connect_db()
        ImportExport.export_students_to_csv(f"{backup_file_path}_students.csv")
        ImportExport.export_subjects_to_csv(f"{backup_file_path}_subjects.csv")
        ImportExport.export_attendance_to_csv(f"{backup_file_path}_attendance.csv")
        ImportExport.export_marks_to_csv(f"{backup_file_path}_marks.csv")
        ImportExport.export_fees_to_csv(f"{backup_file_path}_fees.csv")
        logger.info("Database backup completed successfully to %s", backup_file_path)
        db.close_db()   

    @staticmethod
    def restore_database(backup_file_path):
        db.connect_db()
        ImportExport.import_students_from_csv(f"{backup_file_path}_students.csv")
        ImportExport.import_subjects_from_csv(f"{backup_file_path}_subjects.csv")
        ImportExport.import_attendance_from_csv(f"{backup_file_path}_attendance.csv")
        ImportExport.import_marks_from_csv(f"{backup_file_path}_marks.csv")
        ImportExport.import_fees_from_csv(f"{backup_file_path}_fees.csv")
        logger.info("Database restore completed successfully from %s", backup_file_path)
        db.close_db()                                    
