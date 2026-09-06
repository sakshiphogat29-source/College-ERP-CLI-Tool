import mysql.connector
import os
from dotenv import load_dotenv
from logger import logger
load_dotenv()
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_PASSWORD:", "SET" if os.getenv("DB_PASSWORD") else "NOT SET")

class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

        self.conn = None
        self.cursor = None
    def create_db(self):
        try:
           self.conn = mysql.connector.connect(host=self.host,user=self.user,password=self.password) 
           self.cursor = self.conn.cursor()
           self.cursor.execute("CREATE DATABASE IF NOT EXISTS studentdatabase")
           
        except mysql.connector.Error as e:
            logger.error(f"Error in creating the database\n Error:{e}.")
    def connect_db(self):
        try:
            self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor=self.conn.cursor()
            logger.info("Connected to the student database.")

        except mysql.connector.Error as e:
            print(f"Error in connecting to the database\n Error:{e}.")
            logger.error(f"Error in connecting to the database\n Error:{e}.")      
    def close_db(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        
    def execute_query(self,query,values=None):       
        try:
            if values:
                self.cursor.execute(query,values)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error in executing the query\n Error:{e}.")
            logger.error(f"Error in executing the query\n Error:{e}.")
            return False
        
    def fetch_query(self,query,values=None):
        try:
            if values:
              self.cursor.execute(query,values)
              result=self.cursor.fetchall()
              return result
            else: 
              self.cursor.execute(query) 
              result=self.cursor.fetchall() 
              return result 
        except mysql.connector.Error as e:
            logger.error(f"Error in fetching the query\n Error:{e}.")

    def create_table(self):
        
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS students( rollno INT , name VARCHAR(50) NOT NULL , DOB DATE , fathername VARCHAR(50), mothername VARCHAR(50), sem INT, branch VARCHAR(10), phone VARCHAR(15), address VARCHAR(50),password VARCHAR(20),PRIMARY KEY(rollno))") 
            self.cursor.execute("CREATE TABLE IF NOT EXISTS subjects(subject_id INT ,subject_name VARCHAR(50) NOT NULL,subject_code VARCHAR(20),credits INT , branch VARCHAR(20),sem INT,PRIMARY KEY(subject_id))  ")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS fees(rollno INT,totalfees INT,feespaid INT,penalty INT,feesconcession INT,balancefees INT, PRIMARY KEY(rollno), FOREIGN KEY(rollno) REFERENCES students(rollno))")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS marks(rollno INT,subject_id INT,internal INT,external INT, total INT, grade CHAR(2), PRIMARY KEY(rollno, subject_id),FOREIGN KEY(rollno) REFERENCES students(rollno), FOREIGN KEY(subject_id) REFERENCES subjects(subject_id));")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS attendancetable( rollno INT,attendance_date DATE DEFAULT(CURRENT_DATE),status VARCHAR(20),subject_id int,sem INT,branch VARCHAR(10), PRIMARY KEY(rollno,attendance_date,subject_id), FOREIGN KEY(rollno) REFERENCES students(rollno), FOREIGN KEY(subject_id) REFERENCES subjects(subject_id) )")
            
        except mysql.connector.Error as e:
            logger.error(f"Error in creating the table Error:{e}.")  

              
    
db=Database()
db.create_db()
db.connect_db()
db.create_table()


