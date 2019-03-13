import random

# store rules in dictionaries. 3:16 means if the player is at 3, it should jump to 16
SNAKES = {12:2, 14:11, 17:4, 31:19, 35:22}
LADDERS = {3:16, 5:7, 15:25, 18:20, 21:32}

def simulation_sl():

    # variable to keep track of # of games
    num_games = 0

    # variables to keep track of wins
    A_wins = 0
    B_wins = 0

    # variable that determines the number of rounds
    rounds = 10000


    # while we haven't reached 10,000 games, keep on playing!
    while A_wins + B_wins < rounds:

        # variable to decide whose turn is it. If odd, player B; If even, player A.
        turn = 0


        # while none of the players have achieved 1, the game continues
        player_A = 0
        player_B = 0

        # variables to track positions of A and B
        position_A = 0
        position_B = 0

        # variable snake will control when a snake is activated. must be zeroed in every game
        snake = 0



        # while none of the players have won (i.e. 1), keep on playing
        while player_A == 0 and player_B == 0:


            # roll the dice and store it in the variable dice
            dice = random.randint(1, 6)


            # the variable will be used to keep track of whether this is the first
            # snake that shows up for B
            snake_position_B = 0


            # this variable will be used for calculation purposes
            # it must start every turn with the value of 0
            C = 0


            # check if it's A's turn and move it accordingly
            # if turn is even, the modulo will be 0, signaling it's A's turn
            if turn % 2 == 0:

                # if the dice takes player A beyond square 36, declare winner and add
                # to counter of wins (i.e. A_wins)
                if position_A + dice >= 36:
                    player_A += 1
                    A_wins += 1
                    break

                position_A += dice

                # take A up/down any chute/ladder. If the value is not in dictionary
                # keep the original position.
                position_A = SNAKES.get(position_A, position_A)
                position_A = LADDERS.get(position_A, position_A)


                turn +=1


            # check if it's B's turn and move it accordingly
            # if turn is odd, the modulo will be 1, signaling it's B's turn
            else:
                # if the dice takes player B beyond square 36, declare winner and add
                # to counter of wins (i.e. B_wins)
                if position_B + dice >= 36:
                    player_B += 1
                    B_wins += 1
                    break

                position_B += dice

                # take B up/down any chute/ladder. If the value is not in dictionary
                # keep the original position. Analyze if it's the first snake to skip it.

                snake_position_B = SNAKES.get(position_B, position_B)


                # logic for code below: C will have either the delta for the jump or will be 0.
                # if C is > 0 it means the player is at a snake position, so the variable snake
                # should be added 1.
                # moreover, if and only if the value of variable snake == 1 (i.e meaning it's the
                # first snake it steps on), the player should skip it and don't activate it
                C = position_B - snake_position_B
                if C > 0:
                    snake += 1
                    if snake != 1:
                        position_B = snake_position_B


                # let B take the ladder, as usual
                position_B = LADDERS.get(position_B, position_B)


                turn +=1



        # add 1 to last round to fix the counter of turns played
        turn += 1

        # add 1 to num_games once round is over
        num_games += 1

    return A_wins, B_wins, num_games


if __name__ == "__main__":

    # start simulations!
    A, B, games = simulation_sl()


    print("A has won {0} and B has won {1} in {2} games played\n".format(A, B, games))

    # prob of A winning
    prob = A/games
    print("The new probability for A, given that B gets to bypass the first snake is {0} / {1}, or approximately {2} ".format(A, games, prob))
