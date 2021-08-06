# CJ Aurum -- Aurum Creative
# August 6, 2021
# Unit Converter -- Weight Class

def convert_pounds(number):
    print(number, 'pounds is equal to:')
    print('\t', round(number, 2), 'pounds')
    print('\t', round(number * 16, 2), 'ounces')
    print('\t', round(number * .0005, 4), 'US tons')
    print('\t', round(number * .453592, 2), 'kilograms')
    print('\t', round(number * 453.592, 2), 'grams')
    print('\t', round(number * .0714286, 2), 'stones')


def convert_ounces(number):
    print(number, 'ounces is equal to:')
    print('\t', round(number * .0625, 2), 'pounds')
    print('\t', round(number, 2), 'ounces')
    print('\t', round(number * .00003125, 4), 'US tons')
    print('\t', round(number * .0283495, 2), 'kilograms')
    print('\t', round(number * 28.3495, 2), 'grams')
    print('\t', round(number * .00446429, 2), 'stones')


def convert_tons(number):
    print(number, 'tons is equal to:')
    print('\t', round(number * 2000, 2), 'pounds')
    print('\t', round(number * 32000, 2), 'ounces')
    print('\t', round(number, 2), 'US tons')
    print('\t', round(number * 907.185, 2), 'kilograms')
    print('\t', round(number * 907185, 2), 'grams')
    print('\t', round(number * 142.857, 2), 'stones')


def convert_kilograms(number):
    print(number, 'kilograms is equal to:')
    print('\t', round(number * 2.20462, 2), 'pounds')
    print('\t', round(number * 35.274, 2), 'ounces')
    print('\t', round(number * .00110231, 4), 'US tons')
    print('\t', round(number, 2), 'kilograms')
    print('\t', round(number * 1000, 2), 'grams')
    print('\t', round(number * .157473, 2), 'stones')


def convert_grams(number):
    print(number, 'grams is equal to:')
    print('\t', round(number * .00220462, 2), 'pounds')
    print('\t', round(number * .035274, 2), 'ounces')
    print('\t', round(number * .0000011023, 4), 'US tons')
    print('\t', round(number * .001, 2), 'kilograms')
    print('\t', round(number, 2), 'grams')
    print('\t', round(number * .000157473, 2), 'stones')


def convert_stones(number):
    print(number, 'stones is equal to:')
    print('\t', round(number * 14, 2), 'pounds')
    print('\t', round(number * 224, 2), 'ounces')
    print('\t', round(number * .007, 4), 'US tons')
    print('\t', round(number * 6.35029, 2), 'kilograms')
    print('\t', round(number * 6350.29, 2), 'grams')
    print('\t', round(number, 2), 'stones')


class Weight:
    def weight(self):
        print('What distance type would you like to convert? ')
        print('1) Pounds\t4) Kilograms\n2) Ounces\t5) Grams\n' +
              '3) US Tons\t6) Stones')
        what_weight = int(input('Selection: '))

        if what_weight == 1:
            number = float(input('How many pounds to you wish to convert? '))
            convert_pounds(number)
        elif what_weight == 2:
            number = float(input('How many ounces to you wish to convert? '))
            convert_ounces(number)
        elif what_weight == 3:
            number = float(input('How many kilograms to you wish to convert? '))
            convert_tons(number)
        elif what_weight == 4:
            number = float(input('How many grams to you wish to convert? '))
            convert_kilograms(number)
        elif what_weight == 5:
            number = float(input('How many stones to you wish to convert? '))
            convert_grams(number)
        elif what_weight == 6:
            number = float(input('How many stones to you wish to convert? '))
            convert_stones(number)
        else:
            print('Invalid')

