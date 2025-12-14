while True:
    print("\n1.Add  2.Sub  3.Mul  4.Div  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 5:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if ch == 1:
        print("Addition =", a + b)
    elif ch == 2:
        print("Subtraction =", a - b)
    elif ch == 3:
        print("Multiplication =", a * b)
    elif ch == 4:
        print("Division =", a / b)
    else:
        print("Invalid choice")
