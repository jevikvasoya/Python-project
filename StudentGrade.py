# initialize dictionary
student_grade = {}

#add new students
def add_student(name, grade):
    student_grade[name] = grade
    print(f"added {name} with a grade {grade}")

def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been succesfully deleted")
    else:
        print(f"{name} is not found")

def display_all_student():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("no student found")

def main():
    while True:
        print("\n student grade management system")
        print("1. add student")
        print("2. update student")
        print("3. delete student")
        print("4. view student")
        print("5. exit")

        choice = int(input("enter your choice = "))

        if choice == 1:
            name = input("enter student name = ")
            grade = int(input("enter studetn grade = "))
            add_student(name,grade)
        
        elif choice == 2:
            name = input("enter student name = ")
            grade = int(input("enter student grade"))
            update_student(name, grade)

        elif choice == 3:
            name = input("enter student name = ")   
            delete_student(name)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print("closing the program...")
            break

        else:
            print("invalid choice")
main()