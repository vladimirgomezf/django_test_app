from django.db import models

evaluacion = [
    ("B", "Bien"),
    ("R", "Regular"),
    ("M", "Mal"),
]

class Persona(models.Model):
    nombre = models.CharField('Nombre', max_length=20, blank=False, null=False)
    apellido = models.CharField('Apellidos', max_length=50, blank=False, null=False)
    ci = models.CharField('Carné de Identidad', max_length=11, blank=False, null=False)
    dir = models.CharField('Dirección', max_length=75, blank=True, null=True)
    tel = models.CharField('Teléfono', max_length=30, blank=True, null=True)
    email = models.EmailField('Email')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Universidad(models.Model):
    name = models.CharField('Nombre', max_length=20, blank=False, null=False)
    dir = models.CharField('Dirección', max_length=75, blank=True, null=True)

    def __str__(self):
        return self.name

class Carrera(models.Model):
    name = models.CharField('Nombre', max_length=20, blank=False, null=False)
    responsable = models.OneToOneField(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profesor(Persona):
    uni = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    carrera = models.ManyToManyField(Carrera)
    depto = models.CharField('Departamento', max_length=20, blank=False, null=False)
    evaluacion = models.CharField('Evaluación', max_length=20, choices=evaluacion)
    asignatura = models.CharField('Asignatura', max_length=20, blank=False, null=False)

    def __str__(self):
        return f"Profesor: {self.nombre}  {self.apellido} ({self.uni.name})"


class Estudiante(Persona):
    year = models.CharField('Año Académico', max_length=20, blank=False, null=False)
    prom = models.FloatField('Promedio', default=0)
    ayudante = models.BooleanField('Es alumno ayudante?', default=False)

    def __str__(self):
        return f"{self.nombre, self.apellido, self.ci, self.dir, self.tel, self.email, self.year, self.prom, self.ayudante}"