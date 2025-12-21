#Write a recursive function to calculate the sum of frist n natural numbers.
n=int(input("Enter the no :"))
def cals(n):
    print(n)
    if n == 0:
        return 0
    return n + cals(n-1)

print("Addition is :",cals(n))