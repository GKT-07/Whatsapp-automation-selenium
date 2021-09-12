def apply_cycle(lst, v1, v2, v3):
    val = lst[v3]
    lst[v3] = lst[v2]
    lst[v2] = lst[v1]
    lst[v1] = val


T = int(input())
for _ in range(T):
    n, k = map(int, input().split(" "))
    lis = list(map(int, input().split(" ")))
    a = lis.copy()
    a.sort()
    c = []
    i = 1
    while i < n:
        if i == n - 1:
            break
        if lis[i - 1] != i:
            i1 = i
            i2 = lis[i1 - 1]
            if lis[i2 - 1] != i1:
                i3 = lis[i2 - 1]
                apply_cycle(lis, lis.index(i1), lis.index(i2), lis.index(i3))
                c.append([lis.index(i1) + 1, lis.index(i2) + 1, lis.index(i3) + 1])
        i += 1

    i = 1
    while i <= k:
        if i == n - 1 or lis == a:
            break
        if lis[i - 1] != i:
            i1 = i
            i2 = lis[i1 - 1]
            if lis[i2 - 1] != i1:
                i3 = lis[i2 - 1]
                apply_cycle(lis, lis.index(i1), lis.index(i2), lis.index(i3))
                c.append([lis.index(i1) + 1, lis.index(i2) + 1, lis.index(i3) + 1])
            else:
                for h in range(len(lis)):
                    if lis[h] != h + 1 and h + 1 != i1 and h + 1 != i2:
                        i3 = h + 1
                        apply_cycle(lis, lis.index(i1), lis.index(i2), lis.index(i3))
                        c.append([lis.index(i1) + 1, lis.index(i2) + 1, lis.index(i3) + 1])
                        break
        i += 1

    if a != lis:
        print(-1)
    else:
        print(len(c))
        for u in range(len(c)):
            print(c[u][0], c[u][1], c[u][2])
