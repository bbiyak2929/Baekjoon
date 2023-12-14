import sys
a = int(input())
data = []

for i in range(a):
    b = int(sys.stdin.readline())
    if b != 0:
        data.append(b)
    else:
        data.pop()

print(sum(data))
