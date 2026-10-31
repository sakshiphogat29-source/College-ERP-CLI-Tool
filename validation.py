from datetime import datetime

def get_valid_input(prompt, validator, value=None):
    while True:
        try:
            if value is None:
                value = input(prompt)

            return validator(value)

        except ValueError as e:
            print(f"Error: {e}")
            value = input(prompt)
def validate_name(name):
    while True:
        name = name.strip()

        if name and any(char.isalpha() for char in name):
            return name

        print("Error: Please enter a valid name.")
        name = input("Name again: ")

def validate_sem(sem):
    try:
        sem = int(sem)
    except ValueError:
        raise ValueError("Semester must be a number.")

    if sem < 1 or sem > 8:
        raise ValueError("Semester must be between 1 and 8.")

    return sem

def validate_branch(branch):
    valid_branches = ["CSE", "ECE", "MECH", "CIVIL", "EEE","AI/ML","AI/DS"]
    if branch not in valid_branches:
        raise ValueError(f"Branch must be one of {', '.join(valid_branches)}.")

def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone number must be a 10-digit number.")

def validate_rollno(rollno):
    if not rollno.isdigit():
        raise ValueError("Roll number must be a 10-digit number.")

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str.strip(), "%d-%m-%Y")

        if date_obj.date() > datetime.today().date():
            raise ValueError("Date of birth cannot be in the future.")

        return date_obj

    except ValueError:
        raise ValueError("Date must be a valid date in DD-MM-YYYY format.")

def validate_subject_id(subject_id):
    if not subject_id.isdigit() or len(subject_id) != 5:
        raise ValueError("Subject ID must be a 5-digit number.")

def validate_status(status):
    valid_statuses = ["P", "A", "L", "V"]
    if status not in valid_statuses:
        raise ValueError(f"Status must be one of {', '.join(valid_statuses)}.")

