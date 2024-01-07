
m = []
for i in range(5):
    a = int(input())
    m.append(a)

print(sum(m)//len(m))

data = sorted(m)

if len(data) % 2 == 1:
    print(data[len(data)//2])

else:
    print(data[len(data) // 2-1] + data[len(data)//2] // 2)
