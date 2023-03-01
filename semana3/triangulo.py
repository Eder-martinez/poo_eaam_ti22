"""
    triangulo.py
    nombre:Eder AAM
    fecha:30/01/2023
    descripcion: perimetro y area del triangulo
"""
base = None  #  el comando None denota falta de valor
altura = None  #  el comando None denota falta de valor 
ladoa = None  #  el comando None denota falta de valor
ladob = None  #  el comando None denota falta de valor
ladoc = None  #  el comando None denota falta de valor
while True:  #  while es una estructura cíclica, que nos permite ejecutar una o varias líneas de código de manera repetitiva sin necesidad de tener un valor inicial e incluso a veces sin siquiera conocer cuando se va a dar el valor final que esperamos
  try:  #  Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción
    ladoa = float(input("Escriba la ladoa del triangulo: "))  #  le da valor a un avariable
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  #  se logra establecer una condición en caso de que se generará un error dentro del bloque Try  
    print("Debe escribir un numero") #  ipmprime el texto
while True:  #  while es una estructura cíclica, que nos permite ejecutar una o varias líneas de código de manera repetitiva sin necesidad de tener un valor inicial e incluso a veces sin siquiera conocer cuando se va a dar el valor final que esperamos
  try:   #  Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción
    ladob = float(input("Escriba la ladob del triangulo: "))  #  le da valor a un avariable
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  
    print("Debe escribir un numero") #  ipmprime el texto
while True:  #  while es una estructura cíclica, que nos permite ejecutar una o varias líneas de código de manera repetitiva sin necesidad de tener un valor inicial e incluso a veces sin siquiera conocer cuando se va a dar el valor final que esperamos
  try:  #  Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción
    ladoc = float(input("Escriba la ladoc del triangulo: "))  #  le da valor a un avariable
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  
    print("Debe escribir un numero") #  ipmprime el texto
while True:  #  while es una estructura cíclica, que nos permite ejecutar una o varias líneas de código de manera repetitiva sin necesidad de tener un valor inicial e incluso a veces sin siquiera conocer cuando se va a dar el valor final que esperamos
  try:  #  Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción
    base = float(input("Escriba la base del triangulo: "))  #  le da valor a un avariable
    break  #  el comando break hace un bucle en cuano se da una condicion externa
  except:  
    print("Debe escribir un numero") #  ipmprime el texto
while True:  #  while es una estructura cíclica, que nos permite ejecutar una o varias líneas de código de manera repetitiva sin necesidad de tener un valor inicial e incluso a veces sin siquiera conocer cuando se va a dar el valor final que esperamos
  try:  #  Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción
    altura = float(input("Escriba la altura del triangulo: "))  #  le da valor a un avariable
    break   #  el comando break hace un bucle en cuano se da una condicion externa
  except:  
    print("Debe escribir un numero")  #  ipmprime el texto
area = base * altura / 2  #  le da valor a un avariable
print("El area del triangulo es igual: {}".format(area)) # imprime el resultado
perimetro = ladoa + ladob + ladoc  #  le da valor a un avariable
print("El perimetro del triangulo es igual: {}".format(perimetro)) # imprime el resultado
