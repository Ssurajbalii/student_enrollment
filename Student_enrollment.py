"""
Assignment 6
Student enrollment system

This is a fully functional program that will take student data
and will automatically create a file that will store all the student
data in binary in your system. File name will be "Student_data.pkl"
if you want te see the data just at the start of the program type
"student data" to get a dictionary of all the students you have created

Created on Sat Nov 25 23:14:35 2023

@author: suraj

"""
import pickle

# importing pickle so that i can store data locally

user_data = {}

# Creating empty dictionary to store data
# defining all the functions at the start

def new_student(name, age, email, password):
    """
    This function adds the student data to the dictionary.

    :param name: Name of the student
    :param age: Age of the student
    :param email: email of the student
    :param password: Password to access user data later

    :return: it will add a new user to our dictionary.
    """
    global student_number
    global user_data
    try:
        with open("Student_data.pkl", "rb") as f:
            user_data = pickle.load(f)
    except FileNotFoundError:
        pass

    student_number = len(user_data) + 1

    user_data[student_number] = {'name': name, 'age': age, 'email': email, 'pass': password,
                                 'candidate': 1, 'approved': 0, 'enrolled': 0}

    with open("Student_data.pkl", "wb") as f:
        pickle.dump(user_data, f)


def approved_student(student_number):
    """
    This function is used to update student status

    :param student_number: The student number will be needed to do so
    :return: this will update the student status from candidate to approved
    """
    global user_data

    with open("Student_data.pkl", 'rb') as f:
        user_data = pickle.load(f)

    user_data[student_number]['candidate'] = 0
    user_data[student_number]['approved'] = 1

    with open("Student_data.pkl", 'wb') as f:
        pickle.dump(user_data, f)


def enrolled_student(student_number):
    """
    This function will update the student status
    :param student_number: it will need student number to do so
    :return: It will make student status from approved to enrolled
    """
    global user_data

    with open("Student_data.pkl", 'rb') as f:
        user_data = pickle.load(f)

    user_data[student_number]['enrolled'] = 1
    user_data[student_number]['approved'] = 0

    with open("Student_data.pkl", 'wb') as f:
        pickle.dump(user_data, f)


def find_student(std_id, std_pass):
    """
    this function will find the student data by taking student
    number and password from the student and will then continue
    with the remaining steps

    :param std_id: student number
    :param std_pass: Password which the student
    set when making their account.
    :return: it will return the student data and their
    current status will be displayed.
    """
    try:
        with open("Student_data.pkl", 'rb') as f:
            user_data = pickle.load(f)

        try:
            if std_id in user_data:
                if user_data[std_id]['pass'] == std_pass:
                    print("Access Granted")
                    print("User data:")
                    student_status()
                    for key, value in user_data[std_id].items():
                        if key == 'pass':
                            break
                        print(f"{key}: {value}")

                    if user_data[std_id]['candidate'] :
                        continue_application()

                        decision1 = input("Press Enter to upload your documents")

                        while True:
                            nrml_decision = input("Have you Uploaded Your "
                                                  "documents").lower().strip()
                            if nrml_decision == "yes" or nrml_decision == "y":
                                approved_student(std_id)
                                break
                            elif nrml_decision == "no" or nrml_decision == "n":
                                print("Please Upload your Documents First")
                            else:
                                print("Invalid Input")
                                print("\nAnswer in Yes or No")

                        print("\nYour Current Status is")
                        student_status(std_id)
                        continue_application()

                        # Asking user to pay Fees

                        print("Let's Continue With Paying your fees")

                        fees_calculator()

                        while True:

                            try:
                                fee = input("Type Pay to pay the "
                                            "fees:- ").strip().lower()
                                if fee != "pay":
                                    raise ValueError("Fees Not Paid! "
                                                     "Try again.")

                                break
                            except ValueError as e:
                                print(e)

                        enrolled_student(std_id)
                        student_status(std_id)

                        print("\nCongratulations! "
                              "You are now a student of RRC.")
                        exit()

                    elif user_data[std_id]['approved']:
                        continue_application()

                        # Asking user to pay Fees

                        print("Let's Continue With Paying your fees")

                        fees_calculator()

                        while True:

                            try:
                                fee = input("Type Pay to pay "
                                            "the fees:- ").strip().lower()
                                if fee != "pay":
                                    raise ValueError("Fees Not Paid! Try again.")

                                break
                            except ValueError as e:
                                print(e)

                        enrolled_student(std_id)
                        student_status(std_id)

                        print("\nCongratulations! You "
                              "are now a student of RRC.")
                        exit()

                    elif user_data[std_id]['enrolled']:
                        print("\nCongratulations! You are now a student of RRC.")
                        exit()

                else:
                    print("Password Does not match")
            else:
                raise KeyError


        except KeyError:
            print("Student Not Found")


    except FileNotFoundError:
        print("Student Data invalid")
        print("Try Creating a new account")


def student_status(std_id):
    """
    this is a pretty basic function just to print the current student status

    :param std_id: Student number
    :return: It will return the current student status
    """
    with open("Student_data.pkl", "rb") as f:
        user_data = pickle.load(f)

    if user_data[std_id]["candidate"]:
        print("Current Status : Candidate")
    elif user_data[std_id]["approved"]:
        print("Current Status : Approved Student")
    elif user_data[std_id]["enrolled"]:
        print("Current Status : Enrolled Student")


def continue_application():
    """
    This is a basic function just to ask user if the want
    to continue their application or not

    :return: if yes then continue else exit the code
    """

    while True:
        decision_1 = input("Do you want to continue your application :- ").lower().strip()
        if decision_1 == "yes":
            break
        elif decision_1 == "no":
            print("Thanks for Visiting")
            exit()
        else:
            print("Invalid Output")


def fees_calculator():
    tuition_fee = 1000
    course_fee = 200
    tax_rate = 5
    discount = 15

    taken_courses = int(input("Number of courses you had taken :- "))

    total_fees = tuition_fee + (taken_courses * course_fee)

    tax_amount = total_fees * (tax_rate / 100)

    discount_calculated = (taken_courses > 5) * (total_fees * (discount / 100))

    total_with_tax = total_fees + int(tax_amount) - discount_calculated

    print("Your estimated fees is :- ", total_fees)
    print("\nYour total tax is :- ", int(tax_amount))
    print("\ndiscount is :- ", discount_calculated)
    print("\nYour Total fee is :- ", total_with_tax)


# This is where the program starts

print("Welcome To Red River College".center(80))

user_sign_in = ""
student_number = ""

# using a while loop to make sure that user enter right value

while True:
    user_sign_in: str = input(" Do you have an account :- ").lower().strip()
    print("You entered :", user_sign_in)
    if user_sign_in == "yes" or user_sign_in == "no" or user_sign_in == "y" or user_sign_in == "n"\
            or user_sign_in == "student data":
        break
    else:
        print("Invalid output")

# Asking user if they already have an account or not.

if user_sign_in == 'no' or user_sign_in == 'n':

    # taking input from the user
    print("Let's Create an account")
    email = input("Email :- ").lower().strip()
    first_name = input("First Name :- ").title().strip()
    last_name = input("Last Name :- ").title().strip()

    while True:
        try:
            age = int(input("Age :- "))
            break
        except ValueError:
            print(" Invalid Age ")

    name = first_name + " " + last_name

    print("Password must meet the following criteria:\n"
          "- At least one number\n"
          "- At least one uppercase letter\n"
          "- Minimum length of 5 characters\n")

    while True:
        user_password = input('Password :- ')

        if not any(i.isnumeric() for i in user_password):
            print("Password must contain a digit")
            print("Try again")
            continue
        else:
            pass

        if not len(user_password) >= 5:
            print("Password must be at least 5 ")
            continue
        else:
            pass

        if not any(i.isupper() for i in user_password):
            print("Password must contain an Upper Case")
            continue
        else:
            print("Password accepted")
            break

    # Try adding a confirm password section

    new_student(name, age, email, user_password)

    print("your Student Number is :- ", student_number)

    student_status(student_number)

    continue_application()

    decision1 = input("Press Enter to upload your documents")

    while True:
        nrml_decision = input("Have you Uploaded Your documents").lower().strip()
        if nrml_decision == "yes" or nrml_decision == "y":
            approved_student(student_number)
            break
        elif nrml_decision == "no" or nrml_decision == "n":
            print("Please Upload your Documents First")
        else:
            print("Invalid Input")
            print("\nAnswer in Yes or No")

    print("\nYour Current Status is")
    student_status(student_number)

    continue_application()

    # Asking user to pay Fees

    print("Let's Continue With Paying your fees")


    fees_calculator()

    while True:

        try:
            fee = input("Type Pay to pay the fees:- ").strip().lower()
            if fee != "pay":
                raise ValueError("Fees Not Paid! Try again.")

            break
        except ValueError as e:
            print(e)

    enrolled_student(student_number)
    student_status(student_number)

    print("\nCongratulations! You are now a student of RRC.")

elif user_sign_in == "yes" or user_sign_in == "y":

    while True:
        try:
            std_id = int(input("Enter your Student Number :- "))
            break
        except ValueError:
            print("Invalid Student Number")

    user_pass = input("Enter Your Password :-")

    find_student(std_id, user_pass)

elif user_sign_in == "student data":
    try:
        with open("Student_data.pkl") as f :
            user_data = pickle.load(f)
            print(user_data)
    except FileNotFoundError:
        print("Your Student data is empty")
        print("Try Creating an account first")


print()
