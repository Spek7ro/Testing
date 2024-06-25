Característica: Inicio de sesión
Como usuario del sistema de tribunal
quiero iniciar sesión
para realizar mis actividades.

Escenario: Credenciales validas
Dado que ingreso a la url "https://ingsoftware3.uaz.edu.mx/tribunal/usuario/ingreso/"
Y escribo  mi usuario "usuario-tribunal" y mi contraseña "Admin1234@"
Cuando presiono el botón de Ingresar
Entonces puedo ver mi usuario "usuario-tribunal" en la barra principal

Escenario: Credenciales invalidas
Dado que ingreso a la url "https://ingsoftware3.uaz.edu.mx/tribunal/usuario/ingreso/"
Y escribo  mi usuario "usuario123" y mi contraseña "12345678"
Cuando presiono el botón de Ingresar
Entonces puedo ver el mensaje "Datos incorrectos, intente de nuevo."
