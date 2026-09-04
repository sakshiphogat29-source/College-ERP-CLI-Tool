from database import db
from getpass import getpass
from logger import logger
def student_login(username, password):
    db.connect_db()
    query = "SELECT password FROM students WHERE rollno=%s"
    result = db.fetch_query(query, (username,))
    db.close_db()
    
    if result:
        if result[0][0] == password:
            return True
        else:
            print("wrong password.")
            logger.warning("Failed login attempt for Roll No %s", username)
    else:
        print("Username not found.")
        logger.warning("Login attempt with unknown username: %s", username)
        db.close_db()    
def reset_password(username):
    db.connect_db()
    query = """
    SELECT dob, fathername, mothername
    FROM students
    WHERE rollno = %s
    """
    result=db.fetch_query(query, (username,))
    

    if result:
        dob = input("Enter DOB (YYYY-MM-DD): ")
        father = input("Enter father's name: ")
        mother = input("Enter mother's name: ")

        if str(result[0][0]) == dob and result[0][1].lower() == father.lower() and result[0][2].lower() == mother.lower():
            new_password = getpass("Enter new password: ")

            db.execute_query(
                "UPDATE students SET password = %s WHERE rollno = %s",
                (new_password, username))
            print("Password reset successfully.")
            logger.info("Password reset successfully for Roll No %s", username)
        else:
            print("Verification failed.")
    else:
        print("Username not found.")
    db.close_db()    

def admin_login(username, password):
    if username.lower()=="admin" and password=="1234abc":
        logger.info("Admin login successful.")
        return True 
        
    else:
        print("INVALID CREDENTIALS .... TRY AGAIN ") 
        logger.warning("Failed admin login attempt with username: %s", username)
                           

    