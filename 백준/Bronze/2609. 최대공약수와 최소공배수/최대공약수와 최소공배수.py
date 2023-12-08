a, b = map(int, input().split())

if a > b:
    big = a
    small = b
else:
    big = b
    small = a

while (1):
    m = big / small
    g = big % small

    if g == 0:
        break

    big = small
    small = g

gcm = small

lcm = (a*b) / gcm
print(gcm)
print(int(lcm))
