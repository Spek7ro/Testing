Característica: Convertir formato de fecha a texto
  Como usuario quiero poder introducir una fecha
  y obtener la fecha en formato textual descriptivo.

  Escenario: Convertir una fecha válida
    Dado que el usuario ingresa la fecha "25/12/2021"
    Cuando se convierte la fecha a texto
    Entonces el resultado debe ser "Día veinticinco de Diciembre de dos mil veintiuno."

  Escenario: Intentar convertir con un día inválido
    Dado que el usuario ingresa la fecha "32/10/2021"
    Cuando se convierte la fecha a texto
    Entonces el resultado debe ser "Día inválido"

  Escenario: Intentar convertir con un mes inválido
    Dado que el usuario ingresa la fecha "10/13/2021"
    Cuando se convierte la fecha a texto
    Entonces el resultado debe ser "Mes inválido"

  Escenario: Intentar convertir con un año inválido
    Dado que el usuario ingresa la fecha "10/10/-50"
    Cuando se convierte la fecha a texto
    Entonces el resultado debe ser "Año inválido"
