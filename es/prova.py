# from os import utime
import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
        
def solve(T):
    list_teams = []
    games = []
    list =[]
    best = {}  
    for i in range(T):
        list_teams.append(str(input()))

    for j in range(round(T*(T-1)/2)):
        list = list + str(input()).split(' ') 
        games.append(list)
        list = []
    
    for team in list_teams:
        score_now = 0
        for i in range(len(games)):
            if team in games[i][0]:
                index = games[i][0].find(team)
                if index == 0:
                    a,b = games[i][1].split(':')
                    if a > b:
                        score_now += 3
                    elif a == b:
                        score_now += 1
                else:
                    c,d = games[i][1].split(':')
                    if d > c:
                        score_now += 3
                    elif d == c:
                        score_now += 1

        best[team] = score_now
    all = []
    diocane = []
    for k,v in sorted(best.items(),key=lambda x:(-x[1],x[0])): #Trovo i maggiori in ordine
        all.append(k)

    print(all)

    for j in range(round(T/2)): #Prendo i primi T/2 elementi e li metto in una lista 
        diocane.append(all[j])

    diocane = sorted(diocane) # Sorto la lista
    
    for item in diocane: #Printo
        print(item + '\t')
   
T = int(input())

solve(T)

sys.stdout.close()