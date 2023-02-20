class Alumno:  # clase alumno
    __nombre = None  # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
    __matricula = None  # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
    __carrera = None # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada   
    def __init__(self):  # constructor de la clase persona
        print("Persona") # imprime el texto persona
    def setNombre(self, nombre):  # funcion para modificar la variable privada __nombre
        self.__nombre = nombre  # modifica el valor de la variable privada __nombre y le asigna uno nuevo
    def getNombre(self):  # funcion que regresa el valor ed la variable privada __nombre
        return self.__nombre  # regresa el valor de la variable privada __nombre
    def setMatricula(self, matricula): # funcion para modificar la variable privada __matricula
        self.__matricula = matricula # modifica el valor de la variable privada __matricula y le asigna uno nuevo
    def getMatricula(self):  # funcion que regresa el valor de la variable privada __matricula
        return self.__matricula   # regresa el valor de la variable privada __matricula
    def setCarrera(self, carrera):  # funcion para modificar la variable privada __carrera
        self.__carrera = carrera  # modifica el valor de la variable privada __carrera y le asigna uno nuevo
    def getCarrera(self):  # funcion que regresa el valor de la variable privada __carrera
        return self.__carrera  # regresa el valor de la variable privada __matricula  
dejah = Alumno()  #  asigna valor a la variable
dejah.setNombre("Dejah") # funcion para modificar la variable y asignar un nuevo valor
print(dejah. getNombre())  # imprime la funcion dejah. getNombre
dejah.setMatricula("1722110109") # funcion para modificar la variable y asignar un nuevo valor
print(dejah. getMatricula())  # imprime la funcion dejah. getMatricula
dejah.setCarrera("Desarrollo de software") # funcion para modificar la variable y asignar un nuevo valor
print(dejah. getCarrera()) # imprime la funcion dejah. getCarrera
