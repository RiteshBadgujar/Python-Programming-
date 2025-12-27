class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding new student")
        
s1 = Student("Karan",56)
print(s1.name, s1.marks)

s2 = Student("\n Ritesh",96)
print(s2.name, s2.marks)

s3 = Student("\n Tejas",92)
print(s3.name, s3.marks)