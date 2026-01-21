n = 5
mid = n // 2
i = 0
while i < n:
    j = 0
    while j < n:
        if i == mid or j == mid or i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1
