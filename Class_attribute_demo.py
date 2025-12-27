class Student:
    Collage_name = "Met's IOM Nashik"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def welcome(self):
        print("welcome student",self.name)
        
    def get_marks(self):
        return self.marks
s1 = Student("Ritesh",91)
s1.welcome()
print("Marks is =",s1.get_marks())
    