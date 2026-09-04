from database import db
from student import Student
from datetime import date
import pandas as pd
from subjects import SubjectManagement
from logger import logger

def mark_attendance(sem,branch,subject_id):
    today = date.today()
    db.connect_db()
    
    query = """
        SELECT rollno,name FROM students
        WHERE sem = %s AND branch = %s
        ORDER BY rollno
    """
    values = (sem,branch)
    result = db.fetch_query(query,values)
    

    print("\nAttendance Date:", today)
    print("-" * 40)


    for student in result:

        rollno = student[0]
        name = student[1]
        

        status = input(f"{rollno} - {name} (P/A/L/V): ").upper()

        status_map = {
            "P": "Present",
            "A": "Absent",
            "L": "Late",
            "V": "Leave"
        }

        status = status_map.get(status, "Absent")

        

        

        query = """
            INSERT INTO attendancetable
            (rollno,attendance_date, status,subject_id,sem,branch)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        values=(rollno,today,status,subject_id,sem,branch)
        db.execute_query(query,values)
    db.close_db()
    if not result:
        print("No student records found.")

    else:
        logger.info("Attendance marked successfully for Semester %s, Branch %s", sem, branch)
        print("\nAttendance Saved Successfully!\n")



def view_attendance_by_sem_branch(sem,branch):
    db.connect_db()
    query =  """
        SELECT
            s.rollno,
            s.name,
            a.attendance_date,
            a.status
        FROM attendancetable a
        JOIN students s
            ON a.rollno = s.rollno
        WHERE s.sem = %s AND s.branch = %s
        ORDER BY a.attendance_date DESC, s.rollno
    """

    result = db.fetch_query(query, (sem, branch))

    print("\nAttendance Records")
    print("-"*80)
    df=pd.DataFrame(result,columns=['rollno','name','attendance_date','status'])
    print(df)
    db.close_db()

        
def view_attendance_by_subject(subject_id):
    db.connect_db()
    subject=SubjectManagement.get_subject_name(subject_id)
    print(f"Attendance Records for Subject: {subject[1]} (ID: {subject[0]})")
    query="SELECT * FROM attendancetable WHERE subject_id=%s ORDER BY rollno"
    values=(subject_id,)
    result=db.fetch_query(query,values)
    df=pd.DataFrame(result,columns=['rollno','name','attendance_date','status'])
    print(df)
    db.close_db()
def find_defaulter_student(sem,branch):
    db.connect_db()

    query="SELECT rollno,name FROM students WHERE sem=%s and branch=%s ORDER BY  rollno "
    values=(sem,branch)
    result=db.fetch_query(query,values)
    defaulters=[]
    for rollno,name in result:
        percentage=attendance_percentage(rollno)
        if percentage < 75:
            defaulters.append((rollno,name,percentage))
    defaulters.sort(key=lambda x:x[2])
    db.close_db()
    return defaulters        
def attendance_percentage(rollno):
    db.connect_db()
    query=" SELECT ROUND(SUM(CASE WHEN status='Present' THEN 1 ELSE 0 END)*100.0/NULLIF(COUNT(*),0),2) AS attendance_percentage from attendancetable where rollno=%s"
    result=db.fetch_query(query,(rollno,))
    db.close_db()
    if result and result[0][0] is not None:
        return result[0][0]

    return 0
def monthly_report(month,year,subject_id):
    db.connect_db()
    query="SELECT s.rollno,s.name,ROUND(SUM(CASE WHEN a.status='Present' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS attendance_percentage FROM students s join attendancetable a on s.rollno=a.rollno WHERE MONTH(a.attendance_date)=%s AND YEAR(a.attendance_date)=%s AND subject_id=%s GROUP BY s.rollno,s.name ORDER BY attendance_percentage DESC"
    result=db.fetch_query(query,(month,year,subject_id))
    db.close_db()
    return result  

def view_attendance_by(rollno):
    db.connect_db()

    query = """
        SELECT
            a.rollno,
            s.name,
            a.attendance_date,
            a.status,
            a.subject_id,
            a.sem,
            a.branch
        FROM attendancetable a
        JOIN students s
            ON a.rollno = s.rollno
        WHERE a.rollno = %s
        ORDER BY a.attendance_date DESC
    """

    result = db.fetch_query(query, (rollno,))

    if result:
        df = pd.DataFrame(
            result,
            columns=[
                'rollno',
                'name',
                'attendance_date',
                'status',
                'subject_id',
                'sem',
                'branch'
            ]
        )
        print(df)
    else:
        print("No attendance records found.")

    db.close_db()
   

       


