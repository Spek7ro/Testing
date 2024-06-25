from numeroTexto import numeroALetra

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

def fechaTexto(fecha):
    dia, mes, anio = map(int, fecha.split('/'))

    cadena_dia = numeroALetra(dia)
    cadena_mes = meses.get(mes)
    cadena_anio = numeroALetra(anio)

    return ('Día inválido' if not 1 <= dia <= 31 else
            'Mes inválido' if not 1 <= mes <= 12 else
            'Año inválido' if anio <= 0 else
            f"Día {cadena_dia} de {cadena_mes} de {cadena_anio}.")
