n = 4
i = 1
while i <= n:
    print(" "*(n-i), end="")
    j = 1
    while j <= i:
        print(chr(64+i), end=" ")
        j += 1
    print()
    i += 1
