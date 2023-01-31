"""
    cuadrado.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion:perimetro y area de un cuadrado
"""
lado1 = None
while True:
  try:
    lado1 = float(input("Escriba la lado del cuadrado: "))
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  
    print("Debe escribir un numero")

perimetro = lado1
print("el perimetro del cuadrado con lado de: {}, es: {}" .format(lado1, perimetro))
