a, b = map(int, input().split())
data = []
for i in range(1, a+1):
    if a % i == 0:
        data.append(i)

data = sorted(data)
try:
    print(data[b-1])
except:
    print(0)
