import sys
n = int(input())

arr = []
for i in range(n):
    a = str(sys.stdin.readline().strip())
    arr.append(a)

set_ls = set(arr)
ls = list(set_ls)
ls.sort()
ls.sort(key = len)

for i in ls:
    print(i)
