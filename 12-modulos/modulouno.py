""" Modulo ejemplo """


def holamundo(nombre):
    """ Hola """
    return f"Hola {nombre}"


def calculadora(num1, num2, basicas=False, todos=False):
    """ calculadora """
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    concatcalc = ""

    if todos is not False:
        concatcalc += "Suma: " + str(suma)
        concatcalc += "\nResta: " + str(resta)
        concatcalc += "\nMultiplicacion: " + str(multi)
        concatcalc += "\nDivision: " + str(div)

    elif basicas is not False:
        concatcalc += "Suma: " + str(suma)
        concatcalc += "\nResta: " + str(resta)

    else:
        concatcalc += "Multiplicacion: " + str(multi)
        concatcalc += "\nDivision: " + str(div)

    return concatcalc
