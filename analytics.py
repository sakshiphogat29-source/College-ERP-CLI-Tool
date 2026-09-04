from database import db
import matplotlib.pyplot as plt
import pandas as pd
from logger import logger

def student_strength():
    db.connect_db()
    query = "SELECT sem, COUNT(*) as strength FROM students  GROUP BY sem"
    result = db.fetch_query(query)
    db.close_db()
    if result:
        df = pd.DataFrame(result, columns=['sem', 'strength'])
        plt.bar(df['sem'], df['strength'])
        plt.xlabel('Semester')
        plt.ylabel('Number of Students')
        plt.title('Student Strength by Semester')
        plt.show()

def student_strength_by_branch():
    db.connect_db()
    query = "SELECT branch, COUNT(*) as strength FROM students GROUP BY branch"
    result = db.fetch_query(query)
    db.close_db()
    if result:
        df = pd.DataFrame(result, columns=['branch', 'strength'])
        plt.bar(df['branch'], df['strength'])
        plt.xlabel('Branch')
        plt.ylabel('Number of Students')
        plt.title('Student Strength by Branch')
        plt.show()

def student_strength_by_sem_and_branch():
    db.connect_db()
    query = "SELECT s.sem, s.branch, COUNT(*) as strength FROM students s GROUP BY s.sem, s.branch"
    result = db.fetch_query(query)
    db.close_db()
    if result:
        df = pd.DataFrame(result, columns=['sem', 'branch', 'strength'])
        pivot_df = df.pivot(index='sem', columns='branch', values='strength').fillna(0)
        pivot_df.plot(kind='bar', stacked=True)
        plt.xlabel('Semester')
        plt.ylabel('Number of Students')
        plt.title('Student Strength by Semester and Branch')
        plt.legend(title='Branch')
        plt.show()
        logger.info("Student strength analysis viewed")

def marks_analysis():
    db.connect_db()
    query = "SELECT s.sem, s.branch, AVG(m.total) as avg_marks FROM students s JOIN marks m ON s.rollno = m.rollno GROUP BY s.sem, s.branch"
    result = db.fetch_query(query)
    db.close_db()
    if result:
        df = pd.DataFrame(result, columns=['sem', 'branch', 'avg_marks'])
        df['avg_marks'] = pd.to_numeric(df['avg_marks'])
        pivot_df = df.pivot(index='sem', columns='branch', values='avg_marks').fillna(0)
        print(df)
        print(pivot_df)
        pivot_df.plot(kind='bar')
        plt.xlabel('Semester')
        plt.ylabel('Average Marks')
        plt.title('Average Marks by Semester and Branch')
        plt.legend(title='Branch')
        plt.show()
        logger.info("marks analysis viewed")

def attendance_analysis():
    db.connect_db()

    query = "SELECT s.sem, s.branch, ROUND(SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as avg_attendance FROM students s JOIN attendancetable a ON s.rollno = a.rollno GROUP BY s.sem, s.branch"

    result = db.fetch_query(query)
    db.close_db()
    if result:
        df = pd.DataFrame(result, columns=['sem', 'branch', 'avg_attendance'])
        df['avg_attendance'] = df['avg_attendance'].astype(float)
        pivot_df = df.pivot(index='sem', columns='branch', values='avg_attendance').fillna(0)
        print("---- DEBUG ----")
        print(pivot_df.dtypes)
        print(pivot_df.to_numpy().dtype)
        print(type(pivot_df.iloc[0, 0]))
        print(result)
        print(df)
        print(df.dtypes)
        print(type(df['avg_attendance'].iloc[0]))
        
        

        print(pivot_df)
        pivot_df.plot(kind='bar')
        plt.xlabel('Semester')
        plt.ylabel('Average Attendance')
        plt.title('Average Attendance by Semester and Branch')
        plt.legend(title='Branch')
        plt.show()
        logger.info("Attendance analysis viewed")

def student_performance_analysis():
    db.connect_db()
    marks_result = db.fetch_query("SELECT s.sem, s.branch, AVG(m.total) as avg_marks FROM students s JOIN marks m ON s.rollno = m.rollno GROUP BY s.sem, s.branch")
    attendance_result = db.fetch_query("SELECT s.sem, s.branch, ROUND(SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as avg_attendance FROM students s JOIN attendancetable a ON s.rollno = a.rollno GROUP BY s.sem, s.branch")
    db.close_db()
    if marks_result and attendance_result:
        marks_df = pd.DataFrame(marks_result, columns=['sem', 'branch', 'avg_marks'])
        marks_df['avg_marks'] = pd.to_numeric(marks_df['avg_marks'])
        attendance_df = pd.DataFrame(attendance_result,columns=['sem','branch','avg_attendance'])
        attendance_df['avg_attendance'] = pd.to_numeric(attendance_df['avg_attendance'])
        mdf= pd.merge(marks_df,attendance_df,on=['sem','branch'],how='outer')
        pivot_df =mdf.pivot(index='sem', columns='branch', values=['avg_marks', 'avg_attendance']).fillna(0)
        print(pivot_df)
        pivot_df.plot(kind='bar')
        plt.xlabel('Semester')
        plt.ylabel('Average Marks and Attendance')
        plt.title('Student Performance Analysis by Semester and Branch')
        plt.legend(title='Branch')
        plt.show()
        logger.info("Student performance analysis viewed.")
  

def fees_analysis():
    db.connect_db()
    query = "SELECT s.sem, s.branch, AVG(f.feespaid) as  avg_fees FROM students s JOIN fees f ON s.rollno = f.rollno  GROUP BY s.sem, s.branch"
    result = db.fetch_query(query)
    db.close_db()
    if result:
        df = pd.DataFrame(result, columns=['sem', 'branch', 'avg_fees'])
        df['avg_fees'] = pd.to_numeric(df['avg_fees'])
        pivot_df = df.pivot(index='sem', columns='branch', values='avg_fees').fillna(0)
        print(pivot_df)
        pivot_df.plot(kind='bar')
        plt.xlabel('Semester')
        plt.ylabel('Average Fees')
        plt.title('Average Fees by Semester and Branch')
        plt.legend(title='Branch')
        plt.show()
        logger.info("Fees analysis viewed.")


def risk_analysis():
    db.connect_db()

    marks_result = db.fetch_query("""
        SELECT s.rollno, s.name, AVG(m.total) AS avg_marks
        FROM students s
        JOIN marks m ON s.rollno = m.rollno
        GROUP BY s.rollno, s.name
    """)

    attendance_result = db.fetch_query("""
        SELECT s.rollno, s.name,
               ROUND(
                   SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END)
                   * 100.0 / COUNT(*), 2
               ) AS avg_attendance
        FROM students s
        JOIN attendancetable a ON s.rollno = a.rollno
        GROUP BY s.rollno, s.name
    """)

    db.close_db()

    if not marks_result or not attendance_result:
        print("Not enough data to run risk analysis yet.")
        return

    marks_df = pd.DataFrame(
        marks_result,
        columns=['rollno', 'name', 'avg_marks']
    )

    att_df = pd.DataFrame(
        attendance_result,
        columns=['rollno', 'name', 'avg_attendance']
    )

    
    merged = pd.merge(
        marks_df,
        att_df,
        on=['rollno', 'name'],
        how='inner'
    )

    # Make sure values are numeric
    merged['avg_marks'] = pd.to_numeric(merged['avg_marks'])
    merged['avg_attendance'] = pd.to_numeric(merged['avg_attendance'])

    # Identify at-risk students
    merged['at_risk'] = (
        (merged['avg_marks'] < 35) |
        (merged['avg_attendance'] < 75)
    )

    
    at_risk_students = merged[merged['at_risk']]

    print("\n===== STUDENTS AT RISK =====")

    if at_risk_students.empty:
        print("No students are currently at risk.")
    else:
        for _, student in at_risk_students.iterrows():
            print(
                f"Roll No: {student['rollno']} | "
                f"Name: {student['name']} | "
                f"Marks: {student['avg_marks']:.2f} | "
                f"Attendance: {student['avg_attendance']:.2f}%"
            )

    
    plt.scatter(
        merged['avg_attendance'],
        merged['avg_marks']
    )

    plt.xlabel('Attendance %')
    plt.ylabel('Average Marks')
    plt.title('Student Risk Analysis')
    plt.show()

    at_risk_count = len(at_risk_students)

    print(
        f"\n{at_risk_count} student(s) flagged at risk "
        "(marks < 35 or attendance < 75%)."
    )

    logger.info(
        "Risk analysis viewed. %s students flagged at risk.",
        at_risk_count
    )