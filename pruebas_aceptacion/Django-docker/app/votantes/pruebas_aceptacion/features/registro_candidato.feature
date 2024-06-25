Característica: Registro de candidato 
Como administrador del sistema de votacion 
quiero registrar un candidato para que sea votado.

Escenario: Registar al Claudia Sheinbaum Pardo
Dado que ingreso a la url "http://localhost:8000/admin/login"
Y escribo mi usuario "admin" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace Candidatos
Y luego clik en el boton de Agregar candidato
Y escribo el nombre del candidato "Claudia"
Y escribo el apellido paterno del candidato "Sheinbaum"
Y escribo el apellido materno del candidato "Pardo"
Y selecciono la imagen del candidato "C:/Users/20201/Downloads/images.jpg"
Y selecciono el partido "Morena"
Cuando presiono el boton Guardar
Entonces puedo ver el candidato "Claudia" en la lista de candidatos
