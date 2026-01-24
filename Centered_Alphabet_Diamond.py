n = 3
i = 1
while i <= n:
    print(" "*(n-i), end="")
    j = 1
    while j <= i:
        print(chr(64+i), end=" ")
        j += 1
    print()
    i += 1

i = n-1
while i >= 1:
    print(" "*(n-i), end="")
    j = 1
    while j <= i:
        print(chr(64+i), end=" ")
        j += 1
    print()
    i -= 1
