def main():
    BP1 = [4, 4, 4, 4, 4, 4, 0]
    BP2 = [4, 4, 4, 4, 4, 4, 0]
    setup()
    print_board(BP1, BP2)
    play(BP1, BP2)


def setup():
    print("*******************************")
    print("***   WELCOME TO MANCALA   ****")
    print("*******************************")

# Print board. Second player section reversed to emulate mancala board from Player 1 view. Seperate single-value lists are capture pockets.
def print_board(BP1, BP2):
    BP2.reverse()
    print('\nPocket # :  6  5  4  3  2  1')
    print('P2 --> {' + str(BP2[0]) + '} ' + str(BP2[1:7]))
    print('P1 -->     ' + str(BP1[0:6]) + '  {' + str(BP1[6]) + '}')
    print('Pocket # :  1  2  3  4  5  6')
    BP2.reverse()

def play(BP1, BP2, GameOver = False):
    while GameOver != True:
        for i in range(1, 3):
            mancalaList = playround(BP1, BP2, i)
            BP1 = mancalaList[0]
            BP2 = mancalaList[1]
            if sum(BP1[:6]) == 0 or sum(BP2[:6]) == 0:
                GameOver = True
                BP1[6] += sum(BP1[:6])
                BP2[6] += sum(BP2[:6])
                play(BP1, BP2, True)
                return
    print('\nGAME OVER. \nPlayer 1 Scored: ', BP1[6], '\nPlayer 2 Scored: ', BP2[6])
    
def playround(BP1, BP2, PlayerNum):
    P1InPlay = sum(BP1[:6])
    P2InPlay = sum(BP2[:6])
    if P1InPlay == 0 or P2InPlay == 0:
        return [BP1, BP2]
    if PlayerNum == 1:
        Move = int(input('\nPlayer 1, which pocket do you want to move? '))
        Stones = BP1[Move - 1]
        BP = BP1
        OtherBP = BP2
    elif PlayerNum == 2:
        Move = int(input('\nPlayer 2, which pocket do you want to move? '))
        Stones = BP2[Move - 1]
        BP = BP2
        OtherBP = BP1
    if Stones == 0:
        print('There are no stones in that pocket.\nTRY AGAIN\n')
        playround(BP1, BP2, PlayerNum)
    elif Stones + Move < 7:
        BP[Move - 1] = 0
        for i in range(Move, Stones + Move):
            BP[i] += 1
        if (BP[i] == 1) and (i != 6):
            BP[i] += OtherBP[5 - i]
            OtherBP[5 - i] = 0
            pass
    elif Stones + Move == 7:
        BP[Move - 1] = 0
        for i in range(Move, Stones + Move):
            BP[i] += 1
        returnList = toReturn(BP, OtherBP, PlayerNum)
        if (P1InPlay == 0 or P2InPlay == 0):
            return [returnList[0], returnList[1]]
        print_board(returnList[0], returnList[1])
        return playround(returnList[0], returnList[1], PlayerNum)
    elif Stones + Move > 7:
        OFlow = Stones + Move - 6
        for i in range(Move, 7):
            BP[i] += 1
        if OFlow < 7:
            BP[Move - 1] = 0
            for i in range(0, OFlow - 1):
                OtherBP[i] += + 1
        else:
            BP[Move - 1] = 0
            for i in range(0, 6):
                OtherBP[i] += 1
            for i in range(0, OFlow - 7):
                BP[i] += 1
        if (BP[i] == 1) and (i != 6):
            BP[i] += OtherBP[5 - i]
            OtherBP[5 - i] = 0
            pass
    returnList = toReturn(BP, OtherBP, PlayerNum)
    print_board(returnList[0], returnList[1])
    return toReturn(BP, OtherBP, PlayerNum)

def toReturn(BP, OtherBP, PlayerNum):
    if PlayerNum == 1:
        BP1 = BP
        BP2 = OtherBP
    elif PlayerNum == 2:
        BP1 = OtherBP
        BP2 = BP
    return [BP1, BP2]

if __name__ == '__main__':
    main()
