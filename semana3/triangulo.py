"""
    triangulo.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion: peerimetro y area del triangulo
"""
base = None  #  el comando None denota falta de valor
altura = None  #  el comando None denota falta de valor 
while True:
  try:
    base = float(input("Escriba la base del triangulo: "))
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  
    print("Debe escribir un numero")
while True:
  try:
    altura = float(input("Escriba la altura del triangulo: "))
    break
  except:  
    print("Debe escribir un numero")
area = base * altura / 2
print("El area del triangulo es igual: {}".format(area))
    