# CJ Aurum -- Aurum Creative
# August 6, 2021
# Unit Converter -- Main Screen

from ConvertDistance import Distance
from ConvertTemp import Temp
from ConvertWeight import Weight


def main():
    try:
        print('What would you like to convert? ')
        print('\t1) Distance\n\t2) Temperature\n\t3) Weight\n\t99) Exit')
        choice = int(input('Selection: '))

        if choice == 1:
            my_selection = Distance()
            my_selection.distance()
        elif choice == 2:
            my_selection = Temp()
            my_selection.temperature()
        elif choice == 3:
            my_selection = Weight()
            my_selection.weight()
        elif choice == 99:
            exit()
        else:
            print('Invalid selection.  Try again.')
            main()
    except ValueError:
        print('Invalid selection.  Try again.')
        main()


# Executes the main function
if __name__ == '__main__':
    main()

