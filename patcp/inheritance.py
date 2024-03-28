class person:
    def great(self):
        return "hello i am a person"
class Student(person):
    def great(self):
        return "hello i am a student"
class Teacher(person):
    def great(self):
        return "hello i am a teacher"
class teacher_assignment(Teacher,Student): #teacher is first so hello iam a teacher will be printed if student then student will be printed.
    pass
assignment=teacher_assignment()
print(assignment.great())