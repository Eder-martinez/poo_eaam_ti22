class Alumno:
    __nombre = None
    __matricula = None
    __carrera = None    
    def __init__(self):
        print("Persona")
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
dejah = Alumno()
dejah.setNombre("Dejah")
print(dejah. getNombre())
dejah.setMatricula("1722110109")
print(dejah. getMatricula())
dejah.setCarrera("Desarrollo de software")
print(dejah. getCarrera())
