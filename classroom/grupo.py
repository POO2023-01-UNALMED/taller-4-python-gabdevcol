from functools import cached_property

from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        if estudiantes == None:
            estudiantes=[]
        # elif type(estudiantes) == list:
        #     estudiantes.sort()
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            Asignatura(x)
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno=None, lista=False):

        if lista:
            lista.append(alumno)
            lista.sort()
            self.listadoAlumnos += lista
        else:
            self.listadoAlumnos.append(alumno)



    # def __str__(self):
    #     pass


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        cadena = f"Grupo de estudiantes: {self._grupo}"
        return cadena

    # def __str__(self):
    #     cadena= f"{self._grupo} {self._asignaturas} {self.listadoAlumnos} {self.grado}"
    #     return cadena

# if __name__ == "__main__":
#     asignatura1 = Asignatura("Vision por Computador")
#     asignatura2 = Asignatura("POO", "Salon 503B")
#
#     grupo = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])
#     grupo.listadoAsignaturas(asignatura1="Fundamentos de programacion",
#                              asignatura2="Ecuaciones diferenciales",
#                              asignatura3="Inteligencia artificial")
#
#     ok = False
#     if grupo._asignaturas[0]._nombre == "Vision por Computador" and \
#             grupo._asignaturas[1]._nombre == "POO" and \
#             grupo._asignaturas[2]._nombre == "Fundamentos de programacion" and \
#             grupo._asignaturas[3]._nombre == "Ecuaciones diferenciales" and \
#             grupo._asignaturas[4]._nombre == "Inteligencia artificial":
#         ok = True
#
#     print(ok)

