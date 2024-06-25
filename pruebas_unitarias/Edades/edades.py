# Clasifica a las personas según su edad en diferentes categorías.

def clasificar_edad(edad):
    if not isinstance(edad, int):
        return 'Solo se aceptan números enteros'
    if edad < 0:
        return 'No existes'
    elif edad < 13:
        return 'Eres niño'
    elif edad < 18:
        return 'Eres adolescente'
    elif edad < 65:
        return 'Eres adulto'
    elif edad < 120:
        return 'Eres adulto mayor'
    else:
        return 'Eres Mumm-Ra'


'''
Si es menor de 0: No existes
Si es menor de 13: Eres niño
Si es menor de 18: Eres adolescente
Si es menor de 65: Eres adulto
Si es menor de 120: Eres adulto mayor
De lo contrario: Eres Mumm-Ra

'''
