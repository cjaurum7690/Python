def convert_celsius(number):
    celsius = int(number)
    fahrenheit = round(((int(number) * 9 / 5) + 32), 2)
    kelvin = round((int(number) + 273.15), 2)

    converted = (str(celsius) + ' Celsius\n' + str(fahrenheit) + ' Fahrenheit\n' + str(kelvin) + ' Kelvin')
    return converted


def convert_fahrenheit(number):
    celsius = round(((int(number) - 32) * (5/9)), 2)
    fahrenheit = int(number)
    kelvin = round(((int(number) - 32) * (5/9) + 273.15), 2)

    converted = (str(celsius) + ' Celsius\n' + str(fahrenheit) + ' Fahrenheit\n' + str(kelvin) + ' Kelvin')
    return converted


def convert_kelvin(number):
    celsius = round((int(number) - 273.15), 2)
    fahrenheit = round(((int(number) - 273.15) * (9 / 5) + 32), 2)
    kelvin = int(number)

    converted = (str(celsius) + ' Celsius\n' + str(fahrenheit) + ' Fahrenheit\n' + str(kelvin) + ' Kelvin')
    return converted


class Temp:
    def temperature(self, amount, type):
        if type == "Celsius":
            answer_label = convert_celsius(amount)
            return answer_label
        elif type == "Fahrenheit":
            answer_label = convert_fahrenheit(amount)
            return answer_label
        elif type == "Kelvin":
            answer_label = convert_kelvin(amount)
            return answer_label
