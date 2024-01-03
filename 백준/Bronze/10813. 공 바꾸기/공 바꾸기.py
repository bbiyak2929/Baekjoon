N, M = map(int, input().split())
list1 = [i for i in range(1, N+1)]
for i in range(M):
    a, b = map(int, input().split())
    list1[a-1], list1[b-1] = list1[b-1], list1[a-1]
for i in range(N):
    print(list1[i], end=' ')