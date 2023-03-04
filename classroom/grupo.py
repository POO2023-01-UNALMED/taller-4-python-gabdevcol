from functools import cached_property

from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"
    listadoAlumnos=[]

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = [asignaturas][1:]
        self.listadoAlumnos = [estudiantes][1:]

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(x)

    def agregarAlumno(self, alumno=None, lista=False):
        self.listadoAlumnos.append(alumno)
        if lista:
            self.listadoAlumnos += lista
            self.listadoAlumnos.sort()


    # def __str__(self):
    #     pass


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        cadena = f"Grupo de estudiantes: {self._grupo}"
        return cadena
