from database import db
import pandas as pd
from logger import logger
class Fees:
    @staticmethod
    def add_fees(rollno, penalty, feespaid, feesconcession):
        db.connect_db()

        try:
            check_query = "SELECT rollno FROM fees WHERE rollno=%s"
            existing = db.fetch_query(check_query, (rollno,))

            if existing:
                print("Fee record already exists for this student.")
                return
            query = "SELECT branch FROM students WHERE rollno=%s"
            result = db.fetch_query(query, (rollno,))
            branch=result[0][0].lower()
            fee_structure = {"cse": 100000,"ece": 90000,"mech": 80000, "civil": 85000,"eee": 95000,"ai/ds": 110000,"ai/ml": 110000}
            
            totalfees = fee_structure.get(branch)
            if totalfees is None:
                print("NO fees record exists for" , branch)
                return
            
            
            balancefees = totalfees + penalty - feespaid - feesconcession

            
            insert_query = """
            INSERT INTO fees
            (rollno, totalfees, feespaid, penalty, feesconcession, balancefees)
             VALUES (%s, %s, %s, %s, %s, %s)
             """

            values = (rollno, totalfees, feespaid, penalty, feesconcession, balancefees)

            db.execute_query(insert_query, values)

            logger.info("Fees added successfully for Roll No %s", rollno)
        finally:
             db.close_db()
    @staticmethod
    def update_fees( rollno, totalfees=None, penalty=None, feespaid=None, feesconcession=None, balancefees=None):
        db.connect_db()
        query = "UPDATE FEES SET "
        values = []
        if totalfees is not None:
            query += "totalfees=%s, "
            values.append(totalfees)
        if penalty is not None:
            query += "penalty=%s, "
            values.append(penalty)
        if feespaid is not None:
            query += "feespaid=%s, "
            values.append(feespaid)
        if feesconcession is not None:
            query += "feesconcession=%s, "
            values.append(feesconcession)
        if balancefees is not None:
            query += "balancefees=%s, "
            values.append(balancefees)
        query = query.rstrip(", ")
        query += " WHERE rollno=%s"
        values.append(rollno)
        db.execute_query(query, tuple(values))
        logger.info("Fees updated successfully for Roll No %s", rollno)
        db.close_db()
    @staticmethod
    def delete_fees( rollno):  
        db.connect_db()
        query = "DELETE FROM FEES WHERE rollno=%s"
        db.execute_query(query, (rollno,))
        logger.info("Fees deleted successfully for Roll No %s", rollno)
        db.close_db()
    @staticmethod
    def view_fees(rollno):
        db.connect_db()
        query="SELECT * FROM FEES WHERE rollno=%s"
        result=db.fetch_query(query,(rollno,))
        db.close_db()
        if result:
            print("\nFees Details")
            print("-"*80)
            df=pd.DataFrame(result,columns=['rollno','totalfees','feespaid','penalty','feesconcession','balancefees'])
            print(df)
        else:
            print("No fees record found for Roll No:", rollno)
            return None


    @staticmethod
    def view_all_fees():
        db.connect_db()
        query="SELECT * FROM FEES"
        result=db.fetch_query(query)
        if result:
            print("\nAll Fees Records")
            print("-"*80)
            df=pd.DataFrame(result,columns=['rollno','totalfees','feespaid','penalty','feesconcession','balancefees'])
            print(df)
        else:
            print("No fees records found.")
            
        db.close_db()
    @staticmethod
    def view_fees_by_branch_sem(branch, sem):
        db.connect_db()
        query="SELECT s.rollno,s.name,f.totalfees,f.feespaid,f.penalty,f.feesconcession,f.balancefees FROM FEES f JOIN students s ON f.rollno = s.rollno WHERE s.branch=%s AND s.sem=%s"
        values=(branch,sem)
        result=db.fetch_query(query,values)
        db.close_db()
        if result:
            print(f"\nFees Records for Branch: {branch}, Semester: {sem}")
            print("-"*80)
            df=pd.DataFrame(result,columns=['rollno','totalfees','feespaid','penalty','feesconcession','balancefees','name','dob','fathername','mothername','sem','branch','phone','address'])
            print(df)
        else:
            print(f"No fees records found for Branch: {branch}, Semester: {sem}.")
            return None        
        
    @staticmethod
    def total_fee_collected():
        db.connect_db()
        query = "SELECT SUM(feespaid) FROM fees"
        result = db.fetch_query(query)
        db.close_db()
        return result[0][0] or 0
    @staticmethod
    def remained_fees():
        db.connect_db()
        query="SELECT SUM(balancefees) FROM fees"
        result=db.fetch_query(query)
        db.close_db()
        return result[0]
    