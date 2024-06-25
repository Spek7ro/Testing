Característica: Multiplicación de números
  Como usuario de la calculadora, quiero multiplicar dos números para obtener su producto, asegurándome de que las entradas sean válidas.

  Escenario: Multiplicar dos números enteros positivos
    Dado el usuario ingresa los números "5" y "4"
    Cuando realizo la multiplicación
    Entonces puede el usuario ver el resultado igual a "20"

  Escenario: Intentar multiplicar usando una cadena de texto
    Dado el usuario ingresa la cadena "a" y el número "5"
    Cuando realizo la multiplicación
    Entonces puede el usuario ver el mensaje: "Solo se aceptan numeros"

  Escenario: Intentar multiplicar usando listas
    Dado el usuario ingresa la lista "[1,2]" y el número "5"
    Cuando realizo la multiplicación
    Entonces puede el usuario ver el mensaje: "Solo acepto numeros no listas"

  Escenario: Multiplicar números negativos
    Dado el usuario ingresa los números "-8" y "2"
    Cuando realizo la multiplicación
    Entonces puede el usuario ver el mensaje: "Solo numeros positivos"
