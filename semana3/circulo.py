"""
    circulo.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion:perimetro y area de un circulo
"""
radio = None
while True:
  try:
    radio = float(input("Escriba la radio del circulo: "))
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  
    print("Debe escribir un numero")
perimetro = radio * 2 * 3.1416
print("El perimetro de un circulo con un radio de: {}, es: {}" .format(radio, perimetro))
area = 3.1416 * (radio**2)
print("El area del circulo con un radio de: {}, es: {}" .format(radio, area))
