
first = int(input())
fl = 10
while first > fl:
    if first % fl >= fl//2:
        first += fl
    first -= first % fl
    fl = fl * 10


print(first)
