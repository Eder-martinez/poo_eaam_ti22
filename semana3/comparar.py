"""
    programa4.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion:comando input 
"""
numero1 = int(input("escriba un numero: "))  #  le aigna un valor a una variable
numero2 = int(input("escriba un numero: ")) #  le aigna un valor a una variable
if numero1 < numero2 : #  crea un bleque de codigo de desicion 
    print("El numero menor es: {}".format(numero1))  # imprime el texto con la variable
elif numero2 < numero1 : #  hace una segunda opcion 
    print("El numero menor es: {}".format(numero2))  #  imprime la segunda opcion 
else:  #  hace un atercera opcion
    print(None) # imprime un valor nnulo
    