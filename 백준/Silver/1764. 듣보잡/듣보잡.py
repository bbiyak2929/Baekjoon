a, b = map(int, (input().split()))


d = set()
j = set()
for i in range(a):
    d.add(input())
for _ in range(b):
    j.add(input())


sum = d.intersection(j)
sum = sorted(sum)
print(len(sum))
for i in sum:
    print(i)
