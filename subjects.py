from database import db
import pandas as pd
from logger import logger

class SubjectManagement:
    @staticmethod
    def add_subject(subject_id, subject_name, subject_code, sem, branch, credits):
        db.connect_db()        
        query="INSERT INTO subjects(subject_id,subject_name,subject_code,sem,branch,credits) VALUES(%s,%s,%s,%s,%s,%s)" 
        values=(subject_id,subject_name,subject_code,sem,branch,credits) 
        logger.info("Subject added successfully with Subject ID %s", subject_id)
        db.execute_query(query,values) 
        db.close_db()
        
    @staticmethod
    def delete_subject(subject_id):
        db.connect_db()
        query="DELETE FROM subjects WHERE subject_id=%s"
        db.execute_query(query,(subject_id,))
        logger.info("Subject deleted successfully with Subject ID %s", subject_id)
        db.close_db()
    @staticmethod    
    def view_subjects():
        db.connect_db()
        query="SELECT * FROM subjects ORDER BY subject_id"
        result=db.fetch_query(query)
        df=pd.DataFrame(result,columns=['subject_id','subject_name','subject_code','sem','branch','credits'])
        print(df)
        db.close_db()
    @staticmethod
    def update_subjects(subject_id,subject_name=None,subject_code=None,sem=None,branch=None,credits=None):
        db.connect_db()
        query="UPDATE subjects SET"
        values=[]
        subject_name
        if  subject_name is not None:
            query+=" subject_name=%s, "
            values.append(subject_name)
        if subject_code is not None:
            query+=" subject_code=%s, " 
            values.append(subject_code)
        if sem is not None:
            query+=" sem=%s, "
            values.append(sem)
        if branch is not None:
            query+=" branch=%s, "
            values.append(branch)
        if credits is not None:
            query+=" credits=%s, "
            values.append(credits)
        query=query.rstrip(", ")    
        query+=" WHERE subject_id = %s"
        values.append(subject_id)
        db.execute_query(query,values)
        logger.info("Subject updated successfully with Subject ID %s", subject_id)
        db.close_db()
    @staticmethod
    def get_subjects(sem,branch):
        db.connect_db()
        query="SELECT subject_id,subject_name,subject_code FROM subjects WHERE sem=%s and branch=%s ORDER BY subject_id"
        result=db.fetch_query(query,(sem,branch))
        df=pd.DataFrame(result,columns=['subject_id','subject_name','subject_code'])
        print(df)
        return result
    
    @staticmethod
    def get_subject_name(subject_id):
        db.connect_db()
        query="SELECT subject_name FROM subjects WHERE subject_id = %s"
        result=db.fetch_query(query,(subject_id,))
        db.close_db()
        if result and result[0][0]:
            return result[0][0]
    @staticmethod
    def subject_exists(subject_id):
        db.connect_db()
        query="SELECT subject_name, subject_code FROM subjects WHERE subject_id=%s"
        result=db.fetch_query(query,(subject_id,))
        
        if result:
            return result[0]
        else:
            print("Subject does not exists")


        
            




