
def promedio(*args):
    # Comprobar si hay valores nulos
    if any(arg is None for arg in args):
        return 'No se aceptan valores nulos'
    
    # Comprobar si todos los argumentos son números
    if not all(isinstance(arg, (int, float)) for arg in args):
        return 'Solo se aceptan numeros'
    
    # Comprobar si todas las calificaciones son mayores a cero
    if any(arg <= 0 for arg in args):
        return 'Solo calificaciones mayores a cero'
    
    # Comprobar si todas las calificaciones son menores o iguales a 10
    if any(arg > 10 for arg in args):
        return 'Solo calificaciones menores o iguales a 10'
    
    # Calcular el promedio si se pasan todas las comprobaciones
    promedio = sum(args) / len(args)
    return round(promedio)

