print("exception handling")

try:
    no=int(input("Enter the no:"))
    print(18/no)
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
finally:
    print("Done")
