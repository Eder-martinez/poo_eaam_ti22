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
    print("Debe escribir un numero")  # imprime el texto
perimetro = radio * 2 * 3.1416  # le da valor a un avariable multiplicandio otra variable y valores enteros
print("El perimetro de un circulo con un radio de: {}, es: {}" .format(radio, perimetro))  #  imprime el texto incluyendo las variables
area = 3.1416 * (radio**2)  # le asigna valor a un avariable nueva
print("El area del circulo con un radio de: {}, es: {}" .format(radio, area))  #  imprime la variable nueva y la anterior
