import sys
n = int(input())

arr = [[] for _ in range(51)]
for i in range(n):
    a = input()
    arr[len(a)].append(a)

for i in arr:
    if len(i) == 0:
        pass
    else:
        temp = sorted(list(set(i)))
        for j in temp:
            print(j)
