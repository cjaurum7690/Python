# CJ Aurum -- Aurum Creative
# August 6, 2021
# Unit Converter -- Temperature Class

def convert_celsius(number):
    print(number, 'degrees Celsius is equal to:')
    print('\t', number, 'degrees Celsius')
    print('\t', round((number * 9/5) + 32, 2), 'degrees Fahrenheit')
    print('\t', round(number + 273.15, 2), 'degrees Kelvin')

def convert_fahrenheit(number):
    print(number, ' degrees Fahrenheit is equal to:')
    print('\t', round((number - 32) * (5/9), 2), 'degrees Celsius')
    print('\t', number, 'degrees Fahrenheit')
    print('\t', round((number - 32) * (5/9) + 273.15, 2), 'degrees Kelvin')

def convert_kelvin(number):
    print(number, 'degrees Kelvin is equal to:')
    print('\t', round(number - 273.15, 2), 'degrees Celsius')
    print('\t', round((number - 273.15) * (9/5) + 32, 2), 'degrees Fahrenheit')
    print('\t', number, 'degrees Kelvin')

class Temp():
    def temperature(self):
        print('What temperature type would you like to convert? ')
        print('1) Celsius\n2) Fahrenheit\n3) Kelvin')

        what_temp = int(input('Selection: '))

        if what_temp == 1:
            number = float(input('How many degrees Celsius to you wish to convert? '))
            convert_celsius(number)
        elif what_temp == 2:
            number = float(input('How many degrees Fahrenheit to you wish to convert? '))
            convert_fahrenheit(number)
        elif what_temp == 3:
            number = float(input('How many degrees Kelvin to you wish to convert? '))
            convert_kelvin(number)
        else:
            print('Invalid')
