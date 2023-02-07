"""
    programa11v.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion:distintas formas de usar if
"""
#version 1
numero1 = int(input("escriba un numero: "))
numero2 = int(input("escriba un numero: "))
if numero1 < numero2 : 
    print("El numero menor es: {}".format(numero1))
elif numero2 < numero1 :
    print("El numero menor es: {}".format(numero2))
else:
    print(None)
#version 2
numero1 = int(input("escriba un numero: "))
numero2 = int(input("escriba un numero: "))
if numero1 <= numero2 : 
    if numero1 < numero2 :
        print(numero2)
    else:
        print(None)
else: 
    print(numero1)
#version 3
numero1 = int(input("escriba un numero: "))
numero2 = int(input("escriba un numero: "))
if numero1 >= numero2 : 
    if numero1 > numero2 :
        print(numero1)
    else: 
        print(None)
else:
    print(numero2)
#version 4
