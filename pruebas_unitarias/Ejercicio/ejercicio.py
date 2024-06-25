'''
10. Una empresa quiere hacer una compra de varias piezas 
de la misma clase a una fábrica de refacciones. La empresa, 
dependiendo del monto total de la compra, decidirá que hacer 
para pagar al fabricante.

'''

class Ejercicio():

    def calcular_monto_total(self, precio_unitario, cantidad):
        if not isinstance(cantidad, int):
            return 'La cantidad debe ser un numero entero'
        elif not isinstance(precio_unitario, (int, float)):
            return 'El precio debe ser un numero entero o decimal'
        elif cantidad < 0 or precio_unitario < 0:
            return 'El precio y la cantidad deben ser numeros positivos'
        else:    
            return precio_unitario * cantidad


