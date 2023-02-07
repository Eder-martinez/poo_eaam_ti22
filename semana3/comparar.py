"""
    programa4.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion:comando input 
"""
numero1 = int(input("escriba un numero: "))
numero2 = int(input("escriba un numero: "))
if numero1 < numero2 : 
    print("El numero menor es: {}".format(numero1))
elif numero2 < numero1 :
    print("El numero menor es: {}".format(numero2))
else:
    print(None)
    