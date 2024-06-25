Característica: Registro de partido
Como administrador del sistema de votacion 
quiero registrar un partido para que sea votado.

Escenario: Registar a Morena
Dado que ingreso a la url "http://localhost:8000/admin/login"
Y escribo mi usuario "admin" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace Partidos
Y luego clik en el boton de Agregar Partido
Y escribo el nombre del partido "Morena"
Y escribo la descripcion del partido "Morena es un partido de izquierda"
Cuando presiono el boton Guardar 
Entonces puedo ver el partido "Morena" en la lista de Partidos
