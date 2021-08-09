# CJ Aurum -- Aurum Creative
# August 6, 2021
# Unit Converter -- Distance Class

def convert_miles(number):
    print(number, 'miles is equal to:')
    print('\t', number, 'miles')
    print('\t', number * 1760, 'yards')
    print('\t', number * 5280, 'feet')
    print('\t', number * 63360, 'inches')
    print('\t', number * 1.61, 'kilometers')
    print('\t', number * 1609.34, 'meters')
    print('\t', number * 160934, 'centimeters')
    print('\t', number * .868976, 'nautical miles')


def convert_yards(number):
    print(number, 'yards is equal to:')
    print('\t', number * .000568182, 'miles')
    print('\t', number, 'yards')
    print('\t', number * 3, 'feet')
    print('\t', number * 36, 'inches')
    print('\t', number * .0009144, 'kilometers')
    print('\t', number * .9144, 'meters')
    print('\t', number * 91.44, 'centimeters')
    print('\t', number * .000493737, 'nautical miles')


def convert_feet(number):
    print(number, 'feet is equal to:')
    print('\t', number * .000189394, 'miles')
    print('\t', number * .3333, 'yards')
    print('\t', number, 'feet')
    print('\t', number * 12, 'inches')
    print('\t', number * .0003048, 'kilometers')
    print('\t', number * .3048, 'meters')
    print('\t', number * 30.48, 'centimeters')
    print('\t', number * .000164579, 'nautical miles')


def convert_inches(number):
    print(number, 'inches is equal to:')
    print('\t', number * .000015783, 'miles')
    print('\t', number * .027778, 'yards')
    print('\t', number * .083333, 'feet')
    print('\t', number, 'inches')
    print('\t', number * .0000254, 'kilometers')
    print('\t', number * .0254, 'meters')
    print('\t', number * 2.54, 'centimeters')
    print('\t', number * .000013715, 'nautical miles')


def convert_km(number):
    print(number, 'kilometers is equal to:')
    print('\t', number * .621, 'miles')
    print('\t', number * 1093.61, 'yards')
    print('\t', number * 3280.84, 'feet')
    print('\t', number * 39370.1, 'inches')
    print('\t', number, 'kilometers')
    print('\t', number * 1000, 'meters')
    print('\t', number * 100000, 'centimeters')
    print('\t', number * .539957, 'nautical miles')


def convert_meters(number):
    print(number, 'meters is equal to:')
    print('\t', number * .000621371, 'miles')
    print('\t', number * 1.09361, 'yards')
    print('\t', number * 3.28084, 'feet')
    print('\t', number * 39.3701, 'inches')
    print('\t', number * .001, 'kilometers')
    print('\t', number, 'meters')
    print('\t', number * 100, 'centimeters')
    print('\t', number * .000539957, 'nautical miles')


def convert_cm(number):
    print(number, 'centimeters is equal to:')
    print('\t', number * .0000062137, 'miles')
    print('\t', number * .0109361, 'yards')
    print('\t', number * .032808, 'feet')
    print('\t', number * .3937, 'inches')
    print('\t', number * .00001, 'kilometers')
    print('\t', number * .01, 'meters')
    print('\t', number, 'centimeters')
    print('\t', number * .0000053996, 'nautical miles')


def convert_naut_miles(number):
    print(number, 'nautical miles is equal to:')
    print('\t', number * 1.15078, 'miles')
    print('\t', number * 2025.37, 'yards')
    print('\t', number * 6076.12, 'feet')
    print('\t', number * 72913.4, 'inches')
    print('\t', number * 1.852, 'kilometers')
    print('\t', number * 1852, 'meters')
    print('\t', number * 185200, 'centimeters')
    print('\t', number, 'nautical miles')


class Distance:
    def distance(self):
        print('What distance type would you like to convert? ')
        print('1) Miles\t5) Kilometers\n2) Yards\t6) Meters\n3) Feet\t\t' +
              '7) Centimeters\n4) Inches\t8) Nautical Miles\n')
        what_distance = int(input('Selection: '))

        if what_distance == 1:
            number = int(input('How many miles to you wish to convert? '))
            convert_miles(number)
        elif what_distance == 2:
            number = int(input('How many yards to you wish to convert? '))
            convert_yards(number)
        elif what_distance == 3:
            number = int(input('How many feet to you wish to convert? '))
            convert_feet(number)
        elif what_distance == 4:
            number = int(input('How many inches to you wish to convert? '))
            convert_inches(number)
        elif what_distance == 5:
            number = int(input('How many kilometers to you wish to convert? '))
            convert_km(number)
        elif what_distance == 6:
            number = int(input('How many meters to you wish to convert? '))
            convert_meters(number)
        elif what_distance == 7:
            number = int(input('How many centimeters to you wish to convert? '))
            convert_cm(number)
        elif what_distance == 8:
            number = int(input('How many nautical miles to you wish to convert? '))
            convert_naut_miles(number)
        else:
            print('Invalid')

