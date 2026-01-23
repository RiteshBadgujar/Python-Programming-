n = 5
i = 0
while i < n:
    j = 0
    while j < 2*n-1:
        if j == i or j == 2*n-2-i:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
