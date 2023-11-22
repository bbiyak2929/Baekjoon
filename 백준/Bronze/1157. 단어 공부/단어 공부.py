a = input().upper()
b = list(set(a))


list = []
for i in b:
    cnt = a.count(i)
    list.append(cnt)

if list.count(max(list)) > 1:
    print('?')
else:
    max_index = list.index(max(list))
    print(b[max_index])
