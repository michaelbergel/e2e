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

    # variable rolls will be added everytime there is a turn
    rolls = 0



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



        # while none of the players have won (i.e. 1), keep on playing
        while player_A == 0 and player_B == 0:


            # roll the dice and store it in the variable dice
            dice = random.randint(1, 6)

            # variable chance has a 50% chance of being 1 or 0
            # this will be used to determine whether to get on the ladder or not
            chance = random.randint(0, 1)

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

                # variable ladder_position_A will get the original position if it's not a ladder
                # or it will get the position it'd go to IF it were to take the ladder
                ladder_position_A = LADDERS.get(position_A, position_A)

                # to determine whether to take the ladder, we'll use the variable chance
                # a value of 0 means it doesn't take the ladder; a value of 1 means it should take it

                # ----- P.S. the calculation below could be simplified through an IF statement
                # ----- but would take more time than performing the calculations directly

                # variable C below will only be used for calculation purposes. It shall take the extra
                # squares it would move up if it takes the ladder or 0 if it's not in a ladder position at all
                C = ladder_position_A - position_A

                # logic for code below: C will have either the delta for the jump or will be 0.
                # if chance is 0, the player stays where it is, verifiable through position_A.
                # if chance is 1, the player will take the ladder, moving the delta + poisiton_A
                position_A = chance * (C) + position_A


                turn +=1

                # rolls must be added by 1 every time the turn changes
                rolls += 1

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
                # keep the original position.
                position_B = SNAKES.get(position_B, position_B)

                # variable ladder_position_B will get the original position if it's not a ladder
                # or it will get the position it'd go to IF it were to take the ladder
                ladder_position_B = LADDERS.get(position_B, position_B)

                # to determine whether to take the ladder, we'll use the variable chance
                # a value of 0 means it doesn't take the ladder; a value of 1 means it should take it

                # ----- P.S. the calculation below could be simplified through an IF statement
                # ----- but would take more time than performing the calculations directly

                # variable C below will only be used for calculation purposes. It shall take the extra
                # squares it would move up if it takes the ladder or 0 if it's not in a ladder position at all
                C = ladder_position_B - position_B

                # logic for code below: C will have either the delta for the jump or will be 0.
                # if chance is 0, the player stays where it is, verifiable through position_B.
                # if chance is 1, the player will take the ladder, moving the delta + poisiton_B
                position_B = chance * (C) + position_B


                turn +=1

                # rolls must be added by 1 every time the turn changes
                rolls += 1


        # add 1 to last round to fix the counter of turns played
        turn += 1
        rolls += 1

        # add 1 to num_games once round is over
        num_games += 1

    return A_wins, B_wins, num_games, rolls


if __name__ == "__main__":

    # start simulations!
    A, B, games, rolls = simulation_sl()


    print("A has won {0} and B has won {1} in {2} games played and {3} rounds".format(A, B, games, rolls))

    avg = round(rolls/games, 2)
    print("The average of rolls with 50% probability of taking a ladder is {0} / {1}, or approximately {2} ".format(rolls, games, avg))
