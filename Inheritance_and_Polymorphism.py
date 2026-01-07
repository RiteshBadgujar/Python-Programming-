
class Animal:
    def sound(self):
        print("Animal makes sound.")
        
class Dog(Animal):
    def sound(self):          # overridden method
        print("Dog barks.")


class Cat(Animal):
    def sound(self):          # overridden method
        print("Cat meows.")

# Polymorphism 
animals = [Dog(), Cat()]

for a in animals:
    a.sound()
