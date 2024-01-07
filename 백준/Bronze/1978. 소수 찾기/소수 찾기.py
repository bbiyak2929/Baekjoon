x = int(input())
sum = 0
m = list(map(int, input().split()))
for i in m:
    sosu = True
    if i < 2:
        sosu = False
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                sosu = False
                break
        sum += sosu
print(sum)
