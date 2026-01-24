n = 4
num = 1
i = 1
while i <= n:
    row = []
    j = 1
    while j <= n:
        row.append(num)
        num += 1
        j += 1

    if i % 2 == 0:
        row.reverse()

    for x in row:
        print(x, end=" ")
    print()
    i += 1
