

def solve():
    cont = 0
    c = int(input())
    lista = [int(x) for x in str(c)]
    yay = lista[0]
    while len(lista) >= 1:
        cont += len(lista)
        del lista[-1]

    cont += (10 * int(yay - 1))    
    return cont

    
n = int(input())

for i in range(n):
    print(solve())