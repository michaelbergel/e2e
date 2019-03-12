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

    # count how many times a snake has been activated
    snakes = 0

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


        # this variable will be used to keep track of when a snake gets activated
        position_snaked = 0

        # while none of the players have won (i.e. 1), keep on playing
        while player_A == 0 and player_B == 0:

            # roll the dice and store it in the variable dice
            dice = random.randint(1, 6)

            # position_snaked must zero in every round
            position_snaked = 0


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
                position_snaked = SNAKES.get(position_A, position_A)

                # if position_A > position_snaked, it means the snake has been activated
                # the variable snakes then is added by 1 and position_A is updated accordingly
                if position_A > position_snaked:
                    snakes += 1
                    position_A = position_snaked


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
                # keep the original position.
                position_snaked = SNAKES.get(position_B, position_B)

                # if position_B > position_snaked, it means the snake has been activated
                # the variable snakes then is added by 1 and position_B is updated accordingly
                if position_B > position_snaked:
                    snakes += 1
                    position_B = position_snaked

                position_B = LADDERS.get(position_B, position_B)

                turn +=1


        # add 1 to last round to fix the counter of turns played
        turn += 1

        # add 1 to num_games once round is over
        num_games =+ 1

    return A_wins, B_wins, snakes, rounds


if __name__ == "__main__":

    # start simulations!
    A, B, snakes, rounds = simulation_sl()

    # round prob of A winning to 2 decimals
    prob_A = round(A/rounds, 2)
    print("A has won {0} and B has won {1} ".format(A, B))
    print("A has thus a probability of winning of {0} / {1}, or approximately {2} ".format(A, rounds, prob_A))

    # snakes per round on avg = total snakes activated / 10000
    avg_snakes = round(snakes/rounds, 2)
    print("A snake has been activated {0} times in {1} games, an average of {2} per game ". format(snakes, rounds, avg_snakes))