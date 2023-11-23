a = input()

list = list(a)
nlist = ''.join(list)
list.reverse()
rlist = ''.join(list)


if rlist == nlist:
    print('1')
else:
    print('0')
