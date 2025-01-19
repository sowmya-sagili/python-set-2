class Student:
    def _init_(self,student_id,name,grade):
        self.student_id=student_id
        self.name=name
        self.grade=grade
    def display_info(self):
        print(f"\nStudent ID:{self.student_id},Name:{self.name},Grade:{self.grade}")
class Teacher:
    def _init_(self,teacher_id,name,subject):
        self.teacher_id=teacher_id
        self.name=name
        self.subject=subject
    def display_info(self):
        print(f"\nTeacher iD:{self.teacher_id},Name:{self.name},Subject:{self.subject}")
class Course:
    def _init_(self,course_code,course_name,teacher,students):
        self.course_code=course_code
        self.course_name=course_name
        self.teacher=teacher
        self.students=students
    def display_info(self):
        print(f"\nCourse Code:{self.course_code},Course Name:{self.course_name}")
        print("Teacher:")
        self.teacher.display_info()
        print("\nStudents:")
        for student in self.students:
            student.display_info()
    def main():
        students=[]
        teachers=[]
        courses=[]
        print("""1.Student_form/details\n2.Teacher_form/details\n3.Courser_form/details""")
        cho=int(input("\nEnter your choice:"))
        if cho==1:
            num_students=int(input("\nEnter the number of students:"))
            for i in range(num_students):
                student_id=input(f"\nEnter student{i+1}ID:")
                name=input(f"\nEnter student{i+1}Name:")
                grade=input(f"\nEnter student{i+1}grade:")
                students.append(Student(student_id,name,grade))
                print("\nRegistration successful.")
        elif cho==2:
            num_teachers=int(input("\nEnter the number of teachers:"))
            for i in range(num_teachers):
                teacher_id=input(f"\nEnter teacher{i+1}ID:")
                name=input(f"\nEnter teacher{i+1}Name:")
                subject=input(f"\nEnter teacher{i+1}subject:")
                teachers.append(Teacher(teacher_id,name,subject))
                print("\nRegistration successful.")
        elif cho==3:
            num_courses=int(input("\nEnter the number of courses:"))
            for i in range(num_courses):
                course_code=input(f"\nEnter course{i+1}code:")
                course_name=input(f"\nEnter course{i+1}name:")
                teacher_index=int(input("\nEnter the index of the teacher for this course:"))
                teacher=teachers[teacher_index]
                student_indices=input("\nEnter the indices of the students for this course(comma-separated):")
                student_indices=student_indices.split(",")
                students_for_course=[students[int(index)] for index in student_indices]
                courses.append(Course(course_code,course_name,teacher,students_for_course))
                print("\nRegistration successful.")
        else:
            print("\nInvalid input")
    if _name=="main_":
        main()
