""" 
en el siguiente ejercicio se solicita calcular el area y el 
perimetro de un rectangulo para ello deberemos crear las sigueientes 
variables: alto y ancho

el usuario debe proporcionar los valores de largo y ancho  y despues
se debe imprimir  el resultado 
"""

alto= int(input('ingrese el alto de un rectangulo: '))

ancho = int(input('ingrese el ancho: '))

area =ancho *  alto

perimetro =2*(ancho + alto)

print(f' el area de un rectangulo es {area} y su perimeto es {perimetro}')