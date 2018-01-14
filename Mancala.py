
def main():
    BP1 = [4, 4, 4, 4, 4, 4, 0]
    BP2 = [4, 4, 4, 4, 4, 4, 0]
    intro()
    print_board(BP1, BP2)
    P1InPlay = sum(BP1[:6])
    P2InPlay = sum(BP2[:6])
    play(P1InPlay, P2InPlay, BP1, BP2)


def intro():
    print("*******************************")
    print("***   WELCOME TO MANCALA   ****")
    print("*******************************")

# Print board. Second player section reversed to emulate mancala board from Player 1 view. Seperate single-value lists are capture pockets.
def print_board(BP1, BP2):
    BP2.reverse()
    print('\nPocket # :  6  5  4  3  2  1')
    print('P2 -->', BP2[:1], BP2[1:7])
    print('P1 --> ', '  ', BP1[0:6], BP1[6:])
    print('Pocket # :  1  2  3  4  5  6')
    BP2.reverse()

def play(P1InPlay, P2InPlay, BP1, BP2):
    while (P1InPlay != 0) and (P2InPlay != 0):
        P1Move = int(input('\nPlayer 1, which pocket do you want to move? '))
        Stones = BP1[P1Move - 1]
        if BP1[P1Move - 1] == 0:
            print('There are no stones in that pocket.\nTRY AGAIN\n')
            continue
        # Check whether seeds will flow into P2's pockets and distribute accordingly, or repeat turn if seed ends in capture.
        elif Stones + P1Move < 7:
            BP1[P1Move - 1] = 0
            for i in range(P1Move, Stones + P1Move):
                BP1[i] = BP1[i] + 1
            if (BP1[i] == 1) and (i != 6):
                BP1[i] = BP1[i] + BP2[5 - i]
                BP2[5 - i] = 0
                pass
            print_board(BP1, BP2)
        elif Stones + P1Move == 7:
            BP1[P1Move - 1] = 0
            for i in range(P1Move, Stones + P1Move):
                BP1[i] = BP1[i] + 1
            print_board(BP1, BP2)
            continue
        else:
            print('OF')
            OFlow = Stones + P1Move - 6

            for i in range(P1Move, 7):
                BP1[i] = BP1[i] + 1
            if OFlow < 7:
                BP1[P1Move - 1] = 0
                for i in range(0, OFlow - 1):
                    BP2[i] = BP2[i] + 1
                print_board(BP1, BP2)
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
        # Initiate player 2 turn. Structured the same as player 1 turn.
        while (P1InPlay != 0) and (P2InPlay != 0):
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
                    for i in range(0, OFlow - 5):
                        BP2[i] = BP2[i] + 1
                    if (BP2[i] == 1) and (i != 6):
                        BP2[i] = BP2[i] + BP1[5 - i]
                        BP1[5 - i] = 0
                        pass
                print_board(BP1, BP2)
                P1InPlay = sum(BP1[:6])
                P2InPlay = sum(BP2[:6])
            break
    print('\nGAME OVER. \nPlayer 1 Scored: ', BP1[6], '\nPlayer 2 Scored: ', BP2[6])

if __name__ == '__main__':
    main()
