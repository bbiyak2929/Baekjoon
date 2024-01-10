while 1:
    a = int(input())
    if a == -1:
        break
    data = []
    for i in range(1, a):
        if a % i == 0:
            data.append(i)
    if sum(data) == a:
        print('{} = '.format(a), end='')
        print(*data, sep=' + ')
    else:
        print('{} is NOT perfect.'.format(a))
