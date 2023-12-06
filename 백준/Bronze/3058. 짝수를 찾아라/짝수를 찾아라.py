a = int(input())

for i in range(a):
    num = []
    data = list(map(int, input().split()))
    
    for i in data:
        if i % 2 == 0:
            num.append(i)

    print(sum(num), min(num))
    


