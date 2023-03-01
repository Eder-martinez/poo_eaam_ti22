class Persona: # clase persona
    __nombre = None # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
    __edad = None # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
    def __init__(self): # constructor de la clase persona
        print("Persona") # imprime el texto persona
    def setNombre(self, nombre): # funcion para modificar la variable privada __nombre
        self.__nombre = nombre
    def getNombre(self): # funcion que regresa el valor ed la variable privada __nombre
        return self.__nombre # regresa el valor de la variable privada __nombre
    def setEdad(self, edad):  # funcion para modificar la variable privada __edad
        self.__edad = edad  # modifica el valor de la variable privada __edad y le asigna uno nuevo
    def getEdad(self):  # funcion que regresa el valor ed la variable privada __edad
        return self.__edad  # regresa el valor de la variable privada __edad

class Alumno(Persona): # clase alumno
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

class Coordinador(Persona): # clase coordinador
    __no_nomina = None # valor nulo
    __carrera_coordina = None # valor nulo
    def __init__(self):   # constructor de la clase persona
        print("Coordinador") # imprime
    def setNombre(self, nombre): # modifica la variable
        self.__nombre = nombre # le da valor a una variable
    def getNombre(self): # modifica variable
        return self.__nombre # retorna el valor
    def setNoNomina(self, no_nomina): # modifica la variable
        self.__no.nomina = no_nomina # le da valor a la variable
    def getNoNomina(self): # modifica la variable
        return self.__no.nomina # retorna el valor
    def setCarreraCoordina(self, carrera_coordina): # modifica la variable
        self.__carrera.coordina = carrera_coordina
    def getCarreraCoordina(self): # modifica la variable
        return self.__carrera.coordina # retorna el valor

class Profesor(Persona): # crea la clase
    __no_nomina = None # valor nulo
    def __init__(self): # crea la clase
        print("Profesor") # imprime
    def setNombre(self, nombre): # modifica la variable
        self.__nombre = nombre # le da valor a la variable
    def getNombre(self): # modifica la variable
        return self.__nombre # retorna el valor
    def setNoNomina(self, no_nomina): # modifica la variable
        self.__no.nomina = no_nomina # le da valor a la variable
    def getNoNomina(self): # modifica la variable
        return self.__no.nomina # retorna el valor

objeto_persona = Persona()  # llama a la clase
objeto_persona.nombre = "Dejah Thoris" # le da valor a la variable
print(objeto_persona.nombre) # imprime
objeto_persona.edad = "25" # le da valor a la variable
print(objeto_persona.edad) # imprime
objeto_alumno = Alumno()  # llama a la clase
objeto_alumno.nombre = "John Carter" # le da valor a la variable
print(objeto_alumno.nombre) # imprime
objeto_coordinador = Coordinador()  # llama a la clase
objeto_coordinador.nombre = "ci" # le da valor a la variable
print(objeto_coordinador.nombre) # imprime
objeto_profesor = Profesor()  # llama a la clase
objeto_profesor.nombre = "Sara" # le da valor a la variable
print(objeto_profesor.nombre) # imprime
