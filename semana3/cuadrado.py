"""
    cuadrado.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion:perimetro y area de un cuadrado
"""
lado1 = None  #  valor nulo
while True:  #  hace un bloque de codigo
  try:
    lado1 = float(input("Escriba la lado del cuadrado: "))  #  le valor a una variable
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  #  hace una ecepcion 
    print("Debe escribir un numero") # imprime el texto

perimetro = lado1 # l eda valor a un avariable
print("el perimetro del cuadrado con lado de: {}, es: {}" .format(lado1, perimetro)) #  imprime el texto con la variable
