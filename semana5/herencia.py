class Persona:  # clase persona
    def __init__(self):  # constructor de la clase persona
        __nombre = None # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
        __edad = None # la funcion none le asigna un valor nulo a la variable, los guiones antes de la variable indica que es privada
        print("Persona")  # imprime el texto persona

class Alumno(Persona): # clase alumno
    def __init__ (self):  # constructor de la clase alumno
        super().__init__()  #  llama a la clase persona
        print("Alumno")  #  imprime el texto alumno

objeto_persona = Persona() # variable ligada a clase persona
objeto_alumno = Alumno() # variable ligada a clase alumno

objeto_persona.nombre = "Dejah Thoris"  #  le otorga un valor a un avariable ligada a la variable nombre
print(objeto_persona.nombre)  #  imprime el valor de la variable

objeto_alumno.nombre = "John Carter"  #  le otorga un valor a un avariable ligada a la variable nombre
print(objeto_alumno.nombre)  #  imprime el valor de la variable

objeto_alumno.email = "john@utectulancingo.edu.mx"  #  le otorga un valor a un avariable ligada a la variable email
print(objeto_alumno.email)  #  imprime el valor de la variable

print(dir(objeto_persona))  # imprime la variable ligada a clase persona # variable ligada a clase persona
print(dir(objeto_alumno))  # imprime la variable ligada a clase persona # variable ligada a clase alumno
