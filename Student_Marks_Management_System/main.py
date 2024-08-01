student_details = {}

def show_Details():
    print("All Student Details List")
    for student, mark in student_details.items():
        print(f"{student} : {mark}")
    
def add_Student_Details(student, marks):
    student_details[student] = marks
    print(f"Student Name is {student} and obtain marks is {marks} added successfully")
    
    
def update_Student_Details(student, marks):
    if student in student_details:
        student_details[student] = marks
        print(f"Student Name is {student} and obtain marks is {marks} updated successfully")
    else:
        print(f'{student} name is not found!')

def remove_student_details(student):
    student_details.pop(student)
    
    
    
    
def main():
    while True:
        print("Student Marks Management System")
        print("1. Show All Student Details")
        print("2. Add Student Details")
        print("3. Update Student Details")
        print("4. Romove Student Details")
        print("5. Save/Exits")
        
        choice = input("Enter Your Choice (1-5) : ")
        
        if choice == '1':
            show_Details()
        
        elif choice == '2':
            student = input("Enter Student Name : ")
            marks = input("Enter Student Marks : ")
            add_Student_Details(student, marks)
            
        
        elif choice == '3':
            studentName = input("Enter Student Name : ")
            studentMarks = input("Enter Student Marks : ")
            update_Student_Details(studentName, studentMarks)
            show_Details()
        
        
        elif choice == '4':
            student = input("Enter student name you want to remove : ")
            print(f"{student} is remove successfully")
            remove_student_details(student)
        
        
        elif choice == '5':
            print("Closing this app......")
            break
        else:
            print("Syntax errors please choose correct option (1-5) ")

if __name__ == "__main__":
    main()