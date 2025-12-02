num=(10,22,40,30,50,55,20,15,23)
i=0
find=20
while i<=len(num):
    if num[i] == find:
        print("Number found =",i)
        break
    else:
        print("Finding...")
    i+=1
    
print("End of loop..!")