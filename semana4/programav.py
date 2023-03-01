"""
    programav.py
    nombre:Eder AAM
    fecha:08/02/2023
    descripcion:comando def
"""
def mayor(numero1, numero2):  # hace un bloque de codigo de desicion
    if numero1 > numero2 :  # hace un bloque de codigo de desicion
        print(numero1) #imprime
    elif numero2 > numero1 :  # hace un asegunda opcion 
        print(numero2) # imprime
    else:   # hace una tercera opcion 
        print(None) # imprime
mayor(3,2)#3
mayor(2,3)#3
mayor(3,3)#None
# version 2
def mayor(numero1:int, numero2:int)->int:   # hace un bloqeu de codigo
    mayor = None # valor nulo
    if numero1 > numero2 :    # hace un bloqeu de codigo
        mayor = numero1 # variable
    elif numero2 > numero1 :   # hace un asegunda opcion 
        mayor = numero2 # variable
    else:  # hace un tercera opcion 
        mayor = None  # valor nulo
    return mayor    # retorna al principio
print(mayor(3,2))#3        
print(mayor(2,3))#3
print(mayor(3,3))#None
