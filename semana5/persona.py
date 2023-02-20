class Persona: # clase persona
    __nombre = None # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
    __email = None # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
    def __init__(self): # constructor de la clase persona
        print("Persona") # imprime el texto persona
    def setNombre(self, nombre): # funcion para modificar la variable privada __nombre
        self.__nombre = nombre # modifica el valor de la variable privada __nombre y le asigna uno nuevo
    def getNombre(self): # funcion que regresa el valor ed la variable privada __nombre
        return self.__nombre # regresa el valor de la variable privada __nombre
    def setEmail(self, email): # funcion para modificar la variable privada __email
        self.__email = email # modifica el valor de la variable privada __email y le asigna uno nuevo
    def getEmail(self): # funcion que regresa el valor ed la variable privada __email
        return self.__email # regresa el valor de la variable privada __email
dejah = Persona()
dejah.setNombre("Dejah") # funcion para modificar la variable y asignar un nuevo valor
print(dejah. getNombre()) # imprime la funcion dejah. getNombre
dejah.setEmail("Dejah@email.com") # funcion para modificar la variable y asignar un nuevo valor
print(dejah. getEmail()) # imprime la funcion dejah. getEmail
