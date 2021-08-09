def convert_miles(number):
    miles = int(number)
    yards = int(number) * 1760
    feet = int(number) * 5280
    inches = int(number) * 63360
    kilometers = round(int(number) * 1.61, 2)
    meters = round(int(number) * 1609.34, 2)
    centimeters = int(number) * 160934
    converted = (str(miles) +' miles\n' + str(yards) + ' yards\n' + str(feet) + ' feet\n' + str(inches) + ' inches\n' +
                       str(kilometers) + ' kilometers\n' + str(meters) + ' meters\n' + str(centimeters) + ' centimeters')
    return converted


def convert_yards(number):
    miles = round(int(number) * .000568182, 4)
    yards = int(number)
    feet = int(number) * 3
    inches = int(number) * 36
    kilometers = round(int(number) * .0009144, 4)
    meters = round(int(number) * .9144, 2)
    centimeters = int(number) * 91.44
    converted = (str(miles) +' miles\n' + str(yards) + ' yards\n' + str(feet) + ' feet\n' + str(inches) + ' inches\n' +
                       str(kilometers) + ' kilometers\n' + str(meters) + ' meters\n' + str(centimeters) + ' centimeters')
    return converted


def convert_feet(number):
    miles = round(int(number) * .000189394, 4)
    yards = int(number) * .3333
    feet = int(number)
    inches = int(number) * 12
    kilometers = round(int(number) * .0003048, 4)
    meters = round(int(number) * .3048, 2)
    centimeters = round(int(number) * 30.48, 2)
    converted = (str(miles) +' miles\n' + str(yards) + ' yards\n' + str(feet) + ' feet\n' + str(inches) + ' inches\n' +
                       str(kilometers) + ' kilometers\n' + str(meters) + ' meters\n' + str(centimeters) + ' centimeters')
    return converted


def convert_inches(number):
    miles = round(int(number) * .000015783, 4)
    yards = round(int(number) * .027778, 4)
    feet = round(int(number) * .083333, 4)
    inches = int(number)
    kilometers = round(int(number) * .0000254, 4)
    meters = round(int(number) * .0254, 2)
    centimeters = round(int(number) * 2.54, 2)
    converted = (str(miles) +' miles\n' + str(yards) + ' yards\n' + str(feet) + ' feet\n' + str(inches) + ' inches\n' +
                       str(kilometers) + ' kilometers\n' + str(meters) + ' meters\n' + str(centimeters) + ' centimeters')
    return converted


def convert_km(number):
    miles = round(int(number) * .621, 2)
    yards = round(int(number) * 1093.61, 2)
    feet = round(int(number) * 3280.84, 2)
    inches = round(int(number) * 39370.1, 2)
    kilometers = int(number)
    meters = int(number) * 1000
    centimeters = int(number) * 100000
    converted = (str(miles) +' miles\n' + str(yards) + ' yards\n' + str(feet) + ' feet\n' + str(inches) + ' inches\n' +
                       str(kilometers) + ' kilometers\n' + str(meters) + ' meters\n' + str(centimeters) + ' centimeters')
    return converted


def convert_meters(number):
    miles = round(int(number) * .000621371, 2)
    yards = round(int(number) * 1.09361, 2)
    feet = round(int(number) * 3.28084, 2)
    inches = round(int(number) * 39.3701, 2)
    kilometers = round(int(number) * .001, 2)
    meters = int(number)
    centimeters = int(number) * 100
    converted = (str(miles) +' miles\n' + str(yards) + ' yards\n' + str(feet) + ' feet\n' + str(inches) + ' inches\n' +
                       str(kilometers) + ' kilometers\n' + str(meters) + ' meters\n' + str(centimeters) + ' centimeters')
    return converted


def convert_cm(number):
    miles = round(int(number) * .0000062137, 4)
    yards = round(int(number) * .0109361, 4)
    feet = round(int(number) * .032808, 4)
    inches = round(int(number) * .3937, 4)
    kilometers = round(int(number) * .00001, 4)
    meters =round(int(number) * .01, 2)
    centimeters = int(number)
    converted = (str(miles) +' miles\n' + str(yards) + ' yards\n' + str(feet) + ' feet\n' + str(inches) + ' inches\n' +
                       str(kilometers) + ' kilometers\n' + str(meters) + ' meters\n' + str(centimeters) + ' centimeters')
    return converted


def convert_naut_miles(number):
    print(number, 'miles is equal to:')
    print('\t', number * 1.15078, 'miles')
    print('\t', number * 2025.37, 'yards')
    print('\t', number * 6076.12, 'feet')
    print('\t', number * 72913.4, 'inches')
    print('\t', number * 1.852, 'kilometers')
    print('\t', number * 1852, 'meters')
    print('\t', number * 185200, 'centimeters')
    print('\t', number, 'nautical miles')


class Distance:
    def distance(self, amount, type):
        if type == "Miles":
            answer_label = convert_miles(amount)
            return answer_label
        elif type == "Yards":
            answer_label = convert_yards(amount)
            return answer_label
        elif type == "Feet":
            answer_label = convert_feet(amount)
            return answer_label
        elif type == "Inches":
            answer_label = convert_inches(amount)
            return answer_label
        elif type == "Kilometers":
            answer_label = convert_km(amount)
            return answer_label
        elif type == "Meters":
            answer_label = convert_meters(amount)
            return answer_label
        elif type == "Centimeters":
            answer_label = convert_cm(amount)
            return answer_label




