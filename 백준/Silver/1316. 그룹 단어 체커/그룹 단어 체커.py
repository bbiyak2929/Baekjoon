a = int(input())
cnt = a
for i in range(a):
    c = input()
    for j in range(0, len(c)-1):
        if c[j] == c[j+1]:
            pass
        elif c[j] in c[j+1:]:
            cnt -= 1
            break
print(cnt)
