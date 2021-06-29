weight = [2,3,5,7,1,4,1]
profit = [10,5,15,7,6,18,3]
lista = [1,3,4,5,1,87,999,4,5,999]
m=15
worth = [0] * len(weight)
index = 0
final = [0] * len(weight)
def calcoloMax(list):
    mx = -1
    for i in range(len(list)):
        mx = max(list[i], mx)
    return list.index(mx)

for i in range(len(weight)):
    worth[i] = profit[i]/weight[i]

index = calcoloMax(worth)

while m - weight[index] >= 0:
    if m - weight[index] >= 0:
        m -= weight[index]
        final[index] = 1
        worth.pop(index)
        index = calcoloMax(worth)

print(final)