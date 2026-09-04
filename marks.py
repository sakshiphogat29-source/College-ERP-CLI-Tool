from student import Student
from database import db
from subjects import SubjectManagement
import pandas as pd
from logger import logger
class MarksManagement:

    @staticmethod
    def add_marks(sem, branch):
        logger.info("Adding marks for semester %s and branch %s", sem, branch)

        db.connect_db()

        
        subjects = SubjectManagement.get_subjects(sem, branch)

        if not subjects:
            print("No subjects found.")
            db.close_db()
            return

        print("\nAvailable Subjects")
        print("-" * 40)

        for subject_id, subject_name, subject_code in subjects:
            print(f"{subject_id}  {subject_name} ({subject_code})")

        subject_id = int(input("\nEnter Subject ID : "))

    
        if not SubjectManagement.subject_exists(subject_id):
            print("Invalid Subject ID.")
            db.close_db()
            return


        
        

        students = Student.get_students(sem, branch)

        print("\nEnter Marks")
        print("-" * 40)

        for rollno, name in students:

            print(f"\nRoll No : {rollno}")
            print(f"Name    : {name}")

            while True:
                internal = int(input("Internal Marks (0-30): "))
                if 0 <= internal <= 30:
                    break
                print("Invalid Internal Marks.")

            while True:
                external = int(input("External Marks (0-70): "))
                if 0 <= external <= 70:
                    break
                print("Invalid External Marks.")

            total = internal + external

            if total >= 90:
                grade = "A"
            elif total >= 80:
                grade = "B"
            elif total >= 65:
                grade = "C"
            elif total >= 50:
                grade = "D"
            elif total >= 35:
                grade = "E"
            else:
                grade = "F"

            insert_query = """
                INSERT INTO marks
                (rollno, subject_id, internal, external, total, grade)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                rollno,
                subject_id,
                internal,
                external,
                total,
                grade
            )

            db.execute_query(insert_query, values)

        db.close_db()

        logger.info("Marks added successfully.")

    @staticmethod
    def  view_marks(subject_id):
        db.connect_db()
        query="SELECT s.rollno,s.name,m.subject_id,m.internal,m.external,m.total,m.grade FROM marks m JOIN students s ON m.rollno=s.rollno WHERE subject_id=%s ORDER BY rollno"
        result=db.fetch_query(query,(subject_id,))
        df=pd.DataFrame(result,columns=['rollno','name','subject_id','internal','external','total','grade'])
        print(df)
        db.close_db()
        
    @staticmethod
    def update_marks(rollno,subject_id):
        db.connect_db()
        query="SELECT internal,external FROM marks WHERE rollno=%s AND subject_id=%s"
        result=db.fetch_query(query,(rollno,subject_id))
        if not result:
            print("No marks found for the given roll number and subject ID.")
            db.close_db()
            return
        else:
            current_internal=result[0][0]
            current_external=result[0][1]
            internal=int(input(f"Enter new internal marks (current: {current_internal}): "))
            external=int(input(f"Enter new external marks (current: {current_external}): "))
            if internal<0 or internal>30 or external<0 or external>70:
                print("Invalid marks entered.")
                db.close_db()
                return
            total=internal+external
            if total>=90:
                grade="A"
            elif total>=80:
                grade="B"
            elif total>=65:
                grade="C"
            elif total>=50:
                grade="D"
            elif total>=35:
                grade="E"
            else:
                grade="F"
            update_query="UPDATE marks SET internal=%s, external=%s, total=%s, grade=%s WHERE rollno=%s AND subject_id=%s"
            db.execute_query(update_query,(internal,external,total,grade,rollno,subject_id))
            logger.info("Marks updated successfully for Roll No %s and Subject ID %s", rollno, subject_id)
            db.close_db()

    @staticmethod
    def delete_marks(rollno,subject_id):
        db.connect_db()
        query="DELETE FROM marks WHERE rollno=%s AND subject_id=%s"
        db.execute_query(query,(rollno,subject_id))
        logger.info("Marks deleted successfully for Roll No %s and Subject ID %s", rollno, subject_id)
        db.close_db()
    @staticmethod
    def view_student_marks(rollno):
        db.connect_db()
        query="SELECT s.name,sub.subject_name,m.internal,m.external,m.total,m.grade FROM marks m JOIN students s ON m.rollno=s.rollno JOIN subjects sub ON m.subject_id=sub.subject_id WHERE m.rollno=%s"
        result=db.fetch_query(query,(rollno,))
        if not result:
            print("No marks found for the given roll number.")
            db.close_db()
            return
        else:
            df=pd.DataFrame(result,columns=['name','subject_name','internal','external','total','grade'])
            print(df)
            db.close_db()

    @staticmethod
    def student_average_marks(rollno):
        db.connect_db()
        query="SELECT AVG(total) FROM marks WHERE rollno=%s"
        result=db.fetch_query(query,(rollno,))
        if not result:
            print("No marks found for the given roll number.")
            db.close_db()
            return
        else:
            average=result[0][0]
            print(f"Average Marks for Roll No {rollno}: {average}")
            db.close_db()
    @staticmethod
    def subject_average_marks(subject_id):
        db.connect_db()
        query="SELECT AVG(total) FROM marks WHERE subject_id=%s"
        result=db.fetch_query(query,(subject_id,))
        if not result:
            print("No marks found for the given subject ID.")
            db.close_db()
            return
        else:
            average=result[0][0]
            print(f"Average Marks for Subject ID {subject_id}: {average}")
            db.close_db()
    @staticmethod
    def overall_average_marks():
        db.connect_db()
        query="SELECT AVG(total) FROM marks"
        result=db.fetch_query(query)
        if not result:
            print("No marks found.")
            db.close_db()
            return
        else:
            average=result[0][0]
            print(f"Overall Average Marks: {average}")
            db.close_db()
    @staticmethod
    def add_marks_by_rollno(rollno,subject_id,internal,external):
        db.connect_db()
        total=internal+external
        if total>=90:
            grade="A"
        elif total>=80:
            grade="B"
        elif total>=65:
            grade="C"
        elif total>=50:
            grade="D"
        elif total>=35:
            grade="E"
        else:
            grade="F"
        insert_query="INSERT INTO marks (rollno,subject_id,internal,external,total,grade) VALUES (%s,%s,%s,%s,%s,%s)"
        db.execute_query(insert_query,(rollno,subject_id,internal,external,total,grade))
        logger.info("Marks added successfully for Roll No %s and Subject ID %s", rollno, subject_id)
        db.close_db()
    @staticmethod
    def topper_in_subject(subject_id):
        db.connect_db()
        query="SELECT s.rollno,s.name,m.total FROM marks m JOIN students s ON m.rollno=s.rollno WHERE m.subject_id=%s ORDER BY m.total DESC LIMIT 3"
        result=db.fetch_query(query,(subject_id,))
        if not result:
            print("No marks found for the given subject ID.")
            db.close_db()
            return
        else:
            df=pd.DataFrame(result,columns=['rollno','name','total'])
            print(df)
            db.close_db()

    @staticmethod
    def topper_in_semester(sem,branch): 
        db.connect_db()
        query="SELECT s.rollno,s.name,AVG(m.total) as avg_total FROM marks m JOIN students s ON m.rollno=s.rollno WHERE s.sem=%s AND s.branch=%s GROUP BY s.rollno,s.name ORDER BY avg_total DESC LIMIT 3"           
        result=db.fetch_query(query,(sem,branch))
        if not result:
            print("No marks found for the given semester and branch.")
            db.close_db()
            return
        else:
            df=pd.DataFrame(result,columns=['rollno','name','avg_total'])
            print(df)
            db.close_db()
    @staticmethod
    def calculate_percentage(rollno):
        db.connect_db()
        query="SELECT (SUM(total)/COUNT(*)) as percentage FROM marks WHERE rollno=%s"
        result=db.fetch_query(query,(rollno,))
        if not result:
            print("No marks found for the given roll number.")
            db.close_db()
            return
        else:
            percentage=result[0][0]
            print(f"Percentage for Roll No {rollno}: {percentage}")
            db.close_db()
    @staticmethod
    def failed_students(sem,branch):
        db.connect_db()
        query="SELECT s.rollno,s.name,AVG(m.total) as avg_total FROM marks m JOIN students s ON m.rollno=s.rollno WHERE s.sem=%s AND s.branch=%s GROUP BY s.rollno,s.name HAVING AVG(m.total)<35"
        result=db.fetch_query(query,(sem,branch))
        if not result:
            print("No failed students found for the given semester and branch.")
            db.close_db()
            return
        else:
            df=pd.DataFrame(result,columns=['rollno','name','avg_total'])
            print(df)
            db.close_db()
    @staticmethod
    def class_average(sem,branch):
        db.connect_db()
        query="SELECT AVG(m.total) as class_average FROM marks m JOIN students s ON m.rollno=s.rollno WHERE s.sem=%s AND s.branch=%s"
        result=db.fetch_query(query,(sem,branch))
        if not result:
            print("No marks found for the given semester and branch.")
            db.close_db()
            return
        else:
            average=result[0][0]
            print(f"Class Average for Semester {sem} and Branch {branch}: {average}")
            db.close_db()


    @staticmethod
    def view_marks_by_sem_branch(sem,branch):
        db.connect_db()
        query="SELECT s.rollno,s.name,sub.subject_name,m.internal,m.external,m.total,m.grade FROM marks m JOIN students s ON m.rollno=s.rollno JOIN subjects sub ON m.subject_id=sub.subject_id WHERE s.sem=%s AND s.branch=%s ORDER BY s.rollno"
        result=db.fetch_query(query,(sem,branch))
        if not result:
            print("No marks found for the given semester and branch.")
            db.close_db()
            return
        else:
            df=pd.DataFrame(result,columns=['rollno','name','subject_name','internal','external','total','grade'])
            print(df)
            db.close_db()     

    @staticmethod
    def view_all_marks():
        db.connect_db()
        query="SELECT * FROM marks"
        result=db.fetch_query(query) 
        if result and result[0]:
          df=pd.DataFrame(result,columns=['rollno','subject_id','internal','external','total','grade'])
          print(df)
        else:
            print("No marks record found .")  
        db.close_db()          
            