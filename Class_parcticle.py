#Create student class that take name & marks of 3 subject as argument in constructor .then create a method to print to avarage .
class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avarage(self):  
        sum = 0
        for value in self.marks:
            sum+=value
        print("Hi",self.name,"Your avarage score is :",sum/3)

s1 = Student("Ritesh",[99.86,97])
s1.avarage()

s1.name="Rohan"
s1.avarage()