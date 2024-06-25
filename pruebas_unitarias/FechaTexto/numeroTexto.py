MAX_NUMERO = 1000000000

UNIDADES = (
    'cero',
    'uno',
    'dos',
    'tres',
    'cuatro',
    'cinco',
    'seis',
    'siete',
    'ocho',
    'nueve'
)

DECENAS = (
    'diez',
    'once',
    'doce',
    'trece',
    'catorce',
    'quince',
    'dieciseis',
    'diecisiete',
    'dieciocho',
    'diecinueve'
)

DIEZ_DIEZ = (
    'cero',
    'diez',
    'veinte',
    'treinta',
    'cuarenta',
    'cincuenta',
    'sesenta',
    'setenta',
    'ochenta',
    'noventa'
)

CIENTOS = (
    '_',
    'ciento',
    'doscientos',
    'trescientos',
    'cuatroscientos',
    'quinientos',
    'seiscientos',
    'setecientos',
    'ochocientos',
    'novecientos'
)


def numeroALetra(numero):
    if isinstance(numero, float):
        return 'Solo se aceptan numeros enteros'
    elif not (isinstance(numero, int)):
        return 'Solo se aceptan numeros'
    elif numero < 0:
        return 'Solo se aceptan numeros positivos'
    elif numero >= MAX_NUMERO:
        return 'Solo se aceptan numeros menores a 1,000,000,000'
    else:
        if numero <= 99:
            resultado = leer_decenas(numero)
        elif numero <= 999:
            resultado = leer_centenas(numero)
        elif numero <= 999999:
            resultado = leer_miles(numero)

        resultado = resultado.replace('UNO MIL', 'UN MIL')
        resultado = resultado.strip()
        resultado = resultado.replace(' _ ', ' ')
        resultado = resultado.replace('  ', ' ')
        return resultado


def leer_decenas(numero):
    if numero < 10:
        return UNIDADES[numero]
    decena, unidad = divmod(numero, 10)
    if numero <= 19:
        resultado = DECENAS[unidad]
    elif numero == 20:
        resultado = DIEZ_DIEZ[2]
    elif numero <= 29:
        resultado = 'veinti%s' % UNIDADES[unidad]
    else:
        resultado = DIEZ_DIEZ[decena]
        if unidad > 0:
            resultado = '%s y %s' % (resultado, UNIDADES[unidad])
    return resultado


def leer_centenas(numero):
    centena, decena = divmod(numero, 100)
    if numero == 100:
        return "cien"
    else:
        resultado = CIENTOS[centena]
    if decena > 0:
        resultado = '{} {}'.format(resultado, leer_decenas(decena))
    return resultado


def leer_miles(numero):
    millar, centena = divmod(numero, 1000)
    resultado = ''
    if millar == 1:
        resultado = ''
    if (millar >= 2) and (millar <= 9):
        resultado = UNIDADES[millar]
    elif (millar >= 10) and (millar <= 99):
        resultado = leer_decenas(millar)
    elif (millar >= 100) and (millar <= 999):
        resultado = leer_centenas(millar)
    resultado = f"{resultado} mil"
    if centena > 0:
        centena_letras = leer_centenas(centena)
        resultado = f"{resultado} {centena_letras}"
    return resultado.strip()
