from random import randint

def dice():
    # Game Score Begins with 0 for both Computer and Human
    human = 0
    computer = 0

    # Loop to count the score till Human or Computer Wins
    while human <=100 or computer <= 100:
        # Computer turn 
        c_turn = randint(1,6)
        # Human turn 
        h_turn = input("Press Enter to Roll Dice! or Press q to Quit the game")

        # checking whether the user wants to continue the game
        if h_turn != 'q':
            h_score = randint(1,6)

        # Checking the user wants to Quit the Game
        elif h_turn == 'q':
            print(f"You Quit the game, your score was {human} and computer score was {computer}")
            break

        # Adding the scores to Human and Computer after rolling Dice
        human += h_score
        computer += c_turn

        # Checking the scores if Human gets 100 before Computer, Then Human Wins
        if human >= 100:
            print("Hurray....! You Won")
            break
        # Checking the scores if Computer gets 100 before Human, then Computer Wins
        elif computer >= 100:
            print("Sorry!, Better luck next time.") 
            break

# calling the dice function
dice()
