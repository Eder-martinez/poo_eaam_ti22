"""
    programav.py
    nombre:Eder AAM
    fecha:08/02/2023
    descripcion:comando def
"""
def mayor(numero1, numero2):
    if numero1 > numero2 :
        print(numero1)
    elif numero2 > numero1 :
        print(numero2)
    else: 
        print(None)
mayor(3,2)#3
mayor(2,3)#3
mayor(3,3)#None
# version 2
def mayor(numero1:int, numero2:int)->int:
    mayor = None
    if numero1 > numero2 : 
        mayor = numero1
    elif numero2 > numero1 :
        mayor = numero2
    else:
        mayor = None
    return mayor    
print(mayor(3,2))#3        
print(mayor(2,3))#3
print(mayor(3,3))#None
