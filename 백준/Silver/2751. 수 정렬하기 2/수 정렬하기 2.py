import sys
n = int(sys.stdin.readline())

arr = []

for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)

arr1 = sorted(arr)

for i in arr1:
    print(i)
