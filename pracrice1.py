nos = int(input("Please enter the number of students in a class"))
i = 1
print("Total students:", nos)


def class_infor():
    # nos = int(input("Please enter the number of students in a class"))
    # print("Total students:", nos)
    studentInfor = map(lambda x: [int(x[0]),x[1],x[2]], [input("Enter the ID, Name, DoB of student: ").split()])
    print(list(studentInfor))

while i <= nos:
        class_infor()
        i+= 1



