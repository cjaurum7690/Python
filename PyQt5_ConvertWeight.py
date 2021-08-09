def convert_pounds(number):
    pounds = round(int(number), 2)
    ounces = round((int(number) * 16), 2)
    tons = round((int(number) * .0005), 4)
    kilograms = round(int(number) * .453592, 2)
    grams = round(int(number) * 453.592, 2)
    stones = round(int(number) * .0714286, 2)

    converted = (str(pounds) + ' Pounds\n' + str(ounces) + ' Ounces\n' + str(tons) + ' US Tons\n' +
                 str(kilograms) + ' Kilograms\n' + str(grams) + ' Grams\n' + str(stones) + ' Stones')
    return converted


def convert_ounces(number):
    pounds = round(int(number) * .0625, 4)
    ounces = round(int(number), 2)
    tons = round((int(number) * .00003125), 6)
    kilograms = round(int(number) * .0283495, 2)
    grams = round(int(number) * 28.3495, 2)
    stones = round(int(number) * .00446429, 6)

    converted = (str(pounds) + ' Pounds\n' + str(ounces) + ' Ounces\n' + str(tons) + ' US Tons\n' +
                 str(kilograms) + ' Kilograms\n' + str(grams) + ' Grams\n' + str(stones) + ' Stones')
    return converted


def convert_tons(number):
    pounds = round(int(number) * 2000, 2)
    ounces = round(int(number) * 32000, 2)
    tons = round(int(number), 4)
    kilograms = round(int(number) * 907.185, 2)
    grams = round(int(number) * 907185, 2)
    stones = round(int(number) * 142.857, 2)

    converted = (str(pounds) + ' Pounds\n' + str(ounces) + ' Ounces\n' + str(tons) + ' US Tons\n' +
                 str(kilograms) + ' Kilograms\n' + str(grams) + ' Grams\n' + str(stones) + ' Stones')
    return converted


def convert_kilograms(number):
    pounds = round(int(number) * 2.20462, 2)
    ounces = round(int(number) * 35.274, 2)
    tons = round(int(number) * .00110231, 4)
    kilograms = round(int(number), 2)
    grams = round(int(number) * 1000, 2)
    stones = round(int(number) * .157473, 2)

    converted = (str(pounds) + ' Pounds\n' + str(ounces) + ' Ounces\n' + str(tons) + ' US Tons\n' +
                 str(kilograms) + ' Kilograms\n' + str(grams) + ' Grams\n' + str(stones) + ' Stones')
    return converted


def convert_grams(number):
    pounds = round(int(number) * .00220462, 4)
    ounces = round(int(number) * .035274, 2)
    tons = round(int(number) * .0000011023, 6)
    kilograms = round(int(number) * .001, 2)
    grams = round(int(number), 2)
    stones = round(int(number) * .000157473, 6)

    converted = (str(pounds) + ' Pounds\n' + str(ounces) + ' Ounces\n' + str(tons) + ' US Tons\n' +
                 str(kilograms) + ' Kilograms\n' + str(grams) + ' Grams\n' + str(stones) + ' Stones')
    return converted


def convert_stones(number):
    pounds = round(int(number) * 14, 2)
    ounces = round(int(number) * 224, 2)
    tons = round(int(number) * .007, 4)
    kilograms = round(int(number) * 6.35029, 2)
    grams = round(int(number) * 6350.29, 2)
    stones = round(int(number), 2)

    converted = (str(pounds) + ' Pounds\n' + str(ounces) + ' Ounces\n' + str(tons) + ' US Tons\n' +
                 str(kilograms) + ' Kilograms\n' + str(grams) + ' Grams\n' + str(stones) + ' Stones')
    return converted


class Weight:
    def weight(self, amount, type):
        if type == "Pounds":
            answer_label = convert_pounds(amount)
            return answer_label
        elif type == "Kilograms":
            answer_label = convert_kilograms(amount)
            return answer_label
        elif type == "Ounces":
            answer_label = convert_ounces(amount)
            return answer_label
        elif type == "Grams":
            answer_label = convert_grams(amount)
            return answer_label
        elif type == "US Tons":
            answer_label = convert_tons(amount)
            return answer_label
        elif type == "Stones":
            answer_label = convert_stones(amount)
            return answer_label


