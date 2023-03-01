"""
    programa11v.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion:distintas formas de usar if
"""
#version 1
numero1 = int(input("escriba un numero: ")) # imprime el texto
numero2 = int(input("escriba un numero:  # imprime el texto
if numero1 < numero2 :   # hace un bloque de codigo de desicion
    print("El numero menor es: {}".format(numero2))  #  ipmprime el texto
elif numero2 < numero1 :
    print("El numero menor es: {}".format(numero1))  #  ipmprime el texto
else:
    print(None)
#version 2
numero1 = int(input("escriba un numero: "))  #  ipmprime el texto
numero2 = int(input("escriba un numero: "))  #  ipmprime el texto
if numero1 <= numero2 :  # hace un bloque de codigo de desicion
    if numero1 < numero2 :  # hace un bloque de codigo de desicion
        print(numero2)  #  ipmprime la variable
    elif numero1 == numero2 :
        print(None)  #  ipmprime valor nulo
    else: 
        print(numero1)   #  ipmprime la variable
#version 3
numero1 = int(input("escriba un numero: "))  #  ipmprime el texto
numero2 = int(input("escriba un numero: "))  #  ipmprime el texto
if numero1 >= numero2 : # hace un bloque de codigo de desicion
    if numero1 > numero2 :
        print(numero1)  #  ipmprime la variable
    elif numero1 == numero2 : 
        print(None)  #  ipmprime valor nulo
    else:
        print(numero2)  #  ipmprime la variable
