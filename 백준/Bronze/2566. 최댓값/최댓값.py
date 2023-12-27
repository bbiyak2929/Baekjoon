
a = []

for row in range(9):
    a.append(list(map(int, input().split())))

max_value = max(map(max, a))
print(max_value)
for i in range(9):
    for j in range(9):
        if a[i][j] == max_value:
            print(i+1, j+1)
