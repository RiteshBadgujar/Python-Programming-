rows = 3
cols = 9

for i in range(rows):
    for j in range(cols):
        if (i == 0 and j % 4 == 0) or (i == 1 and j % 2 == 1) or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
