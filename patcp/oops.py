class Student:
    def __init__(self,a,b,c):
        self.name=a
        self.sem=b
        self.marks=c
    def __str__(self) -> str:
        return f"(self.name:{self.a},self.sem-:{self.b},self.marks:{self.c})"
obj1=Student("ramesh",6,85)
obj2=Student("rahul",5,95)
obj3=Student("bottu",4,80)
print(obj1)
print(obj2)
print(obj3)

#OR...................................................................................................


class Student:
    def __init__(self,a,b,c):
        self.name=a
        self.sem=b
        self.marks=c
    def ok(self) -> str:
        print(f"name:{self.name},sem-:{self.sem},marks:{self.marks}")
obj1=Student("ramesh",6,85)
obj2=Student("rahul",5,95)
obj3=Student("bottu",4,80)
Student.ok(obj1)
Student.ok(obj2)
Student.ok(obj3)