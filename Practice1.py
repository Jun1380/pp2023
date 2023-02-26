marks = []
courses = []
students = []
#list student
def list_students(students):
    for student in students:
        print("ID: ", student[0])
        print("Name: ", student[1])
        print("DoB: ", student[2])

#list courses
def list_courses(courses):
    for course in courses:
        print("Course ID: ", course[0])
        print("Course Name: ", course[1])

def total_student():
# Get the total students in the class:
    num_students = int(input("Please enter the total students: "))
    print("Total students: ", num_students)
    for i in range(num_students):
        student_info = input(f"Enter the ID, Name, DoB of student #{i + 1}: ").split()
        students.append([int(student_info[0]), student_info[1], student_info[2]])

def total_courses():
# Get the total courses:
    num_courses = int(input("Please enter the total courses: "))
    print("Total courses: ", num_courses)
    for i in range(num_courses):
        course_id = int(input("Enter the course ID: "))
        course_name = input("Enter the course name: ")
        courses.append((course_id, course_name))

#Get student's marks:
def get_stuMark():
    courses_id = int(input("Enter the course ID: "))
    student_id = int(input("Enter the student ID: "))
    mark = int(input("Enter the student's mark: "))
    marks.append([courses_id, student_id, mark])
def student_mark():
    courses_id = int(input("Enter the courses ID: "))
    for mark in marks:
        if mark[0] == courses_id:
            print("CoursesID, StudentID, Mark", marks[0])

while True:
    print("""Please choose an option below:
    0. Exit
    1. Enter the total students
    2. Enter the total courses
    3. Enter the student mark
    4. List all students
    5. List all courses
    6. Show student mark""")
    selection = int(input())
    if selection == 0:
        break
    elif selection == 1:
        total_student()
    elif selection == 2:
        total_courses()
    elif selection == 3:
        get_stuMark()
    elif selection == 4:
        list_students(students)
    elif selection == 5:
        list_courses(courses)
    elif selection == 6:
        student_mark()
    else:
        print("Invalid selection. Please try again.")

