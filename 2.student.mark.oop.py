class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def total_student(self):
        num_students = int(input("Please enter the total students: "))
        print("Total students: ", num_students)
        for i in range(num_students):
            student_info = input(f"Enter the ID, Name, DoB of student #{i + 1}: ").split()
            student = Student(int(student_info[0]), student_info[1], student_info[2])
            self.students.append(student)

    def total_courses(self):
        num_courses = int(input("Please enter the total courses: "))
        print("Total courses: ", num_courses)
        for i in range(num_courses):
            course_id = int(input("Enter the course ID: "))
            course_name = input("Enter the course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def get_stuMark(self):
        course_id = int(input("Enter the course ID: "))
        student_id = int(input("Enter the student ID: "))
        mark = int(input("Enter the student's mark: "))
        mark = Mark(course_id, student_id, mark)
        self.marks.append(mark)

    def list_students(self):
        for student in self.students:
            print("ID: ", student.student_id)
            print("Name: ", student.name)
            print("DoB: ", student.dob)

    def list_courses(self):
        for course in self.courses:
            print("Course ID: ", course.course_id)
            print("Course Name: ", course.name)

    def student_mark(self):
        course_id = int(input("Enter the course ID: "))
        for mark in self.marks:
            if mark.course_id == course_id:
                print("Course ID: ", mark.course_id)
                print("Student ID: ", mark.student_id)
                print("Mark: ", mark.mark)


school = School()

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
        school.total_student()
    elif selection == 2:
        school.total_courses()
    elif selection == 3:
        school.get_stuMark()
    elif selection == 4:
        school.list_students()
    elif selection == 5:
        school.list_courses()
    elif selection == 6:
        school.student_mark()
    else:
        print("Invalid selection. Please try again.")
