Característica: Calcular promedio de calificaciones
  Como un usuario de la calculadora
  Quiero calcular el promedio de varias calificaciones
  Para obtener el resultado basado en los criterios de validación de entrada

  Escenario: Calcular promedio correctamente
    Dado que el usuario ingresa las calificaciones "[8, 9, 10]"
    Cuando calculo el promedio
    Entonces puedo ver el resultado igual a "9"

  Escenario: Ingreso de valores nulos
    Dado que el usuario ingresa las calificaciones "[8,None,7]"
    Cuando calculo el promedio
    Entonces puedo ver el mensaje: "No se aceptan valores nulos"

  Escenario: Ingreso de datos no numéricos
    Dado que el usuario ingresa las calificaciones "[8,'nueve',7]"
    Cuando calculo el promedio
    Entonces puedo ver el mensaje: "Solo se aceptan numeros"

  Escenario: Calificaciones no positivas
    Dado que el usuario ingresa las calificaciones "[0,8,7]"
    Cuando calculo el promedio
    Entonces puedo ver el mensaje: "Solo calificaciones mayores a cero"

  Escenario: Calificaciones superiores al máximo permitido
    Dado que el usuario ingresa las calificaciones "[8,11,7]"
    Cuando calculo el promedio
    Entonces puedo ver el mensaje: "Solo calificaciones menores o iguales a 10"
