from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Candidato(models.Model):
    nombre = models.CharField(max_length=50)
    aPaterno = models.CharField(max_length=50)
    aMaterno = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos')
    Partido = models.ForeignKey("candidatos.Partido", verbose_name="Partido", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre  

class Votacion(models.Model):
    candidato = models.ForeignKey("candidatos.Candidato", verbose_name="Candidato", on_delete=models.CASCADE)  
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fecha_hora.strftime("%Y-%m-%d %H:%M:%S")

    