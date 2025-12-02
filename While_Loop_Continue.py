num=int(input("Enter the No :"))
i=0
print("Odd No.")
while i<=num:
    if(i %2 == 0):
        i+=1
        continue
    print(i)
    i+=1
j=0
print("\n Even No.")
while j<=num:
    if(j%2 !=0):
        j+=1
        continue
    print(j)
    j+=1
    