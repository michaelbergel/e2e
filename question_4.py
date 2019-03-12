import random

# store rules in dictionaries. 3:16 means if the player is at 3, it should jump to 16
SNAKES = {12:2, 14:11, 17:4, 31:19, 35:22}
LADDERS = {3:16, 5:7, 15:25, 18:20, 21:32}

def simulation_sl():

    # variable to keep track of # of games
    num_games = 0

    # 3 arrays to record games' results, B's starting position and respective probabilities
    games = []
    A_outcome = []
    B_outcome = []
    B_start_pos = []
    probability_of_A = []


    # variables to keep track of wins
    A_wins = 0
    B_wins = 0

    # variable that determines the number of rounds
    rounds = 10000

    # this variable will be used to add one square to B's starting point
    # after running 10K simulations until a threshold is reached
    add_one = 1


    # keep adding 1 to B's starting position until B's probability of winning
    # overcomes A's probability of winning (i.e. 10% is arbitrary)
    while 1.1*(A_wins/rounds) >= (B_wins/rounds):

    # if we got to this line of code, it means we haven't reached the threshold yet
    # and thus we must reset both A_wins and B_wins variables
        A_wins = 0
        B_wins = 0


        # while we haven't reached 10,000 games, keep on playing!
        while A_wins + B_wins < rounds:

            # variable to decide whose turn is it. If odd, player B; If even, player A.
            turn = 0

            # while none of the players have achieved 1, the game continues
            player_A = 0
            player_B = 0

            # variables to track positions of A and B
            position_A = 0
            position_B = add_one


            # while none of the players have won (i.e. 1), keep on playing
            while player_A == 0 and player_B == 0:

                # roll the dice and store it in the variable dice
                dice = random.randint(1, 6)


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
                    # keep the original position.
                    position_B = SNAKES.get(position_B, position_B)
                    position_B = LADDERS.get(position_B, position_B)

                    turn +=1


            # add 1 to last round to fix the counter of turns played
            turn += 1

            # add 1 to num_games once round is over
            num_games += 1

        # keep adding one to add_one variable
        add_one += 1

        # record the simulation number and its outcomes
        games.append(round(num_games/10000))
        A_outcome.append(A_wins)
        B_outcome.append(B_wins)
        B_start_pos.append(add_one-1)
        probability_of_A.append(round(A_wins/rounds, 2))


    return games, A_outcome, B_outcome, B_start_pos, probability_of_A


if __name__ == "__main__":

    # start simulations!
    games, A, B, B_start, prob_A = simulation_sl()

    # print results
    for i, j, k, m, p in zip(games, A, B, B_start, prob_A):
        print("Game: {0} A: {1} B: {2} B's starting at: {3} Prob. of A: {4}".format(i, j, k, m, p))
