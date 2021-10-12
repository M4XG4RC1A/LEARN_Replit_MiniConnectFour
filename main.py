def modMat(pos,lists,player):
    state = True
    result = 4
    if lists[pos][3] == '|':
        result = 3
    elif lists[pos][2] == '|':
        result = 2
    elif lists[pos][1] == '|':
        result = 1
    elif lists[pos][0] == '|':
        result = 0
    else:
        state = False
    print("Aqui")
    print(result)
    print(pos)
    if state == True:
        lists[pos][result] = player

    return state,lists
def printConnect(lists):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for i in lists:
        line1 = line1 + str(i[0])+" "
        line2 = line2 + str(i[1])+" "
        line3 = line3 + str(i[2])+" "
        line4 = line4 + str(i[3])+" "
    print(line1)
    print(line2)
    print(line3)
    print(line4)
def win(lists,player):
    status = False
    line = 0
    if lists[line][0] == player and lists[line][1] == player and lists[line][2] == player and lists[line][3] == player:
        status = True
    if lists[0][line] == player and lists[1][line] == player and lists[2][line] == player and lists[3][line] == player:
        status = True
    line = 1
    if lists[line][0] == player and lists[line][1] == player and lists[line][2] == player and lists[line][3] == player:
        status = True
    if lists[0][line] == player and lists[1][line] == player and lists[2][line] == player and lists[3][line] == player:
        status = True
    line = 2
    if lists[line][0] == player and lists[line][1] == player and lists[line][2] == player and lists[line][3] == player:
        status = True
    if lists[0][line] == player and lists[1][line] == player and lists[2][line] == player and lists[3][line] == player:
        status = True
    line = 3
    if lists[line][0] == player and lists[line][1] == player and lists[line][2] == player and lists[line][3] == player:
        status = True
    if lists[0][line] == player and lists[1][line] == player and lists[2][line] == player and lists[3][line] == player:
        status = True
    if lists[0][0] == player and lists[1][1] == player and lists[2][2] == player and lists[3][3] == player:
        status = True
    if lists[3][0] == player and lists[2][1] == player and lists[1][2] == player and lists[0][3] == player:
        status = True
    if status:
        print("Congratulations, Player "+player+", You win!!")
    return status
def actualPlayer(num):
    game = 'B'
    if num == 1:
        game = 'R'
    return game
def available(listA):
    stat = False
    for l in listA:
        for i in l:
            stat = stat or i=='|'
    print("Loose, no more spaces available")
    return not(stat)

print("Welcome to MiniConnectFour")

print("")
print("Rules:")
print("1) Player 1 is R")
print("2) Player 2 is B")
print("3) Player 1 is |")
print("4) The matrix is a 4x4")
print("4) If you connect 4 you win")

list1 = ['|','|','|','|']
listFinal = [['|','|','|','|'],['|','|','|','|'],['|','|','|','|'],['|','|','|','|']]
printConnect(listFinal)

winner = False

player = -1

while not(winner):
    player = player*-1
    gamer = actualPlayer(player)
    print("Player '"+gamer+"' select place to put your coin")
    sel = int(input("Select Place (1,2,3,4): "))
    while sel!=1 and sel!=2 and sel!=3 and sel!=4:
        sel = int(input("Select Place (1,2,3,4): "))
    sel = sel-1
    stat,listFinal = modMat(sel,listFinal,gamer)
    while not(stat):
        print("No available position")
        stat,listFinal = modMat(sel,listFinal,gamer)
    printConnect(listFinal)
    winner = win(listFinal,gamer)
    if not(winner):
        winner = available(listFinal)