import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def solve(T):
    list_teams = []
    games = []
    for i in range(T):
        list_teams.append(str(input()))

    for j in range(T*(T-1)/2):
        games.append(str(input()))        

    for item in games:
        print(item)


T = int(input())
for i in range(T):
    print(solve(T))