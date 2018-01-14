
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

def play(BP1, BP2):
    GameOver = False
    while GameOver != True:
        playermancala = playround(BP1, BP2, GameOver)
        BP1 = playermancala[0]
        BP2 = playermancala[1]
        if sum(BP1[:6]) == 0 or sum(BP2[:6]) == 0:
            GameOver = True
            BP1[6] += sum(BP1[:6])
            BP2[6] += sum(BP2[:6])
    print('\nGAME OVER. \nPlayer 1 Scored: ', BP1[6], '\nPlayer 2 Scored: ', BP2[6])

def playround(BP1, BP2, GameOver):
    P1InPlay = sum(BP1[:6])
    P2InPlay = sum(BP2[:6])
    P1Move = int(input('\nPlayer 1, which pocket do you want to move? '))
    Stones = BP1[P1Move - 1]
    if BP1[P1Move - 1] == 0:
        print('There are no stones in that pocket.\nTRY AGAIN\n')
        return [BP1, BP2, GameOver]
    # Check whether seeds will flow into P2's pockets and distribute accordingly, or repeat turn if seed ends in capture.
    elif Stones + P1Move < 7:
        BP1[P1Move - 1] = 0
        for i in range(P1Move, Stones + P1Move):
            BP1[i] = BP1[i] + 1
        if (BP1[i] == 1) and (i != 6):
            BP1[i] = BP1[i] + BP2[5 - i]
            BP2[5 - i] = 0
            pass
        #print_board(BP1, BP2)
    elif Stones + P1Move == 7:
        BP1[P1Move - 1] = 0
        for i in range(P1Move, Stones + P1Move):
            BP1[i] = BP1[i] + 1
        print_board(BP1, BP2)
        return [BP1, BP2, GameOver]
    elif Stones + P1Move > 7:
        print('OF')
        OFlow = Stones + P1Move - 6

        for i in range(P1Move, 7):
            BP1[i] = BP1[i] + 1
        if OFlow < 7:
            BP1[P1Move - 1] = 0
            for i in range(0, OFlow - 1):
                BP2[i] = BP2[i] + 1
            #print_board(BP1, BP2)
        # This handles overflow back into P1s pockets for large amount of seeds.
        else:
            BP1[P1Move - 1] = 0
            for i in range(0, 6):
                BP2[i] = BP2[i] + 1
            for i in range(0, OFlow - 7):
                BP1[i] = BP1[i] + 1
        if (BP1[i] == 1) and (i != 6):
            BP1[i] = BP1[i] + BP2[5 - i]
            BP2[5 - i] = 0
            pass
    print_board(BP1, BP2)
    P1InPlay = sum(BP1[:6])
    P2InPlay = sum(BP2[:6])
    P2Turn = True
    # Initiate player 2 turn. Structured the same as player 1 turn.
    while P2Turn != False:
        if sum(BP2[:6]) == 0:
            return [BP1, BP2, GameOver]

        P2Move = int(input('\nPlayer 2, which pocket do you want to move?'))
        Stones = BP2[P2Move - 1]
        if BP2[P2Move - 1] == 0:
            print('There are no stones in that pocket.\nTRY AGAIN\n')
            continue
        elif Stones + P2Move < 7:
            BP2[P2Move - 1] = 0
            for i in range(P2Move, Stones + P2Move):
                BP2[i] = BP2[i] + 1
            if (BP2[i] == 1) and (i != 6):
                BP2[i] = BP2[i] + BP1[5 - i]
                BP1[5 - i] = 0
                pass
            print_board(BP1, BP2)
        elif Stones + P2Move == 7:
            BP2[P2Move - 1] = 0
            for i in range(P2Move, Stones + P2Move):
                BP2[i] = BP2[i] + 1
            print_board(BP1, BP2)
            continue
        else:
            print('OF')
            OFlow = Stones + P2Move - 6
            for i in range(P2Move, 7):
                BP2[i] = BP2[i] + 1
            if OFlow < 7:
                BP2[P2Move - 1] = 0
                for i in range(0, OFlow - 1):
                    BP1[i] = BP1[i] + 1

            else:
                BP2[P2Move - 1] = 0
                for i in range(0, 6):
                    BP1[i] = BP1[i] + 1
                for i in range(0, OFlow - 7):
                    BP2[i] = BP2[i] + 1
            if (BP2[i] == 1) and (i != 6):
                BP2[i] = BP2[i] + BP1[5 - i]
                BP1[5 - i] = 0
                pass
            print_board(BP1, BP2)
            P1InPlay = sum(BP1[:6])
            P2InPlay = sum(BP2[:6])
        P2Turn = False
    return [BP1, BP2, GameOver]
if __name__ == '__main__':
    main()
