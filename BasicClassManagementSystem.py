class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Class:
    def __init__(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name

class Student:
    def __init__(self, student_id, student_name, class_id):
        self.student_id = student_id
        self.student_name = student_name
        self.class_id = class_id

class Teacher:
    def __init__(self, teacher_id, teacher_name, class_id):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.class_id = class_id

class BasicClassManagementSystem:
    def __init__(self):
        self.users = []
        self.classes = []
        self.students = []
        self.teachers = []
        self.current_user = None

    def add_user(self, username, password, role):
        self.users.append(User(username, password, role))

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                return True
        return False

    def add_class(self, class_id, class_name):
        if self.current_user and self.current_user.role == 'admin':
            self.classes.append(Class(class_id, class_name))
        else:
            print("Unauthorized action")

    def view_classes(self):
        for cls in self.classes:
            print(f"Class ID: {cls.class_id}, Class Name: {cls.class_name}")

    def delete_class(self, class_id):
        if self.current_user and self.current_user.role == 'admin':
            self.classes = [cls for cls in self.classes if cls.class_id != class_id]
        else:
            print("Unauthorized action")

    def add_student(self, student_id, student_name, class_id):
        if self.current_user and self.current_user.role == 'admin':
            self.students.append(Student(student_id, student_name, class_id))
        else:
            print("Unauthorized action")

    def view_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Student Name: {student.student_name}, Class ID: {student.class_id}")

    def delete_student(self, student_id):
        if self.current_user and self.current_user.role == 'admin':
            self.students = [student for student in self.students if student.student_id != student_id]
        else:
            print("Unauthorized action")

    def add_teacher(self, teacher_id, teacher_name, class_id):
        if self.current_user and self.current_user.role == 'admin':
            self.teachers.append(Teacher(teacher_id, teacher_name, class_id))
        else:
            print("Unauthorized action")

    def view_teachers(self):
        for teacher in self.teachers:
            print(f"Teacher ID: {teacher.teacher_id}, Teacher Name: {teacher.teacher_name}, Class ID: {teacher.class_id}")

    def delete_teacher(self, teacher_id):
        if self.current_user and self.current_user.role == 'admin':
            self.teachers = [teacher for teacher in self.teachers if teacher.teacher_id != teacher_id]
        else:
            print("Unauthorized action")


# Example usage:
def main():
    bcm_system = BasicClassManagementSystem()

    # Adding an admin user
    bcm_system.add_user('khalid', 'password', 'admin')

    # Login as admin
    username = input("Enter username: ")
    password = input("Enter password: ")

    if bcm_system.login(username, password):
        print("Login successful")

        def teacher_operations():
            while True:
                print("\nTeacher Operations")
                print("1. Add Teacher")
                print("2. View Teachers")
                print("3. Delete Teacher")
                print("4. Back to Main Menu")
                choice = int(input("Select operation: "))

                if choice == 1:
                    teacher_id = input("Enter Teacher ID: ")
                    teacher_name = input("Enter Teacher Name: ")
                    class_id = input("Enter Class ID: ")
                    bcm_system.add_teacher(teacher_id, teacher_name, class_id)
                elif choice == 2:
                    bcm_system.view_teachers()
                elif choice == 3:
                    teacher_id = input("Enter Teacher ID to delete: ")
                    bcm_system.delete_teacher(teacher_id)
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")

        def student_operations():
            while True:
                print("\nStudent Operations")
                print("1. Add Student")
                print("2. View Students")
                print("3. Delete Student")
                print("4. Back to Main Menu")
                choice = int(input("Select operation: "))

                if choice == 1:
                    student_id = input("Enter Student ID: ")
                    student_name = input("Enter Student Name: ")
                    class_id = input("Enter Class ID: ")
                    bcm_system.add_student(student_id, student_name, class_id)
                elif choice == 2:
                    bcm_system.view_students()
                elif choice == 3:
                    student_id = input("Enter Student ID to delete: ")
                    bcm_system.delete_student(student_id)
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")

        def class_operations():
            while True:
                print("\nClass Operations")
                print("1. Add Class")
                print("2. View Classes")
                print("3. Delete Class")
                print("4. Back to Main Menu")
                choice = int(input("Select operation: "))

                if choice == 1:
                    class_id = input("Enter Class ID: ")
                    class_name = input("Enter Class Name: ")
                    bcm_system.add_class(class_id, class_name)
                elif choice == 2:
                    bcm_system.view_classes()
                elif choice == 3:
                    class_id = input("Enter Class ID to delete: ")
                    bcm_system.delete_class(class_id)
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")

        while True:
            print("\nMain Menu")
            print("1. Teacher Operations")
            print("2. Student Operations")
            print("3. Class Operations")
            print("4. Exit")
            choice = int(input("Select operation: "))

            operations = {
                1: teacher_operations,
                2: student_operations,
                3: class_operations,
                4: lambda: exit()
            }

            operation = operations.get(choice)
            if operation:
                operation()
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Login failed")


if __name__ == "__main__":
    main()
