class Student:
    
    def __init__(self,fullname):    #Create constructor 
        self.name=fullname
        print("Adding new student ")
        
s1= Student("Karan")
print(s1.name)

s2 = Student("Ritesh")
print(s2.name) 