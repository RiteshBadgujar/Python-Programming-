# WAP to find facorial of n.(n is parameter)
n=int(input("Enter the no:"))

def facts(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print("Factorial no is =",fact)
facts(n)