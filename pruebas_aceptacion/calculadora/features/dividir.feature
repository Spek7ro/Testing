Característica: División de números
Como usuario de la calculadora, quiero dividir dos números para obtener su cociente, asegurándome de que las entradas sean válidas.

  Escenario: Dividir dos números enteros positivos
    Dado que el usuario ingresa los números "10" y "2"
    Cuando realizo la división
    Entonces puedo ver el resultado igual a "5"

  Escenario: Intentar dividir usando una cadena de texto
    Dado que el usuario ingresa la cadena "a" y el numero "2"
    Cuando realizo la división
    Entonces puedo ver el mensaje: "Solo se aceptan numeros"

  Escenario: Intentar dividir usando listas
    Dado que el usuario ingresa la lista "[1,2]" y el numero "2"
    Cuando realizo la división
    Entonces puedo ver el mensaje: "Solo acepto numeros no listas"

  Escenario: Dividir con números no enteros
    Dado que el usuario ingresa los números "4.5" y "2"
    Cuando realizo la división
    Entonces puedo ver el mensaje: "Solo numeros enteros"

  Escenario: Dividir números negativos
    Dado que el usuario ingresa los números "-8" y "2"
    Cuando realizo la división
    Entonces puedo ver el mensaje: "Solo numeros positivos"

  Escenario: Dividir por cero
    Dado que el usuario ingresa los números "8" y "0"
    Cuando realizo la división
    Entonces puedo ver el mensaje: "No se puede dividir entre cero"
