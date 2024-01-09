a, b = map(int, input().split())
result = 0
c = 0
arr = []
for i in range(a):
    arr.append(input())


for i in range(a):
    
    if "X" not in arr[i]:
        result += 1

for j in range(b):
    if "X" not in [arr[i][j] for i in range(a)]:
            c += 1
print(max(result, c))
