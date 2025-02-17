n = int(input("Enter the input number: "))
m = 2 * n + 3
width = 2
for i in range(m):
    for j in range(m):
        if j == 0 or j == m - 1:
            print("O".rjust(width), end="")
        elif i == 0 or i == m - 1:
            print("0".rjust(width), end="")
        elif i == n + 1 and j == n + 1:
            print("O".rjust(width), end="")
        elif i < n + 1 and j < n + 1 and i < j + 1:
            print(str(n - j + 1).rjust(width), end="")
        elif i < n + 1 and j > n + 1 and i + j > m - 2:
            print(str(m - 1 - j).rjust(width), end="")
        elif i > n + 1 and j < n + 1 and i + j < m:
            print(str(j).rjust(width), end="")
        elif i > n + 1 and j > n + 1 and i + 1 > j:
            print(str(j - n - 1).rjust(width), end="")
        else:
            print(" ".rjust(width), end="")
    print()  