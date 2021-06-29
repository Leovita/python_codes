ans = 0
ans += [[[max(l1[i] - min(), l2[i] - min(l2)) for l1, l2 in zip(*map(int,input().split()))] for i in range(int(input()))] for i in range(int(input()))]
print(ans)












