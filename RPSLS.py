# CJ Aurum -- Aurum Creative
# August 3, 2021
# Rock, Paper, Scissors, Lizard, Spock

from random import randint

wins = 0
losses = 0
ties = 0


def again():
    print('Game Totals:\n\tWins: ' + str(wins) + '\n\tLosses: ' + str(losses) + '\n\tTies: ' + str(ties))
    again = input('\nWould you like to play again? ')

    if again.lower() == 'y':
        main()
    else:
        print("Good-bye")
        exit()


# Create Spin Function
def play(player_choice, npc_choice):
    global npc_choice_value, user_choice_value
    global wins, losses, ties

    user_choice_value = ''
    npc_choice_value = ''

    if player_choice == 1:
        user_choice_value = 'Rock'
    elif player_choice == 2:
        user_choice_value = 'Paper'
    elif player_choice == 3:
        user_choice_value = 'Scissors'
    elif player_choice == 4:
        user_choice_value = 'Lizard'
    elif player_choice == 5:
        user_choice_value = 'Spock'

    # User selects Rock
    if npc_choice == 1:
        npc_choice_value = 'Rock'
    elif npc_choice== 2:
        npc_choice_value = 'Paper'
    elif npc_choice == 3:
        npc_choice_value = 'Scissors'
    elif npc_choice == 4:
        npc_choice_value = 'Lizard'
    elif npc_choice == 5:
        npc_choice_value = 'Spock'

    print('You selected ' + user_choice_value)
    print('The computer selected ' + npc_choice_value)

    # Determine if we won or lost
    if player_choice == 1:  # Rock
        if npc_choice == 1:
            print("It's A Tie!")
            ties += 1
        elif npc_choice == 2:  # Paper
            print("Paper Covers Rock! You Lose...")
            losses += 1
        elif npc_choice == 3:  # Scissors
            print("Rock Crushes Scissors!  You Win!!!")
            wins += 1
        elif npc_choice == 4:  # Lizard
            print("Rock Squashes Lizard!  You Win!!!")
            wins += 1
        elif npc_choice == 5:  # Spock
            print("Spock Vaporizes Rock!  You Lose...")
            losses += 1

    # If USer Picks Paper
    if player_choice == 2: # Paper
        if npc_choice == 2:
            print("It's A Tie!")
            ties += 1
        elif npc_choice == 1: # Rock
            print("Paper Cover Rock! You Win!!!")
            wins += 1
        elif npc_choice == 3: # Scissors
            print("Scissors Cuts Paper! You Lose...")
            losses += 1
        elif npc_choice == 4:  # Lizard
            print("Lizard Eats Paper!  You Lose...")
            losses += 1
        elif npc_choice == 5:  # Spock
            print("Paper Disproves Spock.  You WIN!!!")
            wins += 1

    # If User Pics Scissors
    if player_choice == 3: # Scissors
        if npc_choice == 3:
            print("It's A Tie!")
            ties += 1
        elif npc_choice == 1: # Rock
            print("Rock Smashes Scissors! You Lose...")
            losses += 1
        elif npc_choice == 2: # Paper
            print("Scissors Cuts Paper! You Win!!!")
            wins += 1
        elif npc_choice == 4:  # Lizard
            print("Scissors Decapitate Lizard!  You Win!!!")
            wins += 1
        elif npc_choice == 5:  # Spock
            print("Spock Smashes Scissors!  You Lose...")
            losses += 1

    if player_choice == 4: # Lizard
        if npc_choice == 4:
            print("It's A Tie!")
            ties += 1
        elif npc_choice == 1: # Rock
            print("Rock Crushes Lizard! You Lose...")
            losses += 1
        elif npc_choice == 2: # Paper
            print("Lizard Eats Paper! You Win!!!")
            wins += 1
        elif npc_choice == 3:  # Scissors
            print("Scissors Decapitate Lizard!  You Lose...")
        elif npc_choice == 5:  # Spock
            losses += 1
            print("Lizard Poisons Spock!  You Win!!!")
            wins += 1

    if player_choice == 5: # Spock
        if npc_choice == 5:
            print("It's A Tie!")
            ties += 1
        elif npc_choice == 1: # Rock
            print("Spock Vaporizes Rock! You Win!!!")
            wins += 1
        elif npc_choice == 2: # Paper
            print("Paper Disproves Spock!  You Lose...")
            losses += 1
        elif npc_choice == 3:  # Scissors
            print("Rock Smashes Scissors!  You Win!!!")
            wins += 1
        elif npc_choice == 4:  # Lizard
            print("Lizard Poisons Spock!  You Lose...")
            losses += 1

    again()

def main():
    try:
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        print('Player Options:  \n\t1) Rock\n\t2) Paper\n\t3) Scissors')
        print('\t4) Lizard\n\t5) Spock\n------------------\n\t9) Exit\n')
        player_choice = int(input('Make your selection: '))

        if player_choice == 9:
            exit()
        elif player_choice > 5 and player_choice < 9:
            print("Invalid entry")
            main()
        elif player_choice > 9:
            print("Invalid entry")
            main()

        # Pick random number for NPC
        npc_choice = randint(1, 5)

        play(player_choice, npc_choice)
    except ValueError:
        print('Invalid entry')
        main()

# Executes the main function
if __name__ == '__main__':

    main()


