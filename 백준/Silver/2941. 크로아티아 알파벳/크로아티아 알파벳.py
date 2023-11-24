crot = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in crot:
    a = a.replace(i, '*')

print(len(a))
