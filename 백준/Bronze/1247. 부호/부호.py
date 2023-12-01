import sys
a = 0
arr = []

while a < 3:
    n = int(input())
    result = 0

    for i in range(n):
        b = int(sys.stdin.readline())
        result = result + b
    if result > 0:
        arr.append("+")
    elif result < 0:
        arr.append("-")
    elif result == 0:
        arr.append(0)
    a += 1
for i in arr:
    print(i)
