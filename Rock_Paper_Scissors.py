import random

rock = 1
paper = 2
scissors = 3

computer_score = 0
player_score = 0

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}


def start():
    print("Let's play a game of Rock, Paper, Scissors")
    while game():
        pass


def game():
    global player_score, computer_score
    # computer's move
    computer_move = random.randint(1, 3)

    try:
        # telling the user to make a move
        player_move = int(input("Make a move:"))

        try:
            # game draw
            if int(player_move) == computer_move:
                print("Tie Game...\nComputer threw a {0}".format(names[computer_move]))
                print("")

            # if not draw
            else:
                # user win
                if rules[player_move] == computer_move:
                    print("You Win!!!\nComputer threw a {0}".format(names[computer_move]))
                    print("")
                    player_score += 1

                # com win
                else:
                    print("You Lose!!!\nComputer threw a {0}".format(names[computer_move]))
                    print("")
                    computer_score += 1

        # raise error if user input numbers other than 1, 2, 3
        except KeyError:
            print("Please enter 1, 2, or 3.")
            print("")

    # raise error if user input alphabets
    except ValueError:
        print("Enter 1, 2 or 3.")
        print("")


# main game loop
if __name__ == "__main__":
    while player_score or computer_score < 4:
        start()
        n = 3  # choose how many rounds you want

        # user win after n rounds
        if player_score == n:
            print("You Win!!!")
            break

        # com win after n rounds
        elif computer_score == n:
            print("You Lose!!!")
            break
