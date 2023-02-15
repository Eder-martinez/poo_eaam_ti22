class Persona:
    __nombre = None
    __edad = None
    def __init__(self):
        print("Persona")
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setEdad(self, edad):
        self.__edad = edad
    def getEdad(self):
        return self.__edad

class Alumno(Persona):
    __nombre = None
    __matricula = None
    __carrera = None    
    def __init__(self):
        print("Alumno")
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setMatricula(self, matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
    def setCarrera(self, carrera):
        self.__carrera = carrera
    def getCarrera(self):
        return self.__carrera 

class Coordinador(Persona):
    __no_nomina = None
    __carrera_coordina = None
    def __init__(self):
        print("Coordinador")
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setNoNomina(self, no_nomina):
        self.__no.nomina = no_nomina
    def getNoNomina(self):
        return self.__no.nomina
    def setCarreraCoordina(self, carrera_coordina):
        self.__carrera.coordina = carrera_coordina
    def getCarreraCoordina(self):
        return self.__carrera.coordina

class Profesor(Persona):
    __no_nomina = None
    def __init__(self):
        print("Profesor")
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setNoNomina(self, no_nomina):
        self.__no.nomina = no_nomina
    def getNoNomina(self):
        return self.__no.nomina

objeto_persona = Persona()
objeto_persona.nombre = "Dejah Thoris"
print(objeto_persona.nombre)
objeto_persona.edad = "25"
print(objeto_persona.edad)
objeto_alumno = Alumno()
objeto_alumno.nombre = "John Carter"
print(objeto_alumno.nombre)
objeto_coordinador = Coordinador()
objeto_coordinador.nombre = "ci"
print(objeto_coordinador.nombre)
objeto_profesor = Profesor()
objeto_profesor.nombre = "Sara"
print(objeto_profesor.nombre)
